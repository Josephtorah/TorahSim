#!/bin/zsh
# THE DEUTERONOMY WALK sitting 6 — CHAPTER 8 (the one run): the manifest → the chain (seat, verify_text, the ritual) → the fold → build_world →
# the journal gate → the register gate --strict → large_letter_probes → the home-path gate, ONE chain, stopping at the first red; the SUMMARY read once.
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
SP="$(cd "$(dirname "$0")" && pwd)"
S=$SP/ch8_gates_SUMMARY.txt; : > $S
step() { echo "=== $1 $(date +%H:%M:%S)" | tee -a $S; }
run() { local name=$1 out=$2; shift 2; step "$name"; "$@" > $out 2>&1; local rc=$?; echo "exit $rc | $(tail -1 $out)" | tee -a $S; [ $rc -eq 0 ] || { echo "STOP at $name" | tee -a $S; exit 1; }; }
run manifest $SP/ch8_manifest.out python3 $SP/write_ch8_manifest.py
step chain; sh $SP/ch8_chain.sh; tail -4 $SP/ch8_chain.log | tee -a $S; echo "verify_text: $(tail -1 $SP/ch8_vt_deu_08_manna_humility.out)" | tee -a $S
grep -q ALL_DONE $SP/ch8_chain.log || { echo "STOP at chain" | tee -a $S; exit 1; }
step fold; sh $SP/ch8_fold.sh > $SP/ch8_fold.out 2>&1; tail -5 $SP/ch8_fold.out | tee -a $S
grep -q 'CORPUS TRUTH GREEN' $SP/ch8_truth.out || { echo "STOP at fold" | tee -a $S; exit 1; }
run build_world $SP/ch8_build.out python3 World/build_world.py
run journal_gate $SP/ch8_journal.out python3 World/step9/world_journal.py --gate
run register_gate $SP/ch8_register.out python3 World/step9/register_census.py --strict
run large_letter $SP/ch8_large_letter.out python3 World/step9/large_letter_probes.py
run home_gate $SP/ch8_home.out python3 logic/solo_tools/scrub_home_paths.py --check
echo "ALL GREEN $(date +%H:%M:%S)" | tee -a $S
