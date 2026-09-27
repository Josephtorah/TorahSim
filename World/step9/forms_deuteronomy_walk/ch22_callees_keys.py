import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK 17b: the dispatch keys of the kin cells whose asks the regex did not find — every quoted key in the cell's source, its signature and its first
# lines printed (read-only) so the callees' asks are typed from the source, never guessed. RUN FROM THE REPO ROOT.
import sys, io, re, contextlib, subprocess, inspect
ROOT = _ROOT; sys.path.insert(0, ROOT + '/World/step9')
def load(name):
    with contextlib.redirect_stdout(io.StringIO()):
        return __import__('cold_run_' + name)
CELLS = [('ordinances', 'courts'), ('ordinances', 'loan'), ('ordinances', 'stranger'), ('ordinances', 'gifts'), ('holiness', 'gifts'), ('holiness', 'wage'), ('holiness', 'conduct'), ('holiness_b', 'mixtures'), ('holiness_b', 'maidservant'), ('yovel', 'interest'), ('yovel', 'interest_scope'), ('yovel', 'support_duty'), ('sanctions', 'grade'), ('sanctions', 'levirate'), ('sanctions', 'cowives'), ('sanctions', 'unions_misc'), ('sanctions', 'frame'), ('sanctions', 'blood'), ('sanctions', 'census'), ('sanctions', 'curser'), ('priesthood', 'family'), ('priesthood', 'acceptable'), ('priesthood', 'holy_food'), ('family', 'levirate'), ('family', 'commission'), ('family', 'purchase'), ('family', 'inheritance'), ('mishpatim_2', 'grade'), ('mishpatim', 'grade'), ('mishpatim_3', 'cell'), ('exodus_story', 'amalek'), ('balak', 'the_call'), ('joseph', 'dinah'), ('joseph', 'potiphar'), ('primeval', 'hagar'), ('primeval', 'separation'), ('negaim', 'law_negaim'), ('metzora', 'law_metzora'), ('naso', 'camp_purity'), ('hear_o_israel', 'rb'), ('mekoshesh', 'out')]
for n, c in CELLS:
    try:
        m = load(n); fn = getattr(m, c); src = inspect.getsource(fn)
        keys = []
        for k in re.findall(r"""['"]([a-z][a-z_0-9]{2,})['"]\s*:""", src):
            if k not in keys: keys.append(k)
        print('%s.%s %s | %d lines | keys %s\n   HEAD: %s' % (n, c, inspect.signature(fn), src.count('\n'), keys[:60], re.sub(r'\s+', ' ', src[:420])))
    except Exception as ex:
        print('FAIL %s.%s: %r' % (n, c, ex))
