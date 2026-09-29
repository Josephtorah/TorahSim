SP="$(cd "$(dirname "$0")" && pwd)"; cd "$(git rev-parse --show-toplevel)" || exit 2; export TIMING=$SP/ch32b_timing.tsv; rm -f $SP/ch32b_tail_chain2.DONE
sh $SP/tstep.sh "20b TAIL the runner's fifth graded run after the callee bindings' retype (cold_run_song_charge_nebo.py — a miss for this module alone)" sh -c "python3 World/step9/cold_run_song_charge_nebo.py > $SP/ch32_runner_run5.out 2>&1"; RRC=$?
/usr/bin/grep -q "MATRIX: 72/72 cells match the answer sheet" $SP/ch32_runner_run5.out || RRC=98
if [ $RRC = 0 ]; then
  sh $SP/tstep.sh "20b TAIL the import cache cleared whole a second time before the chain's third pass (ink_cache.py --clear — the runner's source moved)" sh -c "python3 World/step9/ink_cache.py --clear > $SP/ch32b_cache_clear2.out 2>&1"
  sh $SP/tstep.sh "20b TAIL the gates chain, third pass, from the tape after the callee bindings' retype and the cache cleared (gates_chain.sh — the positions at four workers)" sh World/step9/gates_chain.sh $SP/ch32b_gates3 > $SP/ch32b_gates3.log 2>&1; CRC=$?; cp $SP/ch32b_gates3/SUMMARY.txt $SP/ch32b_gates3_SUMMARY.txt 2>/dev/null
else CRC=99; fi
{ echo "runner rc=$RRC"; echo "chain rc=$CRC"; } > $SP/ch32b_tail_chain2.DONE
