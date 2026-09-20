import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# 9b RUN B, the chain's first pass (2026-09-20): (1) Q30's return — the retype's comment swallowed the tuple's second element ('got …' — TypeError at the probe);
# the comment moved to the line's end. (2) THE DEPENDENCY GATE'S THREE DEMANDS: the FALSE edge at 11:3 (the king-word's homograph of Molech — 5b's lesson),
# the sequential run's registration edge (8b's form), the AS_WHEN pointer at 11:25 (RUN_CITATION — the design's prediction, the census's demand).
import subprocess, yaml
ROOT = _ROOT
P = f'{ROOT}/World/step9/readback_probes.py'; s = open(P, encoding='utf-8').read()
lines = s.split('\n'); i = [k for k, l in enumerate(lines) if l.startswith('    return got == ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1), [')]; assert len(i) == 1, i; i = i[0]
l = lines[i]; c = l.index('   # the vocabulary'); head, rest = l[:c], l[c:]; j = rest.index(", 'got ("); comment, tail = rest[:j], rest[j:]
assert tail.endswith('% (got,)') and "'got (" in tail, tail[-40:]
lines[i] = head + tail + comment; open(P, 'w', encoding='utf-8').write('\n'.join(lines)); print('Q30 fixed:', lines[i][:80], '…', lines[i][-60:])
import ast; ast.parse(open(P, encoding='utf-8').read()); print('  readback_probes.py parses')
D = f'{ROOT}/World/step9/dependency_dispositions.yaml'; d = open(D, encoding='utf-8').read()
SEQ = ('  - {from: sequence, to: blessing_and_curse, disposition: CALL, link: none,\n'
       '     why: "THE DEUTERONOMY WALK 9b (2026-09-20) | the sequential run\'s REGISTRATION edge — (\'cold_run_blessing_and_curse\', \'law_blessing_and_curse\') in DAEMON_ORDER (the runner compiles no verse: link none, O4\'s license); TWO OWN-DAY lines this sitting after the tape\'s last Deuteronomy 10 line, NO marker — second_paragraph_declared (11:13-21; rain_in_its_season and heavens_shut_for_turning conditional HEAVEN entries, yoke_of_the_commandments_accepted a STATUS — Mishnah Berakhot 2:2\'s name) and blessing_and_curse_set (11:26-32; blessing_and_curse_set a STATUS, gerizim_ebal_ceremony_owed a DEBIT toward Heaven OPEN to Joshua 8:30-35) — STATUTE by form, page_order, the counter\'s day (40, 11, 1) re-asserted; the daemon\'s five writes on its own lines — THE REST drops them, no declared delta; DC1-DC9 the checkpoints"}\n')
FALSE = ('  - {from: blessing_and_curse, to: sanctions, disposition: FALSE, link: none,\n'
         '     why: "THE DEUTERONOMY WALK 9b (2026-09-20) | 11:3\'s \'His signs and His deeds which He did in the midst of Egypt to Pharaoh KING of Egypt\' — the token census matches the king-word (the lemma 4428, \'king\') to the sanctions span\'s Molech (Leviticus 20:2-5 — the lemma 4432, the same consonants): A HOMOGRAPH, named (5b\'s 7:8 the same title; the standing lesson: name homographs, never count them); the verse the discipline retold — plague_struck on the tape by kind (the readback row 11:3 VARIANT), Pharaoh\'s title at its one seat in the chapter; no call; the census\'s three demands this sitting — this edge, the sequential run\'s registration edge, the pointer at 11:25; the design\'s fourteen CALL edges the census\'s own"}\n')
PTR = ('  - {verse: "Deut 11:25", form: AS_WHEN, runner: blessing_and_curse, disposition: RUN_CITATION, link: reference, why: "THE DEUTERONOMY WALK 9b (2026-09-20) | \'no man shall be able to stand before you; the dread of you and the fear of you the LORD your God will put on the face of all the land you tread, AS HE SPOKE TO YOU\' (כַּאֲשֶׁר דִּבֶּר לָכֶם — as He spoke to you; 1:11 and Joshua 23:10 the form\'s other two seats, the Name absent — THE RECEIPT\'S FOURTH SHAPE beside 10:9\'s third): a RUN CITATION of Exodus 23:27\'s \'I will send My terror before you … and I will make all your enemies turn their backs to you\' — ordinances.land(\'angel\', \'hornet\', \'little_by_little\') by CALL (Exodus 23:20-33 has no line by verse; the cell the reference), with 7:23-24\'s \'no man shall stand before you\' (seven_nations.do_not_fear by CALL) and Joshua 1:5 the run\'s receipt; NAMED BY TWO TEACHERS — the Sifrei Devarim 52:4 and Tosefta Sotah 8:6 (the readback row 11:25 VARIANT, pointer=); the register gate lists no seat (its finder scans \'commanded\' — the third and fourth shapes owed to a gate sitting); no debit paid; the design\'s prediction, the census\'s own demand (a sixth time)"}\n')
A1 = '  - {from: blessing_and_curse, to: hear_o_israel, disposition: CALL, link: reference, carries: verdict,\n'; assert d.count(A1) == 1
d = d.replace(A1, SEQ + A1)
k = d.index('  - {from: blessing_and_curse, to: primeval, disposition: CALL'); e = d.index('\n', d.index('\n', k) + 1) + 1   # the entry and its why line
assert d[e:].startswith('  - {') or d[e:].startswith('\n') or d[e:].startswith('#'), repr(d[e:e+40])
d = d[:e] + FALSE + d[e:]
A3 = '  - {verse: "Deut 10:9", form: AS_WHEN, runner: second_tablets, disposition: RUN_CITATION'; k = d.index(A3); e = d.index('\n', k) + 1
d = d[:e] + PTR + d[e:]
open(D, 'w', encoding='utf-8').write(d); y = yaml.safe_load(open(D, encoding='utf-8')); print('dispositions: yaml loads; sections', list(y)[:6] if isinstance(y, dict) else type(y))
