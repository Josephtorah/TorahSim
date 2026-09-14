#!/usr/bin/env python3
# THE LOOP step 3 (2026-09-09): the 43 daemon rows — given_at BY SCRIPT from dependency_dispositions.yaml's spans (the first verse
# of the wrapped runner's first span; the library's five from the function each wraps), installed_by BY HAND from the design
# section's table (THE_LOOP.md "Step 3 INSTALLATION — the design"). Inserts the two lines after each daemon's `wraps:` line,
# preserving every comment; idempotent; verifies by yaml load and re-sums the count by value to 43 before writing.
import re, sys, yaml
ROOT = '<repo-old>/World/step9'
DEP = yaml.safe_load(open(ROOT + '/dependency_dispositions.yaml', encoding='utf-8'))['spans']
DAE = ROOT + '/daemon_dispositions.yaml'
text = open(DAE, encoding='utf-8').read()
decl = yaml.safe_load(text)['daemons']

LIB = {'law_slave_term': 'Exod 21:2', 'law_goring_ox': 'Exod 21:28', 'law_guardians': 'Exod 22:6', 'law_deposit_oath': 'Lev 5:20',
       'law_installation': 'Lev 8:1', 'law_sabbath': 'Exod 31:12'}   # the tabernacle's Sabbath clause (31:12-17 + 35:1-3), not the file's first span (the investiture's 29:1)
BY = {}
for n in ['law_pre_sinai', 'law_primeval', 'law_mamre', 'law_joseph', 'law_family', 'law_exodus_story', 'law_erection']:
    BY[n] = 'boot'
for n in ['law_slave_term', 'law_goring_ox', 'law_guardians', 'law_decalogue', 'law_ordinances', 'law_mishpatim', 'law_mishpatim_2',
          'law_mishpatim_3', 'law_calendar', 'law_sabbath', 'law_sanctuary_build', 'law_vestments', 'law_tochacha']:
    BY[n] = 'covenant_blood_thrown'
for n in ['law_installation', 'law_investiture', 'law_eighth_day']:
    BY[n] = 'erected'
for n in ['law_deposit_oath', 'law_offerings', 'law_minchah', 'law_chatat', 'law_vayikra5', 'law_tzav', 'law_shemini', 'law_clocks',
          'law_negaim', 'law_metzora', 'law_yoma', 'law_sanctions', 'law_holiness', 'law_holiness_b', 'law_moadim', 'law_temurah']:
    BY[n] = 'called_from_the_tent'
BY['law_priesthood'] = 'milluim_blood_sprinkled'
BY['law_yovel'] = 'entered_the_land'
BY['law_pesach'] = 'pending'
BY['law_lev24'] = 'pending'
WHY = {'law_pesach': "the Passover's giving at Exod 12:1-2 is not an EVENT on the tape — the stitcher carries Exod 12:2 as the epoch MARKER only, and the tape's Exodus 12 events begin at 12:29; the installing act registers when the Passover's own acts (12:3 the lamb taken, 12:28 'they did') join the tape",
       'law_lev24': "the blasphemer's law is CASE-BORN: its installing act is the tent's output at Lev 24:13, whose kind registers at Numbers' opening block with the four uncovered cases (THE_LOOP.md 'The tent as the run's interrupt')"}
ORDER = ['Gen', 'Exod', 'Lev', 'Num', 'Deut']

def given(name, d):
    if name in LIB:
        return LIB[name]
    wraps = (d.get('wraps') or '').split(' ')[0].split('.')[0]
    spans = DEP.get(wraps)
    assert spans, (name, wraps)
    b, c, v, _ = sorted(spans, key=lambda s: (ORDER.index(s[0]), s[1], s[2]))[0]
    return '%s %d:%d' % (b, c, v)

rows = {n: (given(n, d), BY[n]) for n, d in decl.items()}
assert set(rows) == set(BY), sorted(set(rows) ^ set(BY))
cnt = {}
for g, b in rows.values():
    cnt[b] = cnt.get(b, 0) + 1
print('by value:', dict(sorted(cnt.items(), key=lambda kv: -kv[1])), 'sum', sum(cnt.values()))
assert sum(cnt.values()) == 43 and cnt == {'boot': 7, 'covenant_blood_thrown': 13, 'erected': 3, 'called_from_the_tent': 16,
                                           'milluim_blood_sprinkled': 1, 'entered_the_land': 1, 'pending': 2}, cnt
for n, (g, b) in rows.items():
    print('  %-22s given_at %-11s installed_by %s' % (n, g, b))
if '--write' not in sys.argv:
    print('(dry run — pass --write)'); sys.exit(0)

out, cur, done = [], None, set()
for line in text.split('\n'):
    m = re.match(r'^  (law_[a-z_0-9]+):\s*(#.*)?$', line)   # a daemon key may carry a trailing comment (the three story daemons)
    if m:
        cur = m.group(1)
    out.append(line)
    if cur and cur not in done and re.match(r'^    wraps: ', line):
        g, b = rows[cur]
        if 'given_at' in decl[cur]:
            done.add(cur); continue
        out.append('    given_at: %s' % g)
        out.append('    installed_by: %s' % b)
        if b == 'pending':
            out.append('    why: "%s"' % WHY[cur].replace('"', "'"))
        done.add(cur)
assert done == set(rows), sorted(set(rows) - done)
open(DAE, 'w', encoding='utf-8').write('\n'.join(out))
after = yaml.safe_load(open(DAE, encoding='utf-8'))['daemons']
assert all('given_at' in d and 'installed_by' in d for d in after.values()) and len(after) == 43
assert all(after[n]['given_at'] == g and after[n]['installed_by'] == b for n, (g, b) in rows.items())
print('written: %d daemons carry both fields; comments preserved (%d lines -> %d)' % (len(after), text.count('\n'), '\n'.join(out).count('\n')))
