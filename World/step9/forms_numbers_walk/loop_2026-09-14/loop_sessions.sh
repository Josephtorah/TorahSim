#!/bin/zsh
ROOT="$(cd "$(dirname "$0")" && git rev-parse --show-toplevel)"   # THE PORTABLE REPO (2026-09-15): the repo root from this script's own place
# THE STEPPER's real sessions (sequential: they share the data dir and the session's source), then the tape, then the three probe files
cd "$ROOT"
echo '==== SESSION A: from the left edge of Num 27:1, by verse, to the left edge of Num 28:1, showing the open entries ===='
/usr/bin/env python3 World/step9/world_stepper.py --from 'Num 27:1' --to 'Num 28:1' --by verse --show open 2>&1 | /usr/bin/grep -v '^guard:\|^probes:\|^callees\|^$'
echo "exit $?"
echo '==== SESSION B: the whole tape by marker, quiet ===='
/usr/bin/env python3 World/step9/world_stepper.py --by marker --quiet 2>&1 | /usr/bin/grep -v '^guard:\|^probes:\|^callees\|^$' > loop_session_b.out
echo "exit $?"; /usr/bin/wc -l loop_session_b.out; /usr/bin/head -3 loop_session_b.out; /usr/bin/tail -4 loop_session_b.out
echo '==== THE BODIES COMPARED: the session segment against the base, line for line after the header ===='
/usr/bin/env python3 - <<'PY'
b = open('"$ROOT"/World/journal/data/L3_run_cold_run_sequence_seed_isaac.jsonl', encoding='utf-8').read().split('\n')
s = open('"$ROOT"/World/journal/data/L3_run_cold_run_sequence_stepper.jsonl', encoding='utf-8').read().split('\n')
print('base header:   ', b[0]); print('session header:', s[0])
print('bodies identical: %s (%d lines each)' % (b[1:] == s[1:], len([l for l in s[1:] if l.strip()])))
PY
echo '==== THE TAPE (the live report lists the session as a fifth source) ===='
/usr/bin/env python3 World/step9/cold_run_sequence.py 2>&1 | /usr/bin/grep 'checkpoints$\|JOURNAL INDEX\|THE SEAL' | /usr/bin/cut -c1-330
echo '==== THE PROBES ===='
for f in live_probes journal_probes cursor_probes step_probes; do printf '%s: ' "$f"; /usr/bin/env python3 World/step9/$f.py 2>&1 | /usr/bin/grep 'probes$' | /usr/bin/tail -1; done
echo '==== DONE ===='
