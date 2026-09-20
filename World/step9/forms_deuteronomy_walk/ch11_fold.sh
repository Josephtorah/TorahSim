#!/bin/zsh
# THE DEUTERONOMY WALK sitting 9 — CHAPTER 11 (the one run): THE FOLD — the tripwire's literals set to the PREDICTION before the bake (units 224 → 225,
# standing 2227 → 2233, the hash unmoved; facts, demands, events, names predicted unchanged), the truth file checked on an unwritten fold, then the
# bake (corpus_world.py regenerates the truth file from the world), then the check again. Run from the repo root. Sitting 8's form (ch10_fold.sh).
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
SP="$(cd "$(dirname "$0")" && pwd)"
grep -q 'status: frozen' logic/units/deu_11_bless_curse_set.yaml || { echo "NOT FROZEN — the fold waits for the ritual"; exit 1; }
python3 - <<'PYEOF'
p = 'logic/corpus/CORPUS_TRUTH.py'; s = open(p, encoding='utf-8').read()
for old, new in (('assert len(W["units"]) == 224\n', 'assert len(W["units"]) == 225\n'), ('assert len(W["standing"]) == 2227\n', 'assert len(W["standing"]) == 2233\n')):
    assert s.count(old) == 1, old
    s = s.replace(old, new)
open(p, 'w', encoding='utf-8').write(s); print('the tripwire set to the prediction: units 225, standing 2233, hash 8b8fff1fa28953af unmoved')
PYEOF
echo "=== CHECK BEFORE THE BAKE (fold unwritten)"; python3 logic/corpus/CORPUS_TRUTH.py 2>&1 | tail -3 > $SP/ch11_fold_check1.out; cat $SP/ch11_fold_check1.out
grep -q 'CORPUS TRUTH GREEN' $SP/ch11_fold_check1.out || { echo "THE PREDICTION DID NOT MATCH — no bake"; exit 1; }
echo "=== THE BAKE"; python3 corpus_world.py > $SP/ch11_bake.out 2>&1; echo "exit $?"; tail -3 $SP/ch11_bake.out
echo "=== CHECK AFTER THE BAKE"; python3 logic/corpus/CORPUS_TRUTH.py 2>&1 | tail -1 | tee $SP/ch11_truth.out
grep -n 'len(W\["units"\]) ==\|len(W\["standing"\]) ==\|_state_hash(W) ==' logic/corpus/CORPUS_TRUTH.py
