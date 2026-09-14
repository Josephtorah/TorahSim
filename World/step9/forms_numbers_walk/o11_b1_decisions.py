# O11 batch B1 — THE INK LAYER (Minchat Shai + Onkelos rows), decided 2026-09-08 by reading scratchpad o11_b1_p1..p4.txt whole.
import re
BATCH = 'B1'

MS = 'ink (the written form — the Masorah\'s note)'
ONK = 'ink (the received translation\'s rendering)'

def DEFAULT(uid, c):
    s = c.get('source', '')
    text = c.get('claim_en', '')
    if s.startswith('Minchat Shai'):
        return MS
    if s.startswith('Onkelos'):
        m = re.search(r'(cold_run_\w+\.py)', text)
        if m:
            return 'ink (the compiled run — %s; the answer sheet\'s rows as test data)' % m.group(1)
        return ONK
    return None

def _run(text_id_to_runner):
    return text_id_to_runner

# the lev_ Onkelos rows are Sifra bundles (source "Onkelos Lev N; Sifra ..."): deferred to B5, read in the Leviticus context
DEFER = {'LV06-11', 'LV06-14', 'LV07A-06', 'LV07C-05', 'LV07C-07', 'LV07B-05', 'LV07B-06', 'LV07B-07', 'LV07B-09',
         'LV08-01', 'LV08-02', 'LV08-06', 'LV08-07', 'LV08-08', 'LV18-05'}

EXCEPTIONS = {
    # the one Masorah-pair row whose CONCLUSION is the Kitzur's analogy (as there, so here) and the law derived from it
    'EX09-03': "E7 (the equal decree on the Masorah's he/alef pair — the Kitzur's as-there-so-here reading, the repeat-offender rule; the written form beside)",
    # the case shelf's readings carried on an Onkelos row (law spans; the particle forms)
    'EX25-03': "E1 (the 'so shall you make' clause read to include the later generations — the case shelf's standing rule; the translation beside)",
    'EX31-03': "E2 (the restrictive particle 'but' read as the labors' own boundary — the case shelf; the translation beside)",
    # the compiled-run rows whose headline IS a catalogued move (the run read back into the spec; the second seat's delta)
    'EX25-15': 'M-22 (the run read back into the spec — cold_run_sanctuary_build.py)',
    'EX28-15': 'M-22 (the run read back into the spec — cold_run_vestments.py)',
    'EX29-16': 'M-23 (the second seat\'s delta — cold_run_incense_shekel.py, Exod 29 against Lev 8)',
    'EX31-09': 'M-22 (the run read back into the spec — cold_run_erection.py, Exod 31:1-11 against 35:30-35)',
    'EX34-12': 'M-23 (the second seat\'s delta — cold_run_erection.py, Exod 34:18-26 against 23:12-19)',
    'EX35-08': 'M-22 (the run read back into the spec — cold_run_erection.py, Exod 35:4-29 against 25:1-9)',
    'EX37-07': 'M-22 (the run read back into the spec — cold_run_sanctuary_build.py, Exod 37 against 25)',
    'EX39-06': 'M-22 (the run read back into the spec — cold_run_vestments.py, Exod 39 against 28)',
    'EX40-08': 'M-22 (the run read back into the spec — cold_run_erection.py, Exod 40 against the whole spec)',
    # ink rows carrying a named rider (the rider noted, the written form leads)
    'EX07-03': "ink (the written form — the Masorah's note; Rabbenu Bachya's letter-value reading, E29, rides beside)",
    'EX08-04': "ink (the written form — the Masorah's note; the Kitzur's quail-rule pair, E7, rides beside)",
    'EX10-02': "ink (the written form — the Masorah's note; the Kitzur's letter-value cipher, E29, rides beside)",
    'EX12-16': "ink (the written form — the Masorah's letter-file; the Kitzur's letter-value quartet, E29, rides beside)",
    'EX13-12': "ink (the written form — the Masorah's letter-file; the Kitzur's ciphers, E29, named beside)",
    'EX14-01': "ink (the written form — the Masorah's note; the Mekhilta's revocalization, M-16, and the Kitzur's letter-value, E29, ride beside)",
    'EX18-13': "ink (the written form — the Masorah's note; the Kitzur's hard-matter pair, E7, rides beside)",
    'G07-01': "ink (the written form — the Masorah's note; its letter-count reason, E29, beside)",
    'G22-04': "ink (the written form — the Masorah's note; R. Yudan's exclusion reading, E2, rides beside)",
    'G39-02': "ink (the written form — the Masorah's note; the Kitzur's letter-value arithmetic, E29, rides beside)",
    'G46-15': "ink (the written form — the Masorah's mirror pair; the measure-for-measure reading, E27, rides beside)",
    'G54-01': "ink (the written form — the Masorah's pair; the Kitzur's one-rule reading, E7, rides beside)",
    'G55-12': "ink (the written form — the Masorah's note; the staff-word's letter-sum, E29, rides beside)",
    'G60-07': "ink (the written form — the Masorah's note; the measure-for-measure reading, E27, rides beside)",
    'EX32-03': "ink (the received translation's rendering; the breaking's recorded a-fortiori, E5, beside)",
    'EX33-02': "ink (the received translation's rendering; the excommunication a-fortiori, E5, rides beside)",
    'EX34-01': "ink (the received translation's rendering; the torn-contract parable, E26, beside)",
    'EX36-04': "ink (the received translation's rendering; the inclusion of the beasts, E1, rides beside)",
    'EX36-05': "ink (the received translation's rendering; the two mornings counted from the doubled word, E10, beside)",
}
