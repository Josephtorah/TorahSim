#!/bin/zsh
# THE DEUTERONOMY WALK sitting 9 — CHAPTER 11 (the one run): the manifest → the chain (seat, verify_text, the ritual) → the fold → build_world →
# the journal gate → the register gate --strict → large_letter_probes → the home-path gate, ONE chain, stopping at the first red; the SUMMARY read once.
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
SP="$(cd "$(dirname "$0")" && pwd)"
S=$SP/ch11_gates_SUMMARY.txt; : > $S
step() { echo "=== $1 $(date +%H:%M:%S)" | tee -a $S; }
run() { local name=$1 out=$2; shift 2; step "$name"; "$@" > $out 2>&1; local rc=$?; echo "exit $rc | $(tail -1 $out)" | tee -a $S; [ $rc -eq 0 ] || { echo "STOP at $name" | tee -a $S; exit 1; }; }
# the manifest written before the chain (ch11_manifest.out — six claims, every cite index name used)
step chain; sh $SP/ch11_chain.sh; tail -4 $SP/ch11_chain.log | tee -a $S; echo "verify_text: $(tail -1 $SP/ch11_vt_deu_11_bless_curse_set.out)" | tee -a $S
grep -q ALL_DONE $SP/ch11_chain.log || { echo "STOP at chain" | tee -a $S; exit 1; }
step fold; sh $SP/ch11_fold.sh > $SP/ch11_fold.out 2>&1; tail -5 $SP/ch11_fold.out | tee -a $S
grep -q 'CORPUS TRUTH GREEN' $SP/ch11_truth.out || { echo "STOP at fold" | tee -a $S; exit 1; }
run build_world $SP/ch11_build.out python3 World/build_world.py
run journal_gate $SP/ch11_journal.out python3 World/step9/world_journal.py --gate
run register_gate $SP/ch11_register.out python3 World/step9/register_census.py --strict
run large_letter $SP/ch11_large_letter.out python3 World/step9/large_letter_probes.py
run home_gate $SP/ch11_home.out python3 logic/solo_tools/scrub_home_paths.py --check
echo "ALL GREEN $(date +%H:%M:%S)" | tee -a $S
