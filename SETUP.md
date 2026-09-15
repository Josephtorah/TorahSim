# SETUP — running TorahSim from a fresh clone

This repository is the workshop of a machine that reads the Torah as a program: the frozen units (the reading), the compiled runners
(the law), the tape (the running world), the journal (the one database) and the board (the window). Every path in the code is computed
from each file's own place, so the clone runs from any folder. Three things are not in the clone until you fetch or build them.

## 1. Clone

    git clone https://github.com/Josephtorah/TorahSim.git
    cd TorahSim

Python 3.12 or newer, with `pyyaml` (`python3 -m pip install --user pyyaml`; on a Homebrew Python add `--break-system-packages`).

## 2. The shelf (2.3 GB, not tracked)

The readings and the exam dockets open Sefaria's export files under `Data/sefaria_export`. The manifest there names every file, its
source in Sefaria's public export, its size and its hash. Fetch them once:

    python3 Data/fetch_shelf.py            # fetches every file the manifest names, then checks each one
    python3 Data/fetch_shelf.py --check    # any time: every file against the manifest, no network

The Bible store the runners read (`Data/tanakh.sqlite`) is tracked and arrives with the clone.

## 3. The one database (derived, not tracked)

    python3 World/build_world.py           # folds the frozen units, builds World/journal/data/world.sqlite, reconciles — ALL GREEN
    python3 World/step9/cold_run_sequence.py   # runs the tape: the four books on one world, 10/10 at the end (about two minutes)

## 4. Watch it

    python3 World/step9/world_board.py                       # the board at http://127.0.0.1:8765/
    python3 World/step9/world_stepper.py --by verse --pace 1   # in another window: the tape one verse a second

Or step by hand: `python3 World/step9/world_stepper.py --by chapter --pause --show checkpoints`.

## 5. The gates

    python3 World/step9/world_journal.py --gate            # the tape twice in two processes, byte-identical; the fold layer against the pinned truth
    python3 World/step9/run_cold_all.py                    # the sweep: every runner (about fifteen minutes)
    python3 World/step9/portable_probes.py                 # the clone-at-another-path proof of this very setup

## Where to read

THE_STEPS.md (the process in plain words), THE_BRIEFING.md (the big picture), THE_WORLD.md (the simulation's master file),
World/README.md and World/RESUME.md (the world's folder), World/step9/THE_LOOP.md (the running world with memory),
logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md (the one-read entry point for a new thread).
