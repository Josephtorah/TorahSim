#!/bin/zsh
# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12 (the one run and its tail; sitting 9's form ch11_gates.sh): the manifest → the chain (seat, verify_text, the ritual) → the fold → build_world →
# the journal gate → the register gate --strict → large_letter_probes → the home-path gate, ONE chain, stopping at the first red; the SUMMARY read once.
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
SP="$(cd "$(dirname "$0")" && pwd)"
S=$SP/ch12_gates_SUMMARY.txt; : > $S
step() { echo "=== $1 $(date +%H:%M:%S)" | tee -a $S; }
run() { local name=$1 out=$2; shift 2; step "$name"; "$@" > $out 2>&1; local rc=$?; echo "exit $rc | $(tail -1 $out)" | tee -a $S; [ $rc -eq 0 ] || { echo "STOP at $name" | tee -a $S; exit 1; }; }
# the manifest written before the chain (ch12_manifest.out — six claims, every cite index name used)
step chain; sh $SP/ch12_chain.sh; tail -4 $SP/ch12_chain.log | tee -a $S; echo "verify_text: $(tail -1 $SP/ch12_vt_deu_12_place_name.out)" | tee -a $S
grep -q ALL_DONE $SP/ch12_chain.log || { echo "STOP at chain" | tee -a $S; exit 1; }
step fold; sh $SP/ch12_fold.sh > $SP/ch12_fold.out 2>&1; tail -5 $SP/ch12_fold.out | tee -a $S
grep -q 'CORPUS TRUTH GREEN' $SP/ch12_truth.out || { echo "STOP at fold" | tee -a $S; exit 1; }
run build_world $SP/ch12_build.out python3 World/build_world.py
run journal_gate $SP/ch12_journal.out python3 World/step9/world_journal.py --gate
run register_gate $SP/ch12_register.out python3 World/step9/register_census.py --strict
run large_letter $SP/ch12_large_letter.out python3 World/step9/large_letter_probes.py
run home_gate $SP/ch12_home.out python3 logic/solo_tools/scrub_home_paths.py --check
echo "ALL GREEN $(date +%H:%M:%S)" | tee -a $S
