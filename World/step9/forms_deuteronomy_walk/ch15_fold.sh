#!/bin/zsh
# THE DEUTERONOMY WALK sitting 13 — CHAPTER 15 (two runs and the tail): THE FOLD — the tripwire's literals set to the PREDICTION before the bake (units 228 → 229,
# standing 2252 → 2259, the hash unmoved; facts, demands, events, names predicted unchanged), the truth file checked on an unwritten fold, then the
# bake (corpus_world.py regenerates the truth file from the world), then the check again. Run from the repo root. Sitting 12's form (ch14_fold.sh).
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
SP="$(cd "$(dirname "$0")" && pwd)"
grep -q 'status: frozen' logic/units/deu_15_release_firstborn.yaml || { echo "NOT FROZEN — the fold waits for the ritual"; exit 1; }
python3 - <<'PYEOF'
p = 'logic/corpus/CORPUS_TRUTH.py'; s = open(p, encoding='utf-8').read()
for old, new in (('assert len(W["units"]) == 228\n', 'assert len(W["units"]) == 229\n'), ('assert len(W["standing"]) == 2252\n', 'assert len(W["standing"]) == 2259\n')):
    assert s.count(old) == 1, old
    s = s.replace(old, new)
open(p, 'w', encoding='utf-8').write(s); print('the tripwire set to the prediction: units 229, standing 2259, hash 8b8fff1fa28953af unmoved')
PYEOF
echo "=== CHECK BEFORE THE BAKE (fold unwritten)"; python3 logic/corpus/CORPUS_TRUTH.py 2>&1 | tail -3 > $SP/ch15_fold_check1.out; cat $SP/ch15_fold_check1.out
grep -q 'CORPUS TRUTH GREEN' $SP/ch15_fold_check1.out || { echo "THE PREDICTION DID NOT MATCH — no bake"; exit 1; }
echo "=== THE BAKE"; python3 corpus_world.py > $SP/ch15_bake.out 2>&1; echo "exit $?"; tail -3 $SP/ch15_bake.out
echo "=== CHECK AFTER THE BAKE"; python3 logic/corpus/CORPUS_TRUTH.py 2>&1 | tail -1 | tee $SP/ch15_truth.out
grep -n 'len(W\["units"\]) ==\|len(W\["standing"\]) ==\|_state_hash(W) ==' logic/corpus/CORPUS_TRUTH.py
