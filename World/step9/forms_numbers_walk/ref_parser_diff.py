#!/usr/bin/env python3
# THE NUMBERS WALK 15b — THE CORPUS-WIDE DIFF: the parser 14b left (cold_run_sequence_OLD_before_rule29.py's INK block) against the parser after
# rule (29) THE BARE DUAL THOUSAND, over EVERY verse of the whole Tanakh — numbers AND ordinals AND the marked tokens. Every moved verse printed with
# both readings, to be read verse by verse. PREDICTED at the design: exactly NINE verses move (the eight bare dual seats and Psalm 8:8), none a marker;
# the twenty-one compound dual seats gain the mark but keep their numbers (printed apart, not counted as moved numbers). midian_parser_diff.py's form.
import re, sqlite3, sys, os
sys.path.insert(0, '<repo-old>/World/step9')
import world_engine as WE
def ink(path):
    src = open(path, encoding='utf-8').read().split('# ==== INK BEGIN')[1].split('# ==== INK END ====')[0].split('\n', 1)[1]
    G = {'re': re, 'sqlite3': sqlite3, 'os': os, 'WE': WE}; exec(src, G); return G
OLD = ink('<scratch>/cold_run_sequence_OLD_before_rule29.py')
NEW = ink('<repo-old>/World/step9/cold_run_sequence.py')
db = sqlite3.connect('file:<repo-old>/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
verses = db.execute("SELECT book, chapter, verse FROM verses ORDER BY id").fetchall()
moved, marked_only = [], []
for b, c, v in verses:
    wo, wn = OLD['verse_words'](b, c, v), NEW['verse_words'](b, c, v)
    no, nn = OLD['ink_numbers'](wo), NEW['ink_numbers'](wn)
    oo, on = OLD['ink_ordinals'](wo), NEW['ink_ordinals'](wn)
    if no != nn or oo != on:
        moved.append((b, c, v, no, nn, oo, on, ' '.join(w for w in wn if w.endswith(('|', '*', '%', '~', '@')) or '/' in w)))
    elif wo != wn:
        marked_only.append((b, c, v, [w for w in wn if w.endswith('~')], nn))
print('verses scanned %d; MOVED (a number or an ordinal changed) %d (predicted 9); MARKED ONLY (the dual mark on, the numbers unmoved) %d (predicted 20: the twenty-one compound seats less none — every one printed below)' % (len(verses), len(moved), len(marked_only)))
for b, c, v, no, nn, oo, on, ws in moved:
    print('  MOVED %s %d:%d  numbers %s -> %s%s   [%s]' % (b, c, v, [str(x) for x in no], [str(x) for x in nn], ('  ordinals %s -> %s' % (oo, on)) if oo != on else '', ws))
for b, c, v, ws, nn in marked_only:
    print('  MARKED %s %d:%d  %s  numbers %s' % (b, c, v, ws, nn))
