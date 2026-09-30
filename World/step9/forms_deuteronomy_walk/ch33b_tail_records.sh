#!/bin/sh
# THE DEUTERONOMY WALK 21b (LEAN) — THE TAIL'S RECORDS IN ONE CALL after the job's DONE and its SUMMARY read once (ALL GREEN): the facts whole, the records checked then written,
# the message, the forms, the home gate — each timed; a failed check stops the sequence before any file is written. RUN FROM THE REPO ROOT.
SP="$(cd "$(dirname "$0")" && pwd)"; cd "$(git rev-parse --show-toplevel)" || exit 2; export TIMING=$SP/ch33b_timing.tsv
sh $SP/tstep.sh "21b TAIL the facts read whole from the prints (ch33b_tail_facts.py)" sh -c "PYTHONPATH=$SP python3 $SP/ch33b_tail_facts.py > $SP/ch33b_facts.out 2>&1" || { echo FACTS FAILED; tail -5 $SP/ch33b_facts.out; exit 3; }
sh $SP/tstep.sh "21b TAIL the records checked (write_ch33b_records.py --check)" sh -c "PYTHONPATH=$SP python3 $SP/write_ch33b_records.py --check > $SP/ch33b_records_check.out 2>&1" || { echo RECORDS CHECK FAILED; tail -5 $SP/ch33b_records_check.out; exit 4; }
sh $SP/tstep.sh "21b TAIL the four records, the walk note and the debt line (15) written in one call (write_ch33b_records.py)" sh -c "PYTHONPATH=$SP python3 $SP/write_ch33b_records.py > $SP/ch33b_records_write.out 2>&1" || { echo RECORDS WRITE FAILED; tail -5 $SP/ch33b_records_write.out; exit 5; }
sh $SP/tstep.sh "21b TAIL the commit message built (write_ch33b_commit_msg.py — 21 folded beneath 21b)" sh -c "PYTHONPATH=$SP python3 $SP/write_ch33b_commit_msg.py > $SP/ch33b_commit_msg.out 2>&1" || { echo MESSAGE FAILED; tail -5 $SP/ch33b_commit_msg.out; exit 6; }
sh $SP/tstep.sh "21b TAIL the forms copied (RUN A's, RUN B's and the tail's)" sh -c "python3 $SP/copy_ch33_forms.py > $SP/ch33b_forms3.out 2>&1" || { echo FORMS FAILED; tail -5 $SP/ch33b_forms3.out; exit 7; }
sh $SP/tstep.sh "21b TAIL the home-path gate after the tail (scrub_home_paths.py --check)" sh -c "python3 logic/solo_tools/scrub_home_paths.py --check > $SP/ch33b_home3.out 2>&1" || { echo HOME GATE FAILED; tail -5 $SP/ch33b_home3.out; exit 8; }
echo TAIL RECORDS DONE; tail -1 $SP/ch33b_records_write.out; cat $SP/ch33b_commit_msg.out; cat $SP/ch33b_forms3.out; tail -1 $SP/ch33b_home3.out
