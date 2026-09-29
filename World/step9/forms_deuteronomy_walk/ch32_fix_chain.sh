#!/bin/sh
# THE DEUTERONOMY WALK 20b: after the gate's first print and the stitcher's register test — part 1 rederived (the literal calls), the runner chain (assemble, the cases, the graded run), the facts' asserts
# regenerated from the runner's own print and part 1 rederived, then the tape wrap (the second graded run, the gates alone, the recorder, the stitcher, the literals, the tape's first run, checkpoint_check,
# the scan census), then the registration edge filed and the dependency gate alone again; one DONE file (the cache law — launched in the background)
SP="$(cd "$(dirname "$0")" && pwd)"
cd "$(git rev-parse --show-toplevel)" || exit 2
export TIMING=$SP/ch32b_timing.tsv
rm -f $SP/ch32_fix_chain.DONE
sh $SP/tstep.sh "20b part 1 derived, fourth pass (the literal calls for the twenty-four callees)" sh -c "PYTHONPATH=$SP N_DROP=3 python3 $SP/derive_ch32_part1.py > $SP/derive_ch32_part1_4.out 2>&1" || { echo "derive failed" > $SP/ch32_fix_chain.DONE; exit 1; }
sh $SP/ch32_runner_chain.sh > $SP/ch32_runner_chain2.out 2>&1; echo "runner chain rc $?" >> $SP/ch32_runner_chain2.out
if /usr/bin/grep -q "^MATRIX: 72/72" $SP/ch32_runner_run1.out; then
  sh $SP/tstep.sh "20b the facts' asserts regenerated from the runner's own print (parse_ch32_fastcheck.py over ch32_runner_run1.out)" sh -c "python3 $SP/parse_ch32_fastcheck.py ch32_runner_run1.out > $SP/ch32_parse_run1.out 2>&1"
  sh $SP/tstep.sh "20b part 1 derived, fifth pass (every fact asserted — the twenty-four calls' values from the print)" sh -c "PYTHONPATH=$SP N_DROP=3 python3 $SP/derive_ch32_part1.py > $SP/derive_ch32_part1_5.out 2>&1"
  sh $SP/ch32_tape_wrap.sh > $SP/ch32_tape_wrap2.log 2>&1; echo "tape wrap rc $?" >> $SP/ch32_tape_wrap2.log
  if /usr/bin/grep -q "import cold_run_song_charge_nebo" World/step9/cold_run_sequence.py; then
    sh $SP/tstep.sh "20b the registration edge filed (patch_deps_ch32.py --registration — after the stitcher wrote the import)" sh -c "python3 $SP/patch_deps_ch32.py --registration > $SP/patch_deps_ch32_reg.out 2>&1"
    sh $SP/tstep.sh "20b the dependency gate alone, after the demands (the second print)" sh -c "python3 World/step9/dependency_census.py > $SP/ch32b_dependency_after.out 2>&1"
  fi
fi
echo "rc=0" > $SP/ch32_fix_chain.DONE
