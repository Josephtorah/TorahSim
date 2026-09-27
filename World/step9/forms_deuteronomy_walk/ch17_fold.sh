#!/bin/zsh
# THE DEUTERONOMY WALK sitting 15 — CHAPTERS 17-18 (LEAN): THE FOLD — the tripwire's literals set to the PREDICTION before the bake (units 230 → 232,
# standing 2267 → 2275, the hash unmoved; the design's print), the truth file checked on an unwritten fold, then the bake, then the check again.
# Run from the repo root. Sitting 14's form (ch16_fold.sh) over two units.
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
SP="$(cd "$(dirname "$0")" && pwd)"
for u in deu_17_courts_king deu_18_levi_prophet; do grep -q 'status: frozen' logic/units/$u.yaml || { echo "NOT FROZEN — the fold waits for the ritual ($u)"; exit 1; }; done
python3 - <<'PYEOF'
p = 'logic/corpus/CORPUS_TRUTH.py'; s = open(p, encoding='utf-8').read()
for old, new in (('assert len(W["units"]) == 230\n', 'assert len(W["units"]) == 232\n'), ('assert len(W["standing"]) == 2267\n', 'assert len(W["standing"]) == 2275\n')):
    assert s.count(old) == 1, old
    s = s.replace(old, new)
open(p, 'w', encoding='utf-8').write(s); print('the tripwire set to the prediction: units 232, standing 2275, hash 8b8fff1fa28953af unmoved')
PYEOF
echo "=== CHECK BEFORE THE BAKE (fold unwritten)"; python3 logic/corpus/CORPUS_TRUTH.py 2>&1 | tail -3 > $SP/ch17_fold_check1.out; cat $SP/ch17_fold_check1.out
grep -q 'CORPUS TRUTH GREEN' $SP/ch17_fold_check1.out || { echo "THE PREDICTION DID NOT MATCH — no bake"; exit 1; }
echo "=== THE BAKE"; python3 corpus_world.py > $SP/ch17_bake.out 2>&1; echo "exit $?"; tail -3 $SP/ch17_bake.out
echo "=== CHECK AFTER THE BAKE"; python3 logic/corpus/CORPUS_TRUTH.py 2>&1 | tail -1 | tee $SP/ch17_truth.out
grep -n 'len(W\["units"\]) ==\|len(W\["standing"\]) ==\|_state_hash(W) ==' logic/corpus/CORPUS_TRUTH.py
