#!/bin/zsh
# THE DEUTERONOMY WALK sitting 16 — CHAPTERS 19-21 (LEAN; sitting 15's form ch17_gates.sh): the manifests → the chain (seat, verify_text, the ritual — three units) →
# the fold → build_world → the journal gate → the register gate --strict → large_letter_probes → the home-path gate, ONE chain, stopping at the first red; the SUMMARY read once.
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
SP="$(cd "$(dirname "$0")" && pwd)"
S=$SP/ch19_gates_SUMMARY.txt; : > $S
step() { echo "=== $1 $(date +%H:%M:%S)" | tee -a $S; }
run() { local name=$1 out=$2; shift 2; step "$name"; "$@" > $out 2>&1; local rc=$?; echo "exit $rc | $(tail -1 $out)" | tee -a $S; [ $rc -eq 0 ] || { echo "STOP at $name" | tee -a $S; exit 1; }; }
# the manifests written before the chain (ch19_manifest.out — thirteen claims over three units, every cite index name used)
step chain; sh $SP/ch19_chain.sh; tail -8 $SP/ch19_chain.log | tee -a $S; for u in deu_19_miklat_witness deu_20_war_rules deu_21_eglah_family; do echo "verify_text $u: $(tail -1 $SP/ch19_vt_$u.out)" | tee -a $S; done
grep -q ALL_DONE $SP/ch19_chain.log || { echo "STOP at chain" | tee -a $S; exit 1; }
step fold; sh $SP/ch19_fold.sh > $SP/ch19_fold.out 2>&1; tail -5 $SP/ch19_fold.out | tee -a $S
grep -q 'CORPUS TRUTH GREEN' $SP/ch19_truth.out || { echo "STOP at fold" | tee -a $S; exit 1; }
run build_world $SP/ch19_build.out python3 World/build_world.py
run journal_gate $SP/ch19_journal.out python3 World/step9/world_journal.py --gate
run register_gate $SP/ch19_register.out python3 World/step9/register_census.py --strict
run large_letter $SP/ch19_large_letter.out python3 World/step9/large_letter_probes.py
run home_gate $SP/ch19_home.out python3 logic/solo_tools/scrub_home_paths.py --check
echo "ALL GREEN $(date +%H:%M:%S)" | tee -a $S
