#!/bin/zsh
# THE DEUTERONOMY WALK sitting 22 — CHAPTER 34, THE DEATH OF MOSES (LEAN; sitting 20's form ch34_gates.sh): the manifest → the chain (seat, verify_text, the ritual — one unit) →
# the fold → build_world → the journal gate → the register gate --strict → large_letter_probes → the home-path gate, ONE chain, stopping at the first red; the SUMMARY read once.
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
SP="$(cd "$(dirname "$0")" && pwd)"
S=$SP/ch34_gates_SUMMARY.txt; : > $S
step() { echo "=== $1 $(date +%H:%M:%S)" | tee -a $S; }
run() { local name=$1 out=$2; shift 2; step "$name"; "$@" > $out 2>&1; local rc=$?; echo "exit $rc | $(tail -1 $out)" | tee -a $S; [ $rc -eq 0 ] || { echo "STOP at $name" | tee -a $S; exit 1; }; }
# the manifest written before the chain (ch34_manifest.out — six claims over one unit, every cite index name used once)
step chain; zsh $SP/ch34_chain.sh; tail -12 $SP/ch34_chain.log | tee -a $S; for u in deu_34_moses_death; do echo "verify_text $u: $(tail -1 $SP/ch34_vt_$u.out)" | tee -a $S; done
grep -q ALL_DONE $SP/ch34_chain.log || { echo "STOP at chain" | tee -a $S; exit 1; }
step fold; zsh $SP/ch34_fold.sh > $SP/ch34_fold.out 2>&1; tail -5 $SP/ch34_fold.out | tee -a $S
grep -q 'CORPUS TRUTH GREEN' $SP/ch34_truth.out || { echo "STOP at fold" | tee -a $S; exit 1; }
run build_world $SP/ch34_build.out python3 World/build_world.py
run journal_gate $SP/ch34_journal.out python3 World/step9/world_journal.py --gate
run register_gate $SP/ch34_register.out python3 World/step9/register_census.py --strict
run large_letter $SP/ch34_large_letter.out python3 World/step9/large_letter_probes.py
run home_gate $SP/ch34_home_chain.out python3 logic/solo_tools/scrub_home_paths.py --check
echo "ALL GREEN $(date +%H:%M:%S)" | tee -a $S
