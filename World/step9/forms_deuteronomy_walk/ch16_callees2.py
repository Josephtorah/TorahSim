import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b: the erection runner's cells by their QUESTION keys (the first callees print used the cells' names — 'no_case' every one); printed before any assert. RUN FROM THE REPO ROOT.
import sys, io, contextlib, subprocess
ROOT = _ROOT; sys.path.insert(0, ROOT + '/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_erection as ER
for q in ('empty_where_it_stands', 'empty_two_seats', 'chagigah_overnight', 'until_morning_forms', 'purge_before_slaughter', 'warranty_read', 'equinox', 'wheat_two_loaves', 'chagigah_older', 'appearance_amounts', 'pilgrimage_by_call', 'leaven_by_call', 'matzah_by_call'):
    c = ER.repeats(q); print('FACT ER.repeats(%s) = %r' % (q, (c['v'], c['p'], c['fx'], c['why'][:140])))
for q in ('sheet_az_3_5', 'sheet_az_4_2', 'demolition_grows', 'asherav_homograph', 'pillars_exod'):
    c = ER.covenant(q); print('FACT ER.covenant(%s) = %r' % (q, (c['v'], c['p'], c['fx'], c['why'][:140])))
print('CALLEES2 DONE')
