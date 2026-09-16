#!/usr/bin/env python3
# THE DEUTERONOMY WALK 1b — THE CORPUS-WIDE DIFF: the parser 15b left (cold_run_sequence_OLD_before_rule30.py's INK block) against the parser after
# rule (30) THE HALF OF A NAMED WHOLE, over EVERY verse of the whole Tanakh — numbers AND ordinals AND the marked tokens. Every moved verse printed
# with both readings, to be read verse by verse. PREDICTED at the design: FOURTEEN Torah tokens in THIRTEEN verses move (Exod 12:29, 24:6 x2, 26:12,
# 27:5, Num 12:12, 31:42, 32:33, 34:13, 34:14, 34:15, Deut 3:12, 3:13, 29:7), one a marker row (Exod 12:29); some sixty verses outside. ref_parser_diff.py's form.
import re, sqlite3, sys, os, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SCR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT + '/World/step9')
import world_engine as WE
def ink(path):
    src = open(path, encoding='utf-8').read().split('# ==== INK BEGIN')[1].split('# ==== INK END ====')[0].split('\n', 1)[1]
    G = {'re': re, 'sqlite3': sqlite3, 'os': os, 'WE': WE, '_ROOT': ROOT}; exec(src, G); return G
OLD = ink(SCR + '/cold_run_sequence_OLD_before_rule30.py')
NEW = ink(ROOT + '/World/step9/cold_run_sequence.py')
db = sqlite3.connect('file:' + ROOT + '/Data/tanakh.sqlite?mode=ro', uri=True)
verses = db.execute("SELECT book, chapter, verse FROM verses ORDER BY id").fetchall()
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
moved, marked_only = [], []
for b, c, v in verses:
    wo, wn = OLD['verse_words'](b, c, v), NEW['verse_words'](b, c, v)
    no, nn = OLD['ink_numbers'](wo), NEW['ink_numbers'](wn)
    oo, on = OLD['ink_ordinals'](wo), NEW['ink_ordinals'](wn)
    if no != nn or oo != on:
        moved.append((b, c, v, no, nn, oo, on, ' '.join(w for w in wn if w.endswith(('|', '*', '%', '~', '@', '#')) or '/' in w)))
    elif wo != wn:
        marked_only.append((b, c, v, [w for w in wn if w.endswith('%')], nn))
tor = [m for m in moved if m[0] in T]
print('verses scanned %d; MOVED %d — the Torah %d in %d verses (predicted 13 verses / 14 tokens), outside %d; MARKED ONLY %d' % (len(verses), len(moved), sum(len([x for x in m[4] if x != 0]) - len([x for x in m[3] if x != 0]) for m in tor), len(tor), len(moved) - len(tor), len(marked_only)))
for b, c, v, no, nn, oo, on, ws in moved:
    print('  MOVED %s %d:%d  numbers %s -> %s%s   [%s]' % (b, c, v, [str(x) for x in no], [str(x) for x in nn], ('  ordinals %s -> %s' % (oo, on)) if oo != on else '', ws))
for b, c, v, ws, nn in marked_only:
    print('  MARKED %s %d:%d  %s  numbers %s' % (b, c, v, ws, nn))
print('THE TORAH VERSES MOVED: %s' % ['%s %d:%d' % (b, c, v) for b, c, v, *_ in tor])
