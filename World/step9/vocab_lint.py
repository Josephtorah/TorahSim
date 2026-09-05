#!/usr/bin/env python3
"""vocab_lint.py — the structural lint of World/step9/vocabulary.yaml
(sitting C of the audit, 2026-09-05). gloss_lint.py skips .yaml by
design (the vocabulary carries its glosses in a `gloss:` field, not
inline), so this file checks what that contract cannot:
  1. every value has a non-empty gloss;
  2. no gloss is a placeholder — a bare round label, 'exam query (date)',
     a quote-wrapped string, '—', '?', 'TODO';
  3. no Hebrew `he` is shared by more than FOUR values inside one
     dimension (round 44's signature: the docket TOPIC copied into every
     value's Hebrew — a false attribution);
  4. every non-empty `he` carries Hebrew letters, and no `gloss` carries
     Hebrew without English beside it.
Coverage is printed first (a report of zero is worth only the coverage
line above it). Exit 1 on any flag.
Run: python3 World/step9/vocab_lint.py
"""
import re, sys, os, collections, yaml
HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, 'vocabulary.yaml')
HEB = re.compile(r'[֐-׿]')
PLACEHOLDER = re.compile(r"^(round \d+|.* exam query \(2026-\d\d-\d\d\)|—|-|\?|TODO.*|\.\.\.)$")

def main():
    d = yaml.safe_load(open(PATH, encoding='utf-8'))
    values = []
    def walk(x, dim=None):
        if isinstance(x, dict):
            if 'dimension' in x:
                dim = x['dimension']
            if 'value' in x:
                values.append((dim, x))
            for v in x.values():
                walk(v, dim)
        elif isinstance(x, list):
            for v in x:
                walk(v, dim)
    walk(d)
    dims = len({dm for dm, _ in values})
    print('vocab_lint: %d values on %d dimensions scanned (%s)' % (len(values), dims, os.path.relpath(PATH)))
    flags = []
    by_dim_he = collections.defaultdict(collections.Counter)
    for dm, v in values:
        g = str(v.get('gloss', '') or '').strip()
        he = str(v.get('he', '') or '').strip()
        if not g:
            flags.append(('EMPTY-GLOSS', dm, v['value']))
        elif PLACEHOLDER.match(g) or (g.startswith("'") and g.endswith("'")):
            flags.append(('PLACEHOLDER', dm, v['value'], g[:60]))
        if he:
            if not HEB.search(he):
                flags.append(('HE-NOT-HEBREW', dm, v['value'], he[:40]))
            by_dim_he[dm][he] += 1
        if HEB.search(g) and not re.search(r'[A-Za-z]', g):
            flags.append(('GLOSS-HEBREW-ONLY', dm, v['value'], g[:60]))
    for dm, c in by_dim_he.items():
        for he, n in c.items():
            if n > 4:
                flags.append(('HE-SHARED-BY-%d' % n, dm, he[:40]))
    for f in flags:
        print('FLAG ', f)
    print('vocab_lint: %d flag(s)' % len(flags))
    return 1 if flags else 0

if __name__ == '__main__':
    sys.exit(main())
