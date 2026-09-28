#!/bin/zsh
# THE DEUTERONOMY WALK sitting 20 — CHAPTER 32, THE SONG (LEAN): THE FOLD — the tripwire's literals set to the PREDICTION before the bake (units 247 → 249,
# standing 2344 → 2360, the hash unmoved; the design's print), the truth file checked on an unwritten fold, then the bake, then the check again.
# Run from the repo root. Sitting 19's form (ch29_fold.sh) over two units.
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
SP="$(cd "$(dirname "$0")" && pwd)"
for u in deu_32_haazinu deu_32_song_aftermath; do grep -q 'status: frozen' logic/units/$u.yaml || { echo "NOT FROZEN — the fold waits for the ritual ($u)"; exit 1; }; done
python3 - <<'PYEOF'
p = 'logic/corpus/CORPUS_TRUTH.py'; s = open(p, encoding='utf-8').read()
for old, new in (('assert len(W["units"]) == 247\n', 'assert len(W["units"]) == 249\n'), ('assert len(W["standing"]) == 2344\n', 'assert len(W["standing"]) == 2360\n')):
    assert s.count(old) == 1, old
    s = s.replace(old, new)
open(p, 'w', encoding='utf-8').write(s); print('the tripwire set to the prediction: units 249, standing 2360, hash 8b8fff1fa28953af unmoved')
PYEOF
echo "=== CHECK BEFORE THE BAKE (fold unwritten)"; python3 logic/corpus/CORPUS_TRUTH.py 2>&1 | tail -3 > $SP/ch32_fold_check1.out; cat $SP/ch32_fold_check1.out
grep -q 'CORPUS TRUTH GREEN' $SP/ch32_fold_check1.out || { echo "THE PREDICTION DID NOT MATCH — no bake"; exit 1; }
echo "=== THE BAKE"; python3 corpus_world.py > $SP/ch32_bake.out 2>&1; echo "exit $?"; tail -3 $SP/ch32_bake.out
echo "=== CHECK AFTER THE BAKE"; python3 logic/corpus/CORPUS_TRUTH.py 2>&1 | tail -1 | tee $SP/ch32_truth.out
grep -n 'len(W\["units"\]) ==\|len(W\["standing"\]) ==\|_state_hash(W) ==' logic/corpus/CORPUS_TRUTH.py
