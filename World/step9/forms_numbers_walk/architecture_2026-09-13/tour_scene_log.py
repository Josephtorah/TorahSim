# THE TOUR (2026-09-13): print the refuge runner's scene log for one manslayer and the office-holder's death — the tour quotes the machine's own lines.
import sys, contextlib, io
sys.path.insert(0, '<repo-old>/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_refuge as R
w = R._W
want = {'the-exile-under-eleazar', 'eleazar'}
for kind, day, d in w.log:
    subj = d.get('subject')
    if subj in want or (kind == 'EVENT' and d.get('kind') == 'high_priest_died'):
        keys = {k: d.get(k) for k in ('kind', 'subject', 'effect', 'op', 'value', 'law', 'open', 'seq', 'entry_seq', 'note', 'counterparty', 'ask', 'priest') if d.get(k) is not None}
        print(kind, day, keys)
print('---- the manslayer ledger')
for e in w.entity('the-exile-under-eleazar').ledger:
    print({k: e.get(k) for k in ('effect', 'op', 'value', 'open', 'closed_by', 'day', 'seq', 'law', 'counterparty')})
print('---- day_in', w.clock.day_in('exodus', 40, 6, 1))
