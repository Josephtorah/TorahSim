import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 12b THE TAIL (2026-09-22): the dependency gate's TWO DEMANDS from the chain's first pass (gates_ch14b/dependency.out), filed —
# (1) THE LIVE REGISTRATION EDGE sequence -> food_tithe (link none, 11b's form — the design's 'the registration edge at the tail if the census asks'); (2) a
# HOMOGRAPH filed FALSE with its why: the token census matched 'portion and INHERITANCE' at 14:27 and 14:29 (ונחלה) to the family runner's inheritance LAW (Numbers
# 27's daughters — the transfer of land between heirs): here the noun is THE LEVITE'S LAND PORTION (Numbers 18:20-24 — korach.the_tithe('no_inheritance') by CALL;
# 10:9 — second_tablets.the_levites_separated by CALL), not an heir's share — 7b's precedent (not_righteousness -> family at 9:26, 9:29 filed FALSE); no pointer
# demanded (none predicted), the registry's homographs not matched. Idempotent. patch_tail_ch13b.py's form. RUN FROM THE REPO ROOT.
import subprocess, yaml
ROOT = _ROOT
P = ROOT + '/World/step9/dependency_dispositions.yaml'
s = open(P, encoding='utf-8').read()
W = 'THE DEUTERONOMY WALK 12b (2026-09-22) | '
if 'from: sequence, to: food_tithe,' not in s:
    a = "  - {from: sequence, to: seducers, disposition: CALL, link: none,"
    i = s.index(a); j = s.index('\n', s.index('why:', i)) + 1
    reg = "  - {from: sequence, to: food_tithe, disposition: CALL, link: none,\n     why: \"%sthe sequential run's REGISTRATION edge — ('cold_run_food_tithe', 'law_food_tithe') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license); FIVE OWN-DAY lines this sitting after the tape's last Deuteronomy 13 line, NO marker — sons_and_mourning_declared (14:1-2; cuttings_for_the_dead_barred a BLOCK), food_law_declared (14:3-20; abomination_eating_barred a BLOCK over the twin chapter's classifier by CALL), carcass_and_kid_declared (14:21; carcass_eating_barred a BLOCK — the seat the sanctions engine names), second_tithe_declared (14:22-27; second_tithe_owed a STATUS; rejoicing_before_the_lord_commanded and levite_forsaking_barred REUSED — second entries), third_year_tithe_declared (14:28-29; poor_tithe_owed a STATUS); the daemon's seven writes on Israel — five new, two reuses; the tape 10/10 on its first run (DF1-DF9); demanded by the dependency gate's first pass at the tail (the design's own note)\"}\n" % W
    s = s[:j] + reg + s[j:]
if 'from: food_tithe, to: family, disposition: FALSE' not in s:
    a = "  - {from: not_righteousness, to: family, disposition: FALSE, link: none,"
    i = s.index(a); j = s.index('\n', s.index('why:', i)) + 1
    fal = "  - {from: food_tithe, to: family, disposition: FALSE, link: none,\n     why: \"%sthe token census matched 'he has no portion or INHERITANCE with you' (14:27, 14:29 ונחלה — and inheritance) to the family runner's inheritance law (Numbers 27's daughters, Genesis 48-49's testament — the transfer of land between heirs): here the noun names THE LEVITE'S LAND PORTION — 'in their land you shall not inherit, and you shall have no portion among them' (Numbers 18:20-24 — korach.the_tithe('no_inheritance') by CALL; 10:9 'Levi has no portion or inheritance with his brothers' — second_tablets.the_levites_separated by CALL; 12:12; 18:1-2 ahead), the ladder of four the runner's own row (F6 the_levites_ladder), not an heir's share — no cell of the family runner compiles 14:27 or 14:29; filed FALSE with its why (7b's precedent: not_righteousness -> family at 9:26, 9:29)\"}\n" % W
    s = s[:j] + fal + s[j:]
open(P, 'w', encoding='utf-8').write(s)
d = yaml.safe_load(open(P, encoding='utf-8'))
reg_n = sum(1 for e in d['edges'] if e['from'] == 'sequence' and e['to'] == 'food_tithe'); fal_n = sum(1 for e in d['edges'] if e['from'] == 'food_tithe' and e['to'] == 'family' and e['disposition'] in ('FALSE', False))   # YAML reads the bare FALSE as a boolean (the first run's assert)
assert reg_n == 1 and fal_n == 1, (reg_n, fal_n)
print('filed: the registration edge sequence -> food_tithe (link none) and the FALSE edge food_tithe -> family (the Levite\'s land portion, not the heirs\' law); edges %d; from food_tithe %d' % (len(d['edges']), sum(1 for e in d['edges'] if e['from'] == 'food_tithe')))
