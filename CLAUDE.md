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

Five gates, one exit code: the gloss lint, the 97 derivation units, the
chapter machine with its 60-edge dependency proof, the 64 Tanakh-run
scenes against their frozen stamp baseline
(`app/scene_stamps_baseline.json`), and the simulation sketch. Run it
before and after any change. A change that flips a scene stamp must
answer for it; only after it has answered, re-freeze deliberately with
`python3 tools/check.py --rebaseline`. CI runs the same command on every
push (`.github/workflows/check.yml`).

Individual instruments: `python3 app/app.py` (the 64 scenes, port 8021),
`python3 machines/exo21/chapter.py`, `python3 units/run_all.py`,
`python3 sim/house_of_david.py`, `open viz/inheritance.html`,
`python3 -m http.server 8012 -d scroll` (the Torah as a scroll — static,
whole Torah, with the 97 derivation review pages under `scroll/units/`).

## The public site — torahsim.org

The site is served publicly at **torahsim.org** as a static export on
Cloudflare Pages (project `torahsim`; torahsim.com 301-redirects to
.org at the zone level). The front door is **Epic Disclosure** —
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
  stranger with one command. Never add a package.
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
- `shelf/` (~2.7 GB) is an uncommitted, rebuildable source cache —
  `tools/fetch_*.py` per `docs/SOURCES.md`. `BriansTemp/` is private
  scratch — never commit it and never promote its content.
- A new chapter clones the `machines/exo21/` pattern: scan ledger →
  claim manifests → block machines → assembled chapter with its own
  dependency proof, then its scenes join the Tanakh run.

## Voice

Docs and commit messages are long-form literary prose — read `git log`
before writing either. Divergences and misses are reported at the same
size as confirmations. The project name is TorahSim, settled; do not
rename anything.
