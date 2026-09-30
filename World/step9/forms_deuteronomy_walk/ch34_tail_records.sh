#!/bin/sh
# THE DEUTERONOMY WALK 22 (LEAN) — THE TAIL'S RECORDS IN ONE CALL after the chain's SUMMARY and DONE were read once (ALL GREEN) and the display patch written: the records
# checked then written, the message, the forms, the home gate — each timed; a failed check stops the sequence before any file is written. RUN FROM THE REPO ROOT.
SP="$(cd "$(dirname "$0")" && pwd)"; cd "$(git rev-parse --show-toplevel)" || exit 2; export TIMING=$SP/ch34_timing.tsv
sh $SP/tstep.sh "22 TAIL the records checked (write_ch34_records.py --check)" sh -c "PYTHONPATH=$SP python3 $SP/write_ch34_records.py --check > $SP/ch34_records_check.out 2>&1" || { echo RECORDS CHECK FAILED; tail -5 $SP/ch34_records_check.out; exit 4; }
sh $SP/tstep.sh "22 TAIL the four records, the walk note and the debt line (16) written in one call (write_ch34_records.py)" sh -c "PYTHONPATH=$SP python3 $SP/write_ch34_records.py > $SP/ch34_records_write.out 2>&1" || { echo RECORDS WRITE FAILED; tail -5 $SP/ch34_records_write.out; exit 5; }
sh $SP/tstep.sh "22 TAIL the commit message built (write_ch34_commit_msg.py — 21b and 21 folded beneath 22)" sh -c "PYTHONPATH=$SP python3 $SP/write_ch34_commit_msg.py > $SP/ch34_commit_msg.out 2>&1" || { echo MESSAGE FAILED; tail -5 $SP/ch34_commit_msg.out; exit 6; }
sh $SP/tstep.sh "22 TAIL the forms copied (the run's and the tail's)" sh -c "python3 $SP/copy_ch34_forms.py > $SP/ch34_forms2.out 2>&1" || { echo FORMS FAILED; tail -5 $SP/ch34_forms2.out; exit 7; }
sh $SP/tstep.sh "22 TAIL the home-path gate after the tail (scrub_home_paths.py --check)" sh -c "python3 logic/solo_tools/scrub_home_paths.py --check > $SP/ch34_home2.out 2>&1" || { echo HOME GATE FAILED; tail -5 $SP/ch34_home2.out; exit 8; }
echo TAIL RECORDS DONE; head -c 3000 $SP/ch34_records_check.out; echo; tail -1 $SP/ch34_records_write.out; cat $SP/ch34_commit_msg.out; cat $SP/ch34_forms2.out; tail -1 $SP/ch34_home2.out
