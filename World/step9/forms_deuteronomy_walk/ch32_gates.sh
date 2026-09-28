#!/bin/zsh
# THE DEUTERONOMY WALK sitting 20 — CHAPTER 32, THE SONG (LEAN; sitting 19's form ch29_gates.sh): the manifests → the chain (seat, verify_text, the ritual — two units) →
# the fold → build_world → the journal gate → the register gate --strict → large_letter_probes → the home-path gate, ONE chain, stopping at the first red; the SUMMARY read once.
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
SP="$(cd "$(dirname "$0")" && pwd)"
S=$SP/ch32_gates_SUMMARY.txt; : > $S
step() { echo "=== $1 $(date +%H:%M:%S)" | tee -a $S; }
run() { local name=$1 out=$2; shift 2; step "$name"; "$@" > $out 2>&1; local rc=$?; echo "exit $rc | $(tail -1 $out)" | tee -a $S; [ $rc -eq 0 ] || { echo "STOP at $name" | tee -a $S; exit 1; }; }
# the manifests written before the chain (ch32_manifest.out — sixteen claims over two units, every cite index name used once)
step chain; zsh $SP/ch32_chain.sh; tail -12 $SP/ch32_chain.log | tee -a $S; for u in deu_32_haazinu deu_32_song_aftermath; do echo "verify_text $u: $(tail -1 $SP/ch32_vt_$u.out)" | tee -a $S; done
grep -q ALL_DONE $SP/ch32_chain.log || { echo "STOP at chain" | tee -a $S; exit 1; }
step fold; zsh $SP/ch32_fold.sh > $SP/ch32_fold.out 2>&1; tail -5 $SP/ch32_fold.out | tee -a $S
grep -q 'CORPUS TRUTH GREEN' $SP/ch32_truth.out || { echo "STOP at fold" | tee -a $S; exit 1; }
run build_world $SP/ch32_build.out python3 World/build_world.py
run journal_gate $SP/ch32_journal.out python3 World/step9/world_journal.py --gate
run register_gate $SP/ch32_register.out python3 World/step9/register_census.py --strict
run large_letter $SP/ch32_large_letter.out python3 World/step9/large_letter_probes.py
run home_gate $SP/ch32_home_chain.out python3 logic/solo_tools/scrub_home_paths.py --check
echo "ALL GREEN $(date +%H:%M:%S)" | tee -a $S
