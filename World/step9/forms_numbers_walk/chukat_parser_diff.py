#!/usr/bin/env python3
# THE NUMBERS WALK 5b — THE CORPUS-WIDE DIFF: the parser 4b left (cold_run_sequence.pre_chukat.py's INK block) against the parser after
# the Chukat rules (19) the dual "twice" and (20) the definite numeral after the year-construct as an ordinal year (the ordinals diffed
# too), over EVERY verse of the five books — numbers AND ordinals. Every moved verse printed with both readings, to be read
# verse by verse (1b's lesson: the probes prove the span, the diff shows what else moved).
import re, sqlite3, sys, os
sys.path.insert(0, '<repo-old>/World/step9')
import world_engine as WE
def ink(path):
    src = open(path, encoding='utf-8').read().split('# ==== INK BEGIN')[1].split('# ==== INK END ====')[0].split('\n', 1)[1]
    G = {'re': re, 'sqlite3': sqlite3, 'os': os, 'WE': WE}; exec(src, G); return G
OLD = ink('<scratch>/cold_run_sequence.pre_chukat.py')
NEW = ink('<repo-old>/World/step9/cold_run_sequence.py')
db = sqlite3.connect('file:<repo-old>/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
verses = db.execute("SELECT book, chapter, verse FROM verses WHERE book IN ('Gen','Exod','Lev','Num','Deut') ORDER BY id").fetchall()
moved = []
for b, c, v in verses:
    wo, wn = OLD['verse_words'](b, c, v), NEW['verse_words'](b, c, v)
    no, nn = OLD['ink_numbers'](wo), NEW['ink_numbers'](wn)
    oo, on = OLD['ink_ordinals'](wo), NEW['ink_ordinals'](wn)
    if no != nn or oo != on:
        moved.append((b, c, v, no, nn, oo, on, ' '.join(w for w in wn if w.startswith('ה') or w.startswith('וה') or w.rstrip('*^|~#@%').endswith(('אחד', 'אחת', 'מאות', 'אלפים', 'מאתים', 'חמשים')))))
print('verses scanned %d; MOVED %d' % (len(verses), len(moved)))
for b, c, v, no, nn, oo, on, ws in moved:
    print('  %s %d:%d  numbers %s -> %s%s   [%s]' % (b, c, v, no, nn, ('  ordinals %s -> %s' % (oo, on)) if oo != on else '', ws))
