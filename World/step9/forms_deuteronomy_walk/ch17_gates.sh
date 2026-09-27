#!/bin/zsh
# THE DEUTERONOMY WALK sitting 15 — CHAPTERS 17-18 (LEAN; sitting 14's form ch16_gates.sh): the manifests → the chain (seat, verify_text, the ritual — two units) →
# the fold → build_world → the journal gate → the register gate --strict → large_letter_probes → the home-path gate, ONE chain, stopping at the first red; the SUMMARY read once.
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
SP="$(cd "$(dirname "$0")" && pwd)"
S=$SP/ch17_gates_SUMMARY.txt; : > $S
step() { echo "=== $1 $(date +%H:%M:%S)" | tee -a $S; }
run() { local name=$1 out=$2; shift 2; step "$name"; "$@" > $out 2>&1; local rc=$?; echo "exit $rc | $(tail -1 $out)" | tee -a $S; [ $rc -eq 0 ] || { echo "STOP at $name" | tee -a $S; exit 1; }; }
# the manifests written before the chain (ch17_manifest.out — eight claims over two units, every cite index name used)
step chain; sh $SP/ch17_chain.sh; tail -6 $SP/ch17_chain.log | tee -a $S; for u in deu_17_courts_king deu_18_levi_prophet; do echo "verify_text $u: $(tail -1 $SP/ch17_vt_$u.out)" | tee -a $S; done
grep -q ALL_DONE $SP/ch17_chain.log || { echo "STOP at chain" | tee -a $S; exit 1; }
step fold; sh $SP/ch17_fold.sh > $SP/ch17_fold.out 2>&1; tail -5 $SP/ch17_fold.out | tee -a $S
grep -q 'CORPUS TRUTH GREEN' $SP/ch17_truth.out || { echo "STOP at fold" | tee -a $S; exit 1; }
run build_world $SP/ch17_build.out python3 World/build_world.py
run journal_gate $SP/ch17_journal.out python3 World/step9/world_journal.py --gate
run register_gate $SP/ch17_register.out python3 World/step9/register_census.py --strict
run large_letter $SP/ch17_large_letter.out python3 World/step9/large_letter_probes.py
run home_gate $SP/ch17_home.out python3 logic/solo_tools/scrub_home_paths.py --check
echo "ALL GREEN $(date +%H:%M:%S)" | tee -a $S
