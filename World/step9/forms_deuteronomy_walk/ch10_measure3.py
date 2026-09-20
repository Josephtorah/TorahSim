import sys, io, re, contextlib, subprocess, collections
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import register_census as RC
    w = RC.running_world()
def L(eid): 
    e = w.entities.get(eid)
    for a in ('ledger', 'entries'):
        if hasattr(e, a): return list(getattr(e, a))
    return []
for eid in ('aaron', 'eleazar_son_of_aaron', 'the_levites', 'the_ark', 'israel_people', 'moses'):
    rows = L(eid)
    print('%s (%d): %s' % (eid, len(rows), [(r.get('effect'), r.get('op'), str(r.get('case_source', ''))[:14], r.get('open')) for r in rows][-40:]))
wr = [r for r in w.log if isinstance(r, (list, tuple)) and r[0] in ('WRITE', 'RETRO-WRITE')]
for pat in ('stranger|sojourn|convert|ger_', 'bribe', 'love', 'cleav', 'circumcis|foreskin', 'stiff|neck', 'buried|burial', 'fear_of', 'demand|ask', 'praise', 'stars|seventy', 'invested_office', 'blessed_by_the_priests|blessed_the_people'):
    hits = collections.Counter((r[2].get('effect'), r[2].get('subject')) for r in wr if re.search(pat, str(r[2].get('effect'))))
    print('  WRITE effects matching %-32r: %s' % (pat, dict(hits)))
print('  the entities with buried: %s' % sorted({r[2].get('subject') for r in wr if r[2].get('effect') == 'buried'}))
print('  the open debits on israel: %s' % [(r.get('effect'), r.get('case_source', '')[:12]) for r in L('israel_people') if r.get('op') == 'debit' and r.get('open')])
print('  counts: debits on israel %d, open %d' % (sum(1 for r in L('israel_people') if r.get('op') == 'debit'), sum(1 for r in L('israel_people') if r.get('op') == 'debit' and r.get('open'))))
