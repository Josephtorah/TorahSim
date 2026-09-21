import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# derives ch13_chain.sh, ch13_fold.sh, ch13_gates.sh from chapter 12's forms by ASSERTED substitutions (each named old string present exactly once; the
# sitting's own name then replaced everywhere; THE FORM'S NAME PROTECTED BY A PLACEHOLDER IN EVERY SHELL — chapter 12's lesson 12). derive_ch12_shells.py's form.
import subprocess
ROOT = _ROOT
SP = __file__.rsplit('/', 1)[0]
F = f'{ROOT}/World/step9/forms_deuteronomy_walk'
def derive(name, subs, protect):
    t = open(f'{F}/ch12_{name}', encoding='utf-8').read()
    for a, b in subs:
        assert t.count(a) == 1, ('NOT ONCE', name, t.count(a), a[:70])
        t = t.replace(a, b)
    n12 = t.count('ch12'); t = t.replace('ch12', 'ch13')
    for i, p in enumerate(protect):
        assert t.count(f'@P{i}@') == 1, (name, p); t = t.replace(f'@P{i}@', p)
    nu = t.count('deu_12_place_name'); t = t.replace('deu_12_place_name', 'deu_13_seducers')
    bare = t
    for p in protect: bare = bare.replace(p, '')
    assert 'ch12' not in bare and 'deu_12' not in t and 'sitting 10 —' not in t and 'CHAPTER 12' not in t and '@P' not in t, name
    open(f'{SP}/ch13_{name}', 'w', encoding='utf-8').write(t)
    print(f"ch13_{name}: {len(subs)} named substitutions, ch12->ch13 x{n12}, the unit x{nu}, the form's name protected {protect}, {len(t)} bytes")
derive('chain.sh', [
 ("# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12 (the one run and its tail): seat (once) → verify_text → the freeze ritual; run from the repo root (ROOT from the cwd's git).\n# Sitting 9's form (ch11_chain.sh); SP the scratchpad this script lives in.",
  "# THE DEUTERONOMY WALK sitting 11 — CHAPTER 13 (the one run and its tail): seat (once) → verify_text → the freeze ritual; run from the repo root (ROOT from the cwd's git).\n# Sitting 10's form (@P0@); SP the scratchpad this script lives in."),
], ['ch12_chain.sh'])
derive('fold.sh', [
 ("# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12 (the one run and its tail): THE FOLD — the tripwire's literals set to the PREDICTION before the bake (units 225 → 226,\n# standing 2233 → 2239, the hash unmoved;",
  "# THE DEUTERONOMY WALK sitting 11 — CHAPTER 13 (the one run and its tail): THE FOLD — the tripwire's literals set to the PREDICTION before the bake (units 226 → 227,\n# standing 2239 → 2245, the hash unmoved;"),
 ("Sitting 9's form (ch11_fold.sh).", "Sitting 10's form (@P0@)."),
 ("('assert len(W[\"units\"]) == 225\\n', 'assert len(W[\"units\"]) == 226\\n')", "('assert len(W[\"units\"]) == 226\\n', 'assert len(W[\"units\"]) == 227\\n')"),
 ("('assert len(W[\"standing\"]) == 2233\\n', 'assert len(W[\"standing\"]) == 2239\\n')", "('assert len(W[\"standing\"]) == 2239\\n', 'assert len(W[\"standing\"]) == 2245\\n')"),
 ("print('the tripwire set to the prediction: units 226, standing 2239, hash 8b8fff1fa28953af unmoved')", "print('the tripwire set to the prediction: units 227, standing 2245, hash 8b8fff1fa28953af unmoved')"),
], ['ch12_fold.sh'])
derive('gates.sh', [
 ("# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12 (the one run and its tail; sitting 9's form ch11_gates.sh): the manifest → the chain", "# THE DEUTERONOMY WALK sitting 11 — CHAPTER 13 (the one run and its tail; sitting 10's form @P0@): the manifest → the chain"),
], ['ch12_gates.sh'])
