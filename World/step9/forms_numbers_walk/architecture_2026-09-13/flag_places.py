#!/usr/bin/env python3
# Reproduces gloss_lint.py's three checks (the first occurrence of each Hebrew run / transliterated compound / jargon word, the
# 90-character period-stopped window) and reports WHERE: file, line, column, the token, and the line with its successor.
import re, sys, json
sys.path.insert(0, '<repo-old>/logic/solo_tools'); import gloss_lint as G
def places(path):
    text = open(path, encoding='utf-8').read(); out = []; seen = set()
    def ln(pos): return text.count('\n', 0, pos) + 1
    for m in G.HEBREW_RUN.finditer(text):
        run = m.group(0)
        if len(run) < 2 or run in seen: continue
        seen.add(run)
        if not G.GLOSS_NEAR.match(text[m.end():m.end()+120]): out.append((ln(m.start()), run, m.start()))
    for m in G.TRANSLIT.finditer(text):
        tok = m.group(0)
        if tok in seen or tok.count('-') > 3: continue
        seen.add(tok)
        if any(p in tok for p in ("http", "json", "yaml", "html", "py", "note", "self", "left", "right", "one", "first", "check", "claims", "audit", "translit")): continue
        def eng(p):
            p = p.lower(); return any(x in G.ENGLISH for x in (p, p.rstrip("s"), p[:-1], p[:-2], p[:-3] + "e" if len(p) > 3 else p))
        if G.ENGLISH and all(eng(p) for p in tok.split('-')): continue
        if not G.GLOSS_NEAR.match(text[m.end():m.end()+120]): out.append((ln(m.start()), tok, m.start()))
    for w in sorted(G.JARGON):
        i = re.search(r"\b%s\b" % w, text, re.I)
        if i and w not in seen and not G.GLOSS_NEAR.match(text[i.end():i.end()+120]): out.append((ln(i.start()), w, i.start()))
    lines = text.split('\n')
    return [(l, t, lines[l-1], lines[l] if l < len(lines) else '') for l, t, _ in sorted(out)]
files = [l.split(' ', 1)[1].strip() for l in open(sys.argv[1]) if 'oral_triage' in l and not l.startswith('0 ')] + ['./World/step9/EXAM_LEDGER.md', './World/step9/REPORT_CANON_HUNT.md', './World/step9/REPORT_FESTIVALS.md', './logic/CORE_SHELF.md']
rep = []; n = 0
for f in files:
    ps = places(f)
    for l, t, line, nxt in ps:
        n += 1; rep.append('%s:%d [%s]\n    %s\n    +%s' % (f, l, t, line[:400], nxt[:160]))
open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(rep) + '\n')
print('files', len(files), 'flagged places', n)
