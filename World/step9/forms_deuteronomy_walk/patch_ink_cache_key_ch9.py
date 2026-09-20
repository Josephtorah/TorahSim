import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 7b (2026-09-19): THE EIGHTEENTH SLIP OF THE IMPORT CACHE, read at the first chain (gates_ch9b/probe_ink_cache.out — C2 FAIL on `_SRC` in
# every runner that reads the sequence file): a runner that READS cold_run_sequence.py AT IMPORT (the INK block executed the stitcher's way — `_SRC = open(HERE/
# cold_run_sequence.py).read()`) is keyed on its OWN source and the shared files, so after the tape was re-stitched the cache restored the OLD text of the
# sequence file into those modules (the parser block unchanged, the value not). The fix: the sequence file's digest joins the key for the modules whose source
# names it — those re-harvest once per tape change; the others keep their blobs. FORM unmoved (the blobs' shape is the same; the KEY moved).
import subprocess, re, py_compile
ROOT = _ROOT
P = ROOT + '/World/step9/ink_cache.py'
s = open(P, encoding='utf-8').read()
old = "        key = hashlib.sha256(src.encode('utf-8')).hexdigest() + '|' + shared_key()\n"
assert s.count(old) == 1, s.count(old)
new = ("        key = hashlib.sha256(src.encode('utf-8')).hexdigest() + '|' + shared_key() + ('|' + _sha(os.path.join(ROOT, 'World', 'step9', 'cold_run_sequence.py')) if 'cold_run_sequence.py' in src else '')   # THE DEUTERONOMY WALK 7b (2026-09-19): THE EIGHTEENTH SLIP — a runner that READS THE SEQUENCE FILE at import (the INK block, the stitcher's way: _SRC) restored the OLD text after the tape was re-stitched (ink_cache_probes C2 fell on _SRC in every such module): the sequence file's digest joins the key for those modules alone\n")
s = s.replace(old, new)
open(P, 'w', encoding='utf-8').write(s); py_compile.compile(P, doraise=True)
print('ink_cache.py: the sequence file\'s digest joins the key of every module that reads it; compiles')
