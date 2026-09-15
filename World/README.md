> **PORTABLE 2026-09-15 (reviews/PORTABLE_repo_2026-09-15.md).** Every path in this folder's code is computed from the file's own place;
> the repo runs from any folder and from a fresh clone (SETUP.md at the root: the shelf and the stores by `Data/fetch_shelf.py`, the one
> database by `build_world.py`). The Bible store the runners read is `Data/tanakh.sqlite`. The folder is renamed TorahSim.
>
> **THE CHECKPOINTS AS THEY FALL 2026-09-14 (World/step9/THE_LOOP.md item 5's build).** The tape's checkpoints are a function of the
> world (`cold_run_sequence.checkpoints`); where each one falls is measured by `python3 step9/checkpoint_positions.py` (the table
> `step9/checkpoint_positions.yaml`; `--check`); `python3 step9/world_stepper.py --by chapter --show checkpoints` shows them at a pause.
>
> **THE BOARD 2026-09-14 (World/step9/THE_LOOP.md "THE BOARD — item 10's build").** The window over the one database: `python3
> step9/world_board.py` serves http://127.0.0.1:8765/ read-only; `python3 step9/world_stepper.py --board` beside it and the page's
> Next and Auto-play (Stop) step the engine, which waits between presses (2026-09-15, D31-D33; `--by verse --pace 1` instead for a
> hands-free watch). Names: the registry's `en`, then `step9/board_names.yaml`; `step9/world_board.py --gate`; `step9/drive_probes.py`.
>
> **MERGED 2026-09-14 (D7'S MERGE; World/step9/THE_LOOP.md "D7'S MERGE — ONE DATABASE").** `world.sqlite` in this folder is gone. THE ONE
> DATABASE is `World/journal/data/world.sqlite` — the journal's index: L0 the operators, L1 THE FOLD (this folder's world, one row per item),
> L2 the cases, L3 the runs — and the tables below are VIEWS over it with their old names (`World/journal/fold_views.sql`; the fold's
> events are `fold_events`). `python3 build_world.py` builds the layer, reindexes, creates the views and reconciles; `--check` reconciles
> alone; `python3 ask.py …` answers over the one database. `run_genesis.py` is retired — the player is `step9/world_stepper.py`.
> The rules below (read-only over the corpus; never invent a row; reconcile against the fold) are unchanged.

# World

**This is where the world gets built.** It stands on its own.

It is not part of `Torah_Grok` and not part of anything grok made. It reads the
frozen corpus **read-only** and never writes back to it. Delete `world.sqlite`
and rebuild whenever you like — nothing here is precious, and nothing here can
damage the evidence.

```bash
cd <world-link>
python3 build_world.py          # compile the corpus + reconcile
python3 build_world.py --check  # reconcile only
python3 ask.py                  # the question list
```

## The rule this place runs on

The frozen YAMLs, the fold and the state hash are **evidence** — immutable,
owner-gated, stamped. Everything in this folder is a **model** — freely
rewritable, allowed to be wrong, allowed to be thrown away.

The one hard boundary: **the world never writes back to the corpus, and never
invents data.** Every row it holds cites the operator that produced it. When
the world finds something, it produces a finding for a human, not an edit.

Every build ends with a reconciliation against `corpus_world.fold()`. If the
world and the corpus disagree, one of them is wrong and that is a finding, not
a nuisance.

## What's here

```
build_world.py     compile the corpus into world.sqlite, then reconcile
schema.sql         the shape of the world
ask.py             ask it questions
world.sqlite       the world (rebuildable, never edited by hand)
research/          measurements taken before committing to work
placement/         the location layer — not started
step9/             the law engine, the runners, the registries — the simulation's body (read step9/THE_LOOP.md)
journal/           the world journal — the append-only, hash-chained event record and its sqlite index
                   (moved here from the mockups 2026-09-09; data/ is derived and ignored; read step9/THE_LOOP.md)
```

## Current state

**Genesis, whole.** 97 units · 2,074 verses · 278 entities · 1,809 facts ·
557 events · 740 relations · 341 demands (191 open) · 905 standing facts ·
hash `8b8fff1fa28953af`.

The design principle: **the creation week is a special case, not the template.**
No `heavens`/`earth` tables, no `day` axis. The spine is `refs` — every verse in
one order — and `ord` is the world clock. Any state question is "as of ord N".

## What it answers that a ledger cannot

```bash
python3 ask.py names              # every entity that was renamed, and when
python3 ask.py called jacob       # yaaqov → yisrael, with the verse
python3 ask.py at Gen.32.29       # the world as of a verse
python3 ask.py open Gen.30.24     # what is still unresolved at that moment
python3 ask.py career joseph      # one entity's whole life, in order
python3 ask.py entities           # the cast, by weight
python3 ask.py sql "SELECT ..."   # anything
```

## Known gaps

- **No geography.** The corpus records speech and lineage; movement is almost
  absent. "Jacob went down to Egypt" is not in the machine. This is what
  `placement/` is for — see `research/VERB_REVIEW.md`.
- **`relations` covers events, namings and demands only.** Kinship, ownership,
  covenant and debt still sit inside `facts` payloads as text.
- **Simultaneous namings serialise awkwardly** — Genesis 31:47 gives one heap
  two names in two languages at once.
- **No law modules.** Dispatching a case to a compiled machine is a later layer.

## Eventual scope

The whole Hebrew Bible. Genesis only for now, because Genesis is the only book
derived end to end.
