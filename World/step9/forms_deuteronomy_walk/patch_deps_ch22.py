import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 17b (2026-09-26; LEAN): THE DEPENDENCY GATE'S DEMANDS FILED FROM ITS PRINT (ch22b_dependency_first.out) — the three AS_WHEN pointers the token census
# reads in the four chapters: Deut 22:26 "as when a man rises against his neighbor" (a comparison inside the verse — the pursuer's law read off it: FALSE), Deut 23:24 "as you vowed
# to the LORD" (the vower's own words the referent, not a text: FALSE), Deut 24:8 "as I commanded them you shall keep to do" (Leviticus 13-14's law of the plagues BEHIND — a run
# citation of the command given to the priests, no tape line of its own: RUN_CITATION). Appended to the pointers list, idempotent. RUN FROM THE REPO ROOT.
import yaml, subprocess, re
ROOT = _ROOT
P = f'{ROOT}/World/step9/dependency_dispositions.yaml'
s = open(P, encoding='utf-8').read()
W = "THE DEUTERONOMY WALK 17b (2026-09-26; LEAN) | "
NEW = [
 ('Deut 22:26', 'FALSE', 'none', "'to the girl you shall do nothing … for AS WHEN A MAN RISES AGAINST HIS NEIGHBOR AND MURDERS HIM, so is this matter' — a comparison clause inside the verse, not a pointer to a text: the pursuer's law read off it both ways (the Sifrei 243:2, 244:1 — F4 the_pursuers_law); the murderer's own law 19:11-13's the kin by CALL (refuge_war_family); no procedure fetched"),
 ('Deut 23:24', 'FALSE', 'none', "'what goes out of your lips you shall keep and do, AS YOU VOWED TO THE LORD YOUR GOD' — the vower's own utterance the referent, not a written text: the lips required (the Sifrei 266:1 — F8 what_goes_out_of_your_lips); Numbers 30's law the kin by CALL (vows); no procedure fetched"),
 ('Deut 24:8', 'RUN_CITATION', 'reference', "'take heed in the plague of leprosy … to do according to all that the Levite priests teach you; AS I COMMANDED THEM you shall keep to do' — the whole law of the plagues BEHIND (Leviticus 13:1-14:57 — the Leviticus daemons' installations, no tape line of their own): a citation of the command given to the priests (the Sifrei 274:5-6 — F10 take_heed_in_the_plague_of_leprosy); the tracks' standing verdicts by CALL (negaim), the right members by CALL (metzora); the readback row 24:8 a T4 row against the Leviticus cells (SHORTENED); no register seat (good_land.receipt_seats(24) -> [])"),
]
added = 0
for v, disp, link, why in NEW:
    key = '  - {verse: "%s", form: AS_WHEN, runner: persons_poor_court,' % v
    if key in s: continue
    entry = '%s disposition: %s, link: %s, why: %s}\n' % (key, disp, link, '"' + (W + why).replace('"', '\\"') + '"')
    m = list(re.finditer(r"^  - \{verse: \"[^\n]*\n", s, re.M))[-1]   # after the last pointer entry
    s = s[:m.end()] + entry + s[m.end():]; added += 1
open(P, 'w', encoding='utf-8').write(s)
d = yaml.safe_load(open(P, encoding='utf-8'))
mine = [p for p in d['pointers'] if p.get('runner') == 'persons_poor_court']
assert len(mine) == 3 and {p['verse'] for p in mine} == {'Deut 22:26', 'Deut 23:24', 'Deut 24:8'} and [str(p['disposition']).upper() for p in sorted(mine, key=lambda p: p['verse'])] == ['FALSE', 'FALSE', 'RUN_CITATION']   # yaml reads the bare FALSE as a boolean — the file's own form for the other FALSE pointers, mine
# THE SECOND PRINT'S DEMANDS (ch22b_dependency_first.out, the second wrap): musafim and release_firstborn are DATA reads (MU.DATA['vow_deadline'], RF.DATA['the_cry_and_the_sin']) — a CALL disposition wants a live procedure call; the read carries a VALUE: PARAMETER (15b's mishpatim precedent); the live edge to good_land (GL.receipt_seats(22..25) CALLED — the finder's count, no receipt) filed with its link (rule 9)
s2 = open(P, encoding='utf-8').read()
for to_, new_disp in (('musafim', 'PARAMETER'), ('release_firstborn', 'PARAMETER')):
    key = '  - {from: persons_poor_court, to: %s, disposition: CALL, link: reference, carries: verdict,' % to_
    if key in s2:
        assert s2.count(key) == 1, to_
        s2 = s2.replace(key, '  - {from: persons_poor_court, to: %s, disposition: %s, link: reference, carries: value,' % (to_, new_disp))
        i = s2.index('  - {from: persons_poor_court, to: %s, disposition: %s' % (to_, new_disp)); j = s2.index('why: "', i) + len('why: "')
        s2 = s2[:j] + W + "THE GATE'S PRINT (the second wrap): a DATA read, no procedure called — CALL -> PARAMETER, carries value (15b's mishpatim precedent) | " + s2[j:]
if '  - {from: persons_poor_court, to: good_land, disposition: CALL' not in s2:
    a = '  - {from: persons_poor_court, to: lev24, disposition: CALL, link: reference, carries: verdict,'
    i = s2.index(a); j = s2.index('\n', s2.index('why:', i)) + 1
    s2 = s2[:j] + '  - {from: persons_poor_court, to: good_land, disposition: CALL, link: reference, carries: verdict,\n     why: "%sthe finder\'s own count: GL.receipt_seats(22), (23), (24), (25) CALLED -> [], [], [], [] — NO receipt, footer or header in the four chapters (the register file untouched); the live edge the gate read at the second wrap (rule 9 — the file understated the code), filed with its link: reference (the finder\'s procedure, no verse cited); the three pointers AHEAD OWED under the debt line (24:16 -> 2 Kings 14:6, 25:19 -> 1 Samuel 15, 25:9 -> 27:15)"}\n' % W + s2[j:]
open(P, 'w', encoding='utf-8').write(s2)
d2 = yaml.safe_load(open(P, encoding='utf-8'))
mine_e = [e for e in d2['edges'] if e['from'] == 'persons_poor_court']
assert len(mine_e) >= 33 and {e['to']: e['disposition'] for e in mine_e}['musafim'] == 'PARAMETER' and {e['to']: e['disposition'] for e in mine_e}['release_firstborn'] == 'PARAMETER' and 'good_land' in {e['to'] for e in mine_e}, (len(mine_e), [(e['to'], e['disposition']) for e in mine_e if e['to'] in ('musafim', 'release_firstborn', 'good_land')])
print('THE EDGES AMENDED: persons_poor_court %d edges — musafim and release_firstborn PARAMETER (carries value), good_land CALL filed (rule 9); %d edges on file' % (len(mine_e), len(d2['edges'])))
print('THE DEMANDS FILED: %d pointer rows added (persons_poor_court %d on file); pointers %d; the yaml loads' % (added, len(mine), len(d['pointers'])))

# THE THIRD PRINT'S DEMANDS (ch22b_dependency_after.out): the token census reads 23:14's "and you shall turn back" (ושבת — the verb; the consonants of the Sabbath's noun) as the Sabbath's token whose home is pre_sinai — a HOMOGRAPH: FALSE; mishpatim_2 a DATA read (the PROBES row and the EFFECTS table) — PARAMETER; the sequence file's REGISTRATION edge to this runner filed (16b's form)
s3 = open(P, encoding='utf-8').read()
key = '  - {from: persons_poor_court, to: mishpatim_2, disposition: CALL, link: reference, carries: verdict,'
if key in s3:
    s3 = s3.replace(key, '  - {from: persons_poor_court, to: mishpatim_2, disposition: PARAMETER, link: reference, carries: value,')
    i = s3.index('  - {from: persons_poor_court, to: mishpatim_2, disposition: PARAMETER'); j = s3.index('why: "', i) + len('why: "')
    s3 = s3[:j] + W + "THE GATE'S PRINT (the third pass): a DATA read — the PROBES row ('fifty', 2572, 'Deut', 22, 29) and the EFFECTS table's seducer rows, no procedure called: CALL -> PARAMETER, carries value | " + s3[j:]
if '  - {from: persons_poor_court, to: pre_sinai, disposition: FALSE' not in s3:
    a = '  - {from: persons_poor_court, to: good_land, disposition: CALL, link: reference, carries: verdict,'
    i = s3.index(a); j = s3.index('\n', s3.index('why:', i)) + 1
    s3 = s3[:j] + '  - {from: persons_poor_court, to: pre_sinai, disposition: FALSE, link: none,\n     why: "%sthe token census reads 23:14\'s \'and you shall turn back\' (ושבת — the verb, and you shall turn back) as the Sabbath\'s token, whose home runner is pre_sinai: A HOMOGRAPH OF THE CENSUS — the same consonants, the verb of turning back to cover what comes from you, not the seventh day\'s noun (Onkelos \'and you shall turn back\'); no call, no procedure; 22:10-11\'s Sabbath pair is covenant_at_horeb\'s by CALL (the ox and the ass, remember and keep)"}\n' % W + s3[j:]
if '  - {from: sequence, to: persons_poor_court, disposition: CALL, link: none,' not in s3:
    a = '  - {from: sequence, to: refuge_war_family, disposition: CALL, link: none,'
    i = s3.index(a); j = s3.index('\n', s3.index('why:', i)) + 1
    s3 = s3[:j] + '  - {from: sequence, to: persons_poor_court, disposition: CALL, link: none,\n     why: "%sTHE REGISTRATION EDGE — the sequence file imports cold_run_persons_poor_court (the live edge the gate reads; DAEMON_ORDER carries law_persons_poor_court) so chapters 22-25\'s twenty own-day lines join the tape after the last Deuteronomy 21 line; no call into the runner\'s cells beyond READBACK, RB_GRADES, HOLES, OPEN_ROWS, PARAMETERS, DATA and the callees\' facts read at DK3-DK4 — 13b\'s, 14b\'s, 15b\'s and 16b\'s precedent; filed from the gate\'s own print at RUN B (FAIL LIVE EDGE sequence -> persons_poor_court has NO ENTRY on file)"}\n' % W + s3[j:]
open(P, 'w', encoding='utf-8').write(s3)
d3 = yaml.safe_load(open(P, encoding='utf-8'))
e3 = {(e['from'], e['to']): e for e in d3['edges'] if e['from'] in ('persons_poor_court', 'sequence') and (e['to'] in ('pre_sinai', 'mishpatim_2') or e['to'] == 'persons_poor_court')}
assert str(e3[('persons_poor_court', 'pre_sinai')]['disposition']).upper() == 'FALSE' and e3[('persons_poor_court', 'mishpatim_2')]['disposition'] == 'PARAMETER' and e3[('sequence', 'persons_poor_court')]['disposition'] == 'CALL', e3
print('THE THIRD SET FILED: pre_sinai FALSE (the sabbath homograph), mishpatim_2 PARAMETER, sequence -> persons_poor_court CALL; persons_poor_court edges %d; edges on file %d' % (sum(1 for e in d3['edges'] if e['from'] == 'persons_poor_court'), len(d3['edges'])))

# THE FOURTH PRINT'S DEMANDS (ch22b_dependency_after2.out): two homographs of the token census — 22:22's, 24:1's and 24:4's 'her husband' (בעלה — her husband; the consonants of 'in the burnt offering', the offerings runner's token) and 25:6's 'the firstborn' (the eldest BROTHER who takes the widow — the Sifrei 289:1; not the womb-opener of Exodus 13:2, the pesach runner's firstborn) — both FALSE, no call
s4 = open(P, encoding='utf-8').read()
a = '  - {from: persons_poor_court, to: pre_sinai, disposition: FALSE, link: none,'
i = s4.index(a); j = s4.index('\n', s4.index('why:', i)) + 1
ins = ''
if '  - {from: persons_poor_court, to: offerings, disposition: FALSE' not in s4:
    ins += '  - {from: persons_poor_court, to: offerings, disposition: FALSE, link: none,\n     why: "%sthe token census reads 22:22\'s \'married to a husband\' (בעלת בעל — married to a husband), 24:1\'s \'and marries her\' (ובעלה — and he marries her) and 24:4\'s \'her first husband\' (בעלה — her husband) as the burnt offering\'s token (עלה — the burnt offering), whose home runner is offerings: A HOMOGRAPH OF THE CENSUS — the husband\'s root, not the altar\'s ascent; Sarah\'s phrase at Genesis 20:3 the readback\'s reference (mamre — no edge); no call, no procedure"}\n' % W
if '  - {from: persons_poor_court, to: pesach, disposition: FALSE' not in s4:
    ins += '  - {from: persons_poor_court, to: pesach, disposition: FALSE, link: none,\n     why: "%sthe token census reads 25:6\'s \'the firstborn which she bears\' (הבכור — the firstborn) as the womb-opener\'s token, whose home runner is pesach (Exodus 13:2 — the firstborn for the priest): A HOMOGRAPH OF THE CENSUS — THE FIRSTBORN HERE IS THE ELDEST BROTHER who takes the widow (the Sifrei 289:1 — F14 the_firstborn_on_the_dead_brothers_name; Yevamot 2:8 and 4:5 by the English), the levirate\'s firstborn the inheritance\'s (Bekhorot 8:1\'s kinds — 16b\'s release_firstborn edge the precedent: the firstborn for inheritance is not the firstling for the priest); family\'s order_of_sons by CALL; no call into pesach"}\n' % W
s4 = s4[:j] + ins + s4[j:]
open(P, 'w', encoding='utf-8').write(s4)
d4 = yaml.safe_load(open(P, encoding='utf-8'))
e4 = {e['to']: str(e['disposition']).upper() for e in d4['edges'] if e['from'] == 'persons_poor_court'}
assert e4.get('offerings') == 'FALSE' and e4.get('pesach') == 'FALSE', e4
print('THE FOURTH SET FILED: offerings FALSE (the husband\'s homograph), pesach FALSE (the eldest brother\'s firstborn); persons_poor_court edges %d; edges on file %d' % (len(e4), len(d4['edges'])))
