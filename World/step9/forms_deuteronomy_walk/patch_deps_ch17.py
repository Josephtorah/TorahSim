import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 15b (LEAN): THE FOUR DEMANDS OF THE DEPENDENCY GATE FILED FROM ITS PRINT (ch17b_dependency_first.out — read before this was typed):
# (1) EDGE courts_prophet -> family [inheritance] at Deut 18:1, 18:2 — FALSE: Levi's NO-inheritance is Numbers 18:20's (korach by CALL) and 10:9's (second_tablets by
# CALL), not the family engine's inheritance of the daughters (Numbers 27, 36) — a homograph of the type census; (2) courts_prophet -> refuge and (3) -> good_land
# dispositioned CALL but no live call — the runner READS THEIR DATA ROWS (the one witness by the prototype, the court of twenty-three; the king's law tokens, the heart
# lifted): PARAMETER carries value (13b's mishpatim precedent); (4) POINTER Deut 18:2 AS_WHEN 'as He spoke to him' — RUN_CITATION of Numbers 18:20's line
# portion_declared (10:9's precedent, the receipt's third form). Idempotent; the file asserted to load. patch_deps_ch16.py's form. RUN FROM THE REPO ROOT.
import subprocess, yaml
ROOT = _ROOT
P = ROOT + '/World/step9/dependency_dispositions.yaml'
s = open(P, encoding='utf-8').read()
W = 'THE DEUTERONOMY WALK 15b (2026-09-24; LEAN) | '
for to, extra in (('refuge', "PARAMETER (the gate's print: no live call — the DATA rows read: the_one_witness 'two_by_the_prototype', the_court_of_twenty_three, the_presence_rows; a datum, not a procedure — 13b's mishpatim precedent) | "), ('good_land', "PARAMETER (the gate's print: no live call — the DATA rows read: the_kings_law_tokens (8:13's silver and gold, 8:14's heart lifted — the runner's own row names 17:17 and 17:20 as owed forward), the_heart_lifted; a datum, not a procedure) | ")):
    W0 = 'THE DEUTERONOMY WALK 15b (2026-09-24) | '   # the edges' own prefix as add_types_ch17_b.py wrote it (read at the grep — the first typing guessed the note's form)
    old = "  - {from: courts_prophet, to: %s, disposition: CALL, link: reference, carries: verdict,\n     why: \"%s" % (to, W0)
    if s.count(old) == 1:
        s = s.replace(old, "  - {from: courts_prophet, to: %s, disposition: PARAMETER, link: reference, carries: value,\n     why: \"%s%s" % (to, W0, extra))
    else:
        assert "  - {from: courts_prophet, to: %s, disposition: PARAMETER" % to in s, to
if '{from: courts_prophet, to: family, disposition: FALSE' not in s:
    edge = "  - {from: courts_prophet, to: family, disposition: FALSE, link: none,\n     why: \"%sthe type census's 'inheritance' at Deut 18:1 and 18:2 is LEVI'S NO-INHERITANCE — 'the priests the Levites, all the tribe of Levi, shall have no portion or inheritance with Israel … the LORD is his inheritance' (Numbers 18:20's line by CALL to korach, 10:9's twin by CALL to second_tablets; the Sifrei 163:2-3 the spoil and the land, 164:1-2 the three and the five) — NOT the family engine's inheritance of the daughters and the tribes (Numbers 27:1-11, 36:1-12 — the token's home runner family): a homograph of the census; no call, no procedure\"}\n" % W
    a = "  - {from: courts_prophet, to: pre_sinai, disposition: CALL, link: reference, carries: verdict,"
    i = s.index(a); j = s.index('\n', s.index('why:', i)) + 1
    s = s[:j] + edge + s[j:]
if 'verse: "Deut 18:2", form: AS_WHEN, runner: courts_prophet' not in s:
    ptr = "  - {verse: \"Deut 18:2\", form: AS_WHEN, runner: courts_prophet, disposition: RUN_CITATION, link: reference, why: \"%s'the LORD is his inheritance, AS HE SPOKE TO HIM' (the gate's own print) — A RECEIPT BEHIND: the run citation of Numbers 18:20's line portion_declared (inheritance_barred on aaron and the_levites the tape's entries, never rewritten) and 10:9's twin ('as the LORD your God spoke to him' — the one seat of the full form; second_tablets' receipt's third form by CALL); the Sifrei 164:3 'to tell what caused it'; the readback row 18:2 VERBATIM in kind with tape_kind portion_declared at Num 18:20; no pointer ahead\"}\n" % W
    s = s.rstrip('\n') + '\n' + ptr
open(P, 'w', encoding='utf-8').write(s)
d = yaml.safe_load(open(P, encoding='utf-8'))
E = {(e['from'], e['to']): e for e in d['edges'] if e.get('from') == 'courts_prophet'}
assert E[('courts_prophet', 'refuge')]['disposition'] == 'PARAMETER' and E[('courts_prophet', 'good_land')]['disposition'] == 'PARAMETER' and E[('courts_prophet', 'family')]['disposition'] in ('FALSE', False) and any(p.get('verse') == 'Deut 18:2' and p.get('runner') == 'courts_prophet' and p.get('disposition') == 'RUN_CITATION' for p in d['pointers']), 'the four filed'
print('filed: refuge and good_land -> PARAMETER carries value; family FALSE (the census\'s homograph); the pointer Deut 18:2 RUN_CITATION; edges from courts_prophet %d; edges %d, pointers %d' % (len(E), len(d['edges']), len(d['pointers'])))
