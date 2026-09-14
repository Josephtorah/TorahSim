#!/bin/zsh
cd <repo-old>
for p in installation_probes clock_probes sequence_probes cursor_probes view_probes journal_probes; do
  echo "==== $p" ; python3 World/step9/$p.py 2>&1 | tail -4 ; echo "exit ${pipestatus[1]}"
done
echo "==== journal gate"; python3 World/step9/world_journal.py --gate 2>&1 | tail -8; echo "exit ${pipestatus[1]}"
echo "==== sweep"; python3 World/step9/run_cold_all.py 2>&1 | tail -8; echo "exit ${pipestatus[1]}"
echo "==== chain done"
