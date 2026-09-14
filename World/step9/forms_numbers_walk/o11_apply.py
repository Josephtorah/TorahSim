#!/usr/bin/env python3
"""o11_apply.py — write the decided middah labels into the claims manifests (byte-faithful dump), print the census.
Usage: python3 o11_apply.py <decisions.py>   (the decisions module defines BATCH, DEFAULT(uid, claim) -> label|None, EXCEPTIONS {id: label}, DEFER {ids})
"""
import glob, json, os, sys, importlib.util, collections, re

MAN = '<repo-old>/logic/oral_audit/manifests'
CODE = re.compile(r'^(ink|plain|H|I(?:[1-9]|1[0-3])|E(?:[1-9]|[12][0-9]|3[0-2])|M-\d{2})(?:\s*\(.*\))?\s*$', re.S)

def load(path):
    spec = importlib.util.spec_from_file_location('dec', path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

# THE MANIFESTS' FOUR SHAPES (measured 2026-09-08 over all 166): indent 1 / ensure_ascii False / no tail newline (122 + exo_16);
# indent 2 / False (24); indent 1 / ensure_ascii True (16); the three law-era files one compact row per line, '[\n' ... '\n]\n'.
VARIANTS = [(1, False), (2, False), (1, True), (2, True), (4, False), (4, True)]

def dump_as(rows, shape):
    if shape[0] == 'rows':
        return '[\n' + ',\n'.join(json.dumps(r, ensure_ascii=shape[1], separators=(',', ':')) for r in rows) + '\n]\n'
    ind, ea, nl = shape
    return json.dumps(rows, indent=ind, ensure_ascii=ea) + nl

def detect(raw, rows):
    for ind, ea in VARIANTS:
        for nl in ('', '\n'):
            if dump_as(rows, (ind, ea, nl)) == raw: return (ind, ea, nl)
    for ea in (False, True):
        if dump_as(rows, ('rows', ea)) == raw: return ('rows', ea)
    return None

def main(decpath):
    d = load(decpath)
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from o11_print import select
    written = 0; touched = 0; skipped_labeled = 0; deferred = 0; bycode = collections.Counter(); exc_used = set(); unfaithful = []
    for fpath in sorted(glob.glob(os.path.join(MAN, '*_claims.json'))):
        uid = os.path.basename(fpath)[:-len('_claims.json')]
        raw = open(fpath, encoding='utf-8').read()
        rows = json.loads(raw)
        shape = detect(raw, rows)
        if shape is None:
            unfaithful.append(uid); continue
        changed = False
        for c in rows:
            if not select(d.BATCH, uid, c): continue
            if c['id'] in d.DEFER: deferred += 1; continue
            relabel = getattr(d, 'RELABEL', {})
            if str(c.get('middah') or '').strip() and c['id'] not in relabel: skipped_labeled += 1; continue
            lab = relabel.get(c['id']) or d.EXCEPTIONS.get(c['id'])
            if lab: exc_used.add(c['id'])
            else: lab = d.DEFAULT(uid, c)
            if lab is None: continue
            assert CODE.match(lab), (c['id'], lab)
            c['middah'] = lab; changed = True; written += 1; bycode[CODE.match(lab).group(1)] += 1
        if changed:
            open(fpath, 'w', encoding='utf-8').write(dump_as(rows, shape)); touched += 1
    unused = set(d.EXCEPTIONS) - exc_used
    print('%s: labels written %d in %d manifests; deferred %d; already labeled %d; by code %s' % (d.BATCH, written, touched, deferred, skipped_labeled, dict(bycode)))
    print('exceptions used %d / %d%s' % (len(exc_used), len(d.EXCEPTIONS), ('; UNUSED: ' + ', '.join(sorted(unused))) if unused else ''))
    if unfaithful: print('UNFAITHFUL DUMP — NOT WRITTEN:', unfaithful)

if __name__ == '__main__':
    main(sys.argv[1])
