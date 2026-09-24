#!/bin/zsh
# THE DEUTERONOMY WALK sitting 14 — CHAPTER 16 (LEAN; sitting 13's form ch16_gates.sh): the manifest → the chain (seat, verify_text, the ritual) → the fold → build_world →
# the journal gate → the register gate --strict → large_letter_probes → the home-path gate, ONE chain, stopping at the first red; the SUMMARY read once.
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
SP="$(cd "$(dirname "$0")" && pwd)"
S=$SP/ch16_gates_SUMMARY.txt; : > $S
step() { echo "=== $1 $(date +%H:%M:%S)" | tee -a $S; }
run() { local name=$1 out=$2; shift 2; step "$name"; "$@" > $out 2>&1; local rc=$?; echo "exit $rc | $(tail -1 $out)" | tee -a $S; [ $rc -eq 0 ] || { echo "STOP at $name" | tee -a $S; exit 1; }; }
# the manifest written before the chain (ch16_manifest.out — eight claims, every cite index name used)
step chain; sh $SP/ch16_chain.sh; tail -4 $SP/ch16_chain.log | tee -a $S; echo "verify_text: $(tail -1 $SP/ch16_vt_deu_16_festivals_judges.out)" | tee -a $S
grep -q ALL_DONE $SP/ch16_chain.log || { echo "STOP at chain" | tee -a $S; exit 1; }
step fold; sh $SP/ch16_fold.sh > $SP/ch16_fold.out 2>&1; tail -5 $SP/ch16_fold.out | tee -a $S
grep -q 'CORPUS TRUTH GREEN' $SP/ch16_truth.out || { echo "STOP at fold" | tee -a $S; exit 1; }
run build_world $SP/ch16_build.out python3 World/build_world.py
run journal_gate $SP/ch16_journal.out python3 World/step9/world_journal.py --gate
run register_gate $SP/ch16_register.out python3 World/step9/register_census.py --strict
run large_letter $SP/ch16_large_letter.out python3 World/step9/large_letter_probes.py
run home_gate $SP/ch16_home.out python3 logic/solo_tools/scrub_home_paths.py --check
echo "ALL GREEN $(date +%H:%M:%S)" | tee -a $S
