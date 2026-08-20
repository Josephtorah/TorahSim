# TorahSim

**The laws of the Hebrew Bible, as explained by its own oral tradition,
rewritten as running computer code — and tested against the rest of the
Hebrew Bible.**

One chapter has been taken to full depth: **Exodus 21**, the first chapter
of biblical civil and criminal law. Every word of the oral tradition on it
was read and logged (a 4,903-row coverage ledger), every legal claim
extracted with its source citation (117 witnessed claims), every rule
coded, every test drawn from the tradition's own worked examples. The
assembled chapter machine was then fed 64 recorded cases from all 24 books
— David and Uriah, Amaziah's measured vengeance, the kidnapping of Joseph
— and its verdicts compared with the verdicts the text itself records.

**The scoreboard: 43 CONFIRM · 5 DIVERGE · 7 FORWARD · 9 NO-VERDICT-IN-TEXT.**
Divergences are reported on the same board as confirmations. In the
sharpest case, the text says the king ruled "as it is written in the book
of the Law of Moses" — and the machine, built only from that law,
reproduces his double ruling exactly.

## What this is — and is not

The one-line scope statement this project holds itself to:
**consistency certified, agency absent.**

The machines demonstrate that the law chapter, read through its oral
tradition, forms a coherent computable system whose declared inheritances
from Genesis resolve mechanically, and whose rules agree with the recorded
verdicts of books written centuries later. The machines decide nothing the
text left undecided, generate no history, and prove no theological
proposition. This is an experimental model of a legal tradition — not
binding religious law, and not a substitute for studying the sources.

## Run it (stock Python 3, nothing to install)

```
python3 tools/check.py                # every gate, one exit code — the green button
python3 app/app.py                    # the Tanakh run — open http://127.0.0.1:8021
python3 machines/exo21/chapter.py     # the chapter machine: asserts + 60-edge proof
python3 units/run_all.py              # re-prove all 97 derivation units
python3 sim/house_of_david.py         # the simulation sketch
open viz/inheritance.html             # the inheritance flow (any browser)
python3 -m http.server 8012 -d scroll # the Torah as a scroll — http://127.0.0.1:8012
```

Everything is self-contained — the Hebrew text, word tags, and English
glosses ship in `data/`. Every Hebrew word anywhere in this repository
carries its English inline (enforced by `tools/gloss_lint.py`).

## Where to start

1. **`docs/PROCESS_OVERVIEW.md`** — the premise (the Written Torah, the
   Oral Torah, and the chain of transmission as given inputs) and the
   eight-step pipeline from full-coverage scan to Tanakh-wide test run.
2. **`docs/CHAIN_OF_TRANSMISSION.md`** — the works this project computes
   with, listed in order: the Written Torah through the Mishnah, the
   Talmuds, and the later codes. The chain is the citation graph of the
   code.
3. **`docs/METHOD_LAWS.md`** — the nine binding rules (full inversion,
   witnessed claims only, disputes-are-data, no invented events, ...).
4. **The app** (`app/`) — run the 64 scenes yourself.
5. **The visualizer** (`viz/`) — which Genesis verse feeds which law,
   click-through to verse and code.

## Repository map

```
docs/       process overview · chain of transmission · method laws ·
            source manifest · simulation roadmap · the Ark and the
            Book (every Ark verse read through the project's lens)
data/       tanakh.sqlite (Hebrew Bible + word tags) · lexicon.json
            (English gloss layers) · units_index.json (the 97 units)
machines/   the Exodus 21 block machines + the assembled chapter, with
            the 60-edge dependency proof
logic/      the canonical derivation layer: the 97 frozen unit YAMLs
            (Pre-Code — the plate the prints are struck from), schema,
            gloss overrides, rule sets, world config, and the received
            method records (see logic/README.md)
press/      the derivation press: interpreter, renderers, bundle
            exporter, world fold, database build chain, and the
            authoring gates — TorahSim reprints everything it ships
units/      97 runnable derivation units, Genesis 1 – Exodus 21
            (printed from logic/units/ by the press; the sixth gate
            re-proves the match on every check)
scans/      the evidence layer: coverage ledger · 100 witnessed-claim
            manifests · the scanning-day notes
app/        the Tanakh-run web app (64 scenes, forms, replay)
scroll/     the Torah as a scroll: the whole Torah verse by verse —
            leaves, morphs, roles, search — with the 97 derivation
            review pages under scroll/units/
viz/        the inheritance visualizer
sim/        the simulation sketch + its findings
tools/      the source-shelf fetchers and the whole-work corpus mirror
            (to continue deriving) · the gloss linter · the check
            battery (every gate, one exit code) · the static-site
            exporter behind torahsim.org
```

To **continue the derivation work** — scan and code new chapters — see
`docs/SOURCES.md`: the fetchers in `tools/` build you a local shelf of
the oral-law sources, block by block.

## License and attribution

Code: MIT. Documentation, scan records, and project data: CC BY 4.0.
Third-party data (the Hebrew text and its tags) carries its own open
terms — see `LICENSE` and `ATTRIBUTION.md`.
