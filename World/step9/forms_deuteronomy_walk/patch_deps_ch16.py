import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b (LEAN): THE TWO DEMANDS OF THE DEPENDENCY GATE FILED FROM ITS PRINT (ch16b_dependency_first.out — read before this was typed):
# (1) EDGE festivals_judges -> priesthood [widow] at Deut 16:11, 16:14 — FALSE: the household list's widow (the pilgrim's guests — 'the sojourner, the fatherless and
# the widow'), not Leviticus 21's widow of the priest's marriage class (the token's home) — a homograph of the type census; (2) POINTER Deut 16:10 AS_WHEN 'as He
# blesses you' — PARAMETER: the hand's measure a quantity (Mishnah Chagigah 1:5 — the design's own prediction), not a procedure. Idempotent; the file asserted to load. RUN FROM THE REPO ROOT.
import subprocess, yaml
ROOT = _ROOT
P = ROOT + '/World/step9/dependency_dispositions.yaml'
s = open(P, encoding='utf-8').read()
W = 'THE DEUTERONOMY WALK 14b (2026-09-23; LEAN) | '
if '{from: festivals_judges, to: priesthood, disposition: FALSE' not in s:
    edge = "  - {from: festivals_judges, to: priesthood, disposition: FALSE, link: none,\n     why: \"%sthe type census's 'widow' at Deut 16:11 and 16:14 is the HOUSEHOLD LIST's widow — 'the Levite in your gates, the sojourner, the fatherless and the widow' the pilgrim's guests at the feast (the four against the four, the Sifrei 138:4-6; 12:18's list the twin) — NOT Leviticus 21:14's widow of the priest's marriage class (the token's home runner priesthood): a homograph of the census; the widow's own laws ahead (24:17-21 — the sojourner, the fatherless and the widow's gleanings, 281:1 read whole at the reading) at their sittings; no call, no procedure\"}\n"
    a = "  - {from: festivals_judges, to: pesach_sheni, disposition: CALL, link: reference, carries: verdict,"
    i = s.index(a); j = s.index('\n', s.index('why:', i)) + 1
    s = s[:j] + edge + s[j:]
if 'verse: "Deut 16:10", form: AS_WHEN, runner: festivals_judges' not in s:
    ptr = "  - {verse: \"Deut 16:10\", form: AS_WHEN, runner: festivals_judges, disposition: PARAMETER, link: reference, why: \"%s'with the measure of the freewill offering of your hand which you shall give, AS THE LORD YOUR GOD BLESSES YOU' (the gate's own print) — the hand's MEASURE a quantity set at the case, not a pointer to a procedure: Mishnah Chagigah 1:5's four cases (the exam row read whole — many eaters and little property, much property and few eaters, both few, both many) THE PARAMETER the_gift_of_the_hand in the runner's DATA; the Sifrei 137:3 (the tithe admitted for the surplus); the design's own prediction ('the pointer census at 16:10 PARAMETER if demanded')\"}\n" % W
    s = s.rstrip('\n') + '\n' + ptr
open(P, 'w', encoding='utf-8').write(s)
d = yaml.safe_load(open(P, encoding='utf-8'))
assert any(e.get('from') == 'festivals_judges' and e.get('to') == 'priesthood' and e.get('disposition') == 'FALSE' for e in d['edges']) and any(p.get('verse') == 'Deut 16:10' and p.get('runner') == 'festivals_judges' and p.get('disposition') == 'PARAMETER' for p in d['pointers'])
print('filed: the FALSE edge to priesthood (the household list\'s widow) and the PARAMETER pointer at Deut 16:10 (the hand\'s measure); edges %d, pointers %d' % (len(d['edges']), len(d['pointers'])))
