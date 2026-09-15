import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK 5b: every CELL the docket names must exist as an ask in the runner (the docket's rows are answered by the cells)
import re
D = open((_ROOT + '/logic/oral_triage/num_16_18_korach_exam_2026-09-10.md'), encoding='utf-8').read()
R = open((_ROOT + '/World/step9/cold_run_korach.py'), encoding='utf-8').read()
named = sorted(set(re.findall(r"CELL (rebellion|plague_and_staffs|the_watch|the_gifts|the_tithe)\('([a-z_]+)'\)", D)))
asks = set(re.findall(r"if ask == '([a-z_]+)'", R))
missing = [(f, a) for f, a in named if a not in asks]
print('cells named in the docket:', len(named), '| asks in the runner:', len(asks), '| MISSING:', missing)
