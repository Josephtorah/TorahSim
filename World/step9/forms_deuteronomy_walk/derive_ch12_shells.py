import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# derives ch12_chain.sh, ch12_fold.sh, ch12_gates.sh from chapter 11's forms by ASSERTED substitutions (each named old string present exactly once; the
# sitting's own name then replaced everywhere, the form's name in the comment protected)
import subprocess
ROOT = _ROOT
SP = __file__.rsplit('/', 1)[0]
F = f'{ROOT}/World/step9/forms_deuteronomy_walk'
def derive(name, subs, form_comment=None):
    t = open(f'{F}/ch11_{name}', encoding='utf-8').read()
    for a, b in subs:
        assert t.count(a) == 1, ('NOT ONCE', name, t.count(a), a[:70])
        t = t.replace(a, b)
    n11 = t.count('ch11'); t = t.replace('ch11', 'ch12')
    if form_comment: t = t.replace('@FORM@', form_comment)
    nu = t.count('deu_11_bless_curse_set'); t = t.replace('deu_11_bless_curse_set', 'deu_12_place_name')
    assert 'ch11' not in t.replace(form_comment or '', '') and 'deu_11' not in t and 'sitting 9 —' not in t and 'CHAPTER 11' not in t, name
    open(f'{SP}/ch12_{name}', 'w', encoding='utf-8').write(t)
    print(f'ch12_{name}: {len(subs)} named substitutions, ch11->ch12 x{n11}, the unit x{nu}, {len(t)} bytes')
derive('chain.sh', [
 ("# THE DEUTERONOMY WALK sitting 9 — CHAPTER 11 (the one run): seat (once) → verify_text → the freeze ritual; run from the repo root (ROOT from the cwd's git).\n# Sitting 8's form (ch10_chain.sh); SP the scratchpad this script lives in.",
  "# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12 (the one run and its tail): seat (once) → verify_text → the freeze ritual; run from the repo root (ROOT from the cwd's git).\n# Sitting 9's form (@FORM@); SP the scratchpad this script lives in."),
], 'ch11_chain.sh')
derive('fold.sh', [
 ("# THE DEUTERONOMY WALK sitting 9 — CHAPTER 11 (the one run): THE FOLD — the tripwire's literals set to the PREDICTION before the bake (units 224 → 225,\n# standing 2227 → 2233, the hash unmoved;",
  "# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12 (the one run and its tail): THE FOLD — the tripwire's literals set to the PREDICTION before the bake (units 225 → 226,\n# standing 2233 → 2239, the hash unmoved;"),
 ("Sitting 8's form (ch10_fold.sh).", "Sitting 9's form (@FORM@)."),
 ("('assert len(W[\"units\"]) == 224\\n', 'assert len(W[\"units\"]) == 225\\n')", "('assert len(W[\"units\"]) == 225\\n', 'assert len(W[\"units\"]) == 226\\n')"),
 ("('assert len(W[\"standing\"]) == 2227\\n', 'assert len(W[\"standing\"]) == 2233\\n')", "('assert len(W[\"standing\"]) == 2233\\n', 'assert len(W[\"standing\"]) == 2239\\n')"),
 ("print('the tripwire set to the prediction: units 225, standing 2233, hash 8b8fff1fa28953af unmoved')", "print('the tripwire set to the prediction: units 226, standing 2239, hash 8b8fff1fa28953af unmoved')"),
], 'ch11_fold.sh')
derive('gates.sh', [
 ("# THE DEUTERONOMY WALK sitting 9 — CHAPTER 11 (the one run): the manifest → the chain", "# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12 (the one run and its tail; sitting 9's form ch11_gates.sh): the manifest → the chain"),
 ("(ch11_manifest.out — six claims, every cite index name used)", "(@FORM@ — six claims, every cite index name used)"),
], 'ch12_manifest.out')
