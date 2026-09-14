#!/usr/bin/env python3
# THE NUMBERS WALK 11b — THE CORPUS-WIDE DIFF: the parser 10b left (cold_run_sequence.pre_midian.py's INK block) against the parser after rule (28)
# THE RATIO "one of the N", over EVERY verse of the whole Tanakh (the class's seats lie in Ecclesiastes, Ezekiel, Nehemiah and Job) — numbers AND
# ordinals. Every moved verse printed with both readings, to be read verse by verse. PREDICTED at the design: exactly EIGHT verses move (the probes').
import re, sqlite3, sys, os
sys.path.insert(0, '<repo-old>/World/step9')
import world_engine as WE
def ink(path):
    src = open(path, encoding='utf-8').read().split('# ==== INK BEGIN')[1].split('# ==== INK END ====')[0].split('\n', 1)[1]
    G = {'re': re, 'sqlite3': sqlite3, 'os': os, 'WE': WE}; exec(src, G); return G
OLD = ink('<scratch>/cold_run_sequence.pre_midian.py')
NEW = ink('<repo-old>/World/step9/cold_run_sequence.py')
db = sqlite3.connect('file:<repo-old>/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
verses = db.execute("SELECT book, chapter, verse FROM verses ORDER BY id").fetchall()
moved = []
for b, c, v in verses:
    wo, wn = OLD['verse_words'](b, c, v), NEW['verse_words'](b, c, v)
    no, nn = OLD['ink_numbers'](wo), NEW['ink_numbers'](wn)
    oo, on = OLD['ink_ordinals'](wo), NEW['ink_ordinals'](wn)
    if no != nn or oo != on or wo != wn:
        moved.append((b, c, v, no, nn, oo, on, ' '.join(w for w in wn if w.endswith(('|', '*', '%')) or '/' in w)))
print('verses scanned %d; MOVED %d (predicted 8)' % (len(verses), len(moved)))
for b, c, v, no, nn, oo, on, ws in moved:
    print('  %s %d:%d  numbers %s -> %s%s   [%s]' % (b, c, v, [str(x) for x in no], [str(x) for x in nn], ('  ordinals %s -> %s' % (oo, on)) if oo != on else '', ws))
