import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 8b (2026-09-20): THE CACHE'S NINETEENTH SLIP — ITS OWN ERROR REPORT. The chain's second pass failed at the positions table: one of the eight
# workers raised on the cached path, and the cache's report of WHICH node raised crashed itself — `ast.get_source_segment(src, node)` with `src` no longer the
# module's source text: the restore loop had rebound `src` to a MODULE (an alias's home module; a patch's source module) a few lines above, so the report's
# TypeError ('expected string or bytes-like object, got module') masked the real error. The two rebindings renamed srcm; the report and the slow-node record read
# the source text again. FORM unmoved (the cached path's behaviour untouched — only what it says when it fails). A single worker rerun clean after the fix; the
# table measured by four workers (7b's way). Idempotent: asserts the fix is in place (applied inline at the sitting, this file the record of it).
import subprocess, py_compile
ROOT = _ROOT
P = ROOT + '/World/step9/ink_cache.py'
s = open(P, encoding='utf-8').read()
a = "                            src = sys.modules.get(h[1]); o = src.__dict__.get(h[2], _MISSING) if src is not None else _MISSING\n"
b = "                                    src = sys.modules.get(mod)\n                                    if src is not None and nm in src.__dict__: o = _patch(o, path, src.__dict__[nm])\n"
if s.count(a) == 1 and s.count(b) == 1:
    s = s.replace(a, "                            srcm = sys.modules.get(h[1]); o = srcm.__dict__.get(h[2], _MISSING) if srcm is not None else _MISSING   # THE DEUTERONOMY WALK 8b (2026-09-20): srcm, not src — the module's SOURCE TEXT `src` was shadowed here and at the patch loop, so the cached path's own error report (a node raising) and the slow-node record crashed on get_source_segment(a module): THE NINETEENTH SLIP, the cache's own reporting; FORM unmoved\n")
    s = s.replace(b, "                                    srcm = sys.modules.get(mod)\n                                    if srcm is not None and nm in srcm.__dict__: o = _patch(o, path, srcm.__dict__[nm])\n")
    open(P, 'w', encoding='utf-8').write(s)
s = open(P, encoding='utf-8').read()
assert "srcm = sys.modules.get(h[1]); o = srcm.__dict__.get(h[2], _MISSING)" in s and "srcm = sys.modules.get(mod)" in s and a not in s and b not in s
py_compile.compile(P, doraise=True)
print('ink_cache.py: the shadowed src renamed srcm at the two rebindings (the nineteenth slip — the report reads the source text again); compiles')
