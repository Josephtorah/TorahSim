#!/usr/bin/env python3
# THE DEUTERONOMY WALK 4b (2026-09-17): a prior sitting's script derived from its FORMS COPY — the copy tool's three-level _ROOT header (right in the
# forms folder, wrong in the scratchpad) turned back into the git root (the rule: scratch scripts take ROOT from git, run from the repo root), then the
# substitutions applied, each asserted to hit. Usage: derive_form.py SRC DST OLD=>NEW [OLD=>NEW ...]
import re, sys
src, dst, subs = sys.argv[1], sys.argv[2], sys.argv[3:]
s = open(src, encoding='utf-8').read()
HDR = re.compile(r"^_ROOT = _os\.path\.normpath\(_os\.path\.join\(_os\.path\.dirname\(_os\.path\.abspath\(__file__\)\), '\.\.', '\.\.', '\.\.'\)\)[^\n]*$", re.M)
n = len(HDR.findall(s)); assert n >= 1, ('no forms header in', src)
s = HDR.sub("_ROOT = __import__('subprocess').check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()   # the git root (a scratch script, run from the repo root)", s)
for sub in subs:
    old, new = sub.split('=>', 1); assert old in s, ('substitution misses', old[:60]); s = s.replace(old, new)
open(dst, 'w', encoding='utf-8').write(s); print('derived', dst.rsplit('/', 1)[1], 'headers', n, 'subs', len(subs))
