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
