# CLAUDE.md — working rules for this repository

TorahSim rewrites the laws of the Hebrew Bible, as explained by its oral
tradition, into running Python, and tests that code against the recorded
cases of the rest of the Hebrew Bible. Before touching any law code, read
`docs/PROCESS_OVERVIEW.md` (the eight-step pipeline) and
`docs/METHOD_LAWS.md` (the nine binding rules). The rules are not
aspirations — each is enforced by a mechanical gate, and a violation
blocks shipping.

## The one green button

```
python3 tools/check.py
```

Seven gates, one exit code: the gloss lint, the 97 derivation units, the
chapter machine with its 60-edge dependency proof, the 64 Tanakh-run
scenes against their frozen stamp baseline
(`app/scene_stamps_baseline.json`), the simulation sketch, the receipts
(the reading ledger's 4,903 rows and the census queues' counts, asserted
against their documented figures), and the press (the 97 unit renderings
reprinted from the canonical YAML in `logic/units/` and diffed against
`units/` — skipped with a note when `data/derivation.sqlite` is absent,
as on CI). Run it before and after
any change. A change that flips a scene stamp must answer for it; only
after it has answered, re-freeze deliberately with
`python3 tools/check.py --rebaseline`. CI runs the same command on every
push (`.github/workflows/check.yml`).

Individual instruments: `python3 app/app.py` (the 64 scenes, port 8021),
`python3 machines/exo21/chapter.py`, `python3 units/run_all.py`,
`python3 sim/house_of_david.py`, `open viz/inheritance.html`.

The derivation loop's preview is `python3 tools/dev_server.py` (port
8012): it serves the dressed `site/` exactly as Cloudflare ships it, and
answers the pages' hidden ⟳ regenerate buttons — `/regen/data` re-runs
the index → export → re-dress chain, `/regen/unit/<uid>` reprints one
unit's rendering and review page. Loopback-only, fixed script allowlist,
derived artifacts only (it can never touch `logic/`); production answers
404 on `/regen/ping`, so the buttons never appear on the public site.

## The public site — torahsim.org

The site is served publicly at **torahsimulation.org** as a static
export on Cloudflare Pages (project `torahsim`; torahsimulation.com,
torahsim.org, and torahsim.com all 301-redirect to it at the zone
level). The front door is **Epic Disclosure** —
`Disclosure/Epic_Disclosure.md` is the canonical text, rendered to the
root page by the exporter's own markdown converter. The Tanakh-run app
lives at **/run/** and the scroll reader at **/scroll/**. The export is
built by `tools/export_site.py` into `site/` (gitignored, generated):
every scene, verse, replay event, and custom-forms result is a real
machine call frozen at build time — free-typed parameters become
curated value lists so the whole space precomputes. To publish a
change:

```
python3 tools/check.py                 # green first, always
python3 tools/export_site.py
CLOUDFLARE_API_TOKEN=$(cat ~/.cf_torahsim_token) \
CLOUDFLARE_ACCOUNT_ID=aeb8d0762c9df149269eb78fdbd6a0ac \
  npx -y wrangler@latest pages deploy site --project-name torahsim
```

The token file lives outside the repo; never commit or echo it.

## Rules that bind every contribution

- **Stock Python 3, zero dependencies.** Everything must run for a
  stranger with one command. Never add a package. One vendored
  exception, owner-approved 2026-08-20: PyYAML rides in
  `press/vendor/yaml/` (pure-Python, MIT, license included) so the press
  can read the canonical YAML — nothing to install, the one-command rule
  holds.
- **Witnessed claims only.** No constant, branch, or rule enters a
  machine without a claim ID citing a source in the chain of
  transmission (`docs/CHAIN_OF_TRANSMISSION.md`).
- **Disputes are data, never decisions.** Where the sources disagree —
  a machloket ("division," a recorded dispute) — the code returns both
  positions as a fork. Never silently pick a side.
- **The tests are the tradition's own worked examples.** Never invent a
  test case for the law; transcribe one, with its citation.
- **No invented events — ever.** The simulation computes law over the
  text's own events; it never generates history.
- **Hebrew never appears without English.** Every Hebrew word or phrase,
  in any shipped file, carries an inline English gloss —
  `tools/gloss_lint.py` enforces it. The preserved records — the scan
  records under `scans/` and the derivation review pages under
  `scroll/units/` — are the declared exception: reported, never gated,
  never retouched.
- **Scope honesty.** The standing summary is "consistency certified,
  agency absent." The machines decide nothing the text left undecided
  and prove no theological proposition; never write a claim past that.

## Layout and invariants

- Unit IDs and file paths are load-bearing — the dependency proof
  resolves against them. Never rename `units/*.py`; never move
  `machines/`.
- `scans/` is the evidence layer, shipped exactly as written during the
  scans. Never retouch a ledger, manifest, or note.
- `logic/` is the canonical derivation layer (since 2026-08-20): the 97
  frozen unit YAMLs, the schema, gloss overrides, rule sets, the world
  config, and the received records (method docs, triage ledgers, fetch
  log — preserved, never retouched; see `logic/README.md` for the
  documented border redaction). Editing a frozen YAML is derivation
  work, not maintenance.
- `press/` is the toolchain that prints everything from `logic/`: the
  Stage D interpreter (`run_unit.py`), the renderers (`render_unit_py.py`
  → `units/`, `render_unit_html.py` → the review pages), the scroll
  bundle exporter (`export_web.py`, byte-reproduces `scroll/data/`), the
  world fold (`corpus_world.py`), the database build chain
  (`build_db.py` → `index_units.py` → `index_triage.py`), and the
  authoring gates in `press/gates/` (preflight, lints, the freeze
  ritual). Run press tools from the repo root.
- `shelf/` (~5.5 GB with `shelf/sources/`) is an uncommitted, rebuildable
  source cache — `tools/fetch_*.py` per `docs/SOURCES.md`. The press
  databases (`data/derivation.sqlite`, rebuildable; the two pinned
  snapshots, back them up) are uncommitted the same way. `BriansTemp/` is
  private scratch — never commit it and never promote its content.
- A new chapter clones the `machines/exo21/` pattern: scan ledger →
  claim manifests → block machines → assembled chapter with its own
  dependency proof, then its scenes join the Tanakh run.

## Voice

Docs and commit messages are long-form literary prose — read `git log`
before writing either. Divergences and misses are reported at the same
size as confirmations. The project name is TorahSim, settled; do not
rename anything.
