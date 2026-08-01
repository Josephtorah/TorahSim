# Resume prompt — Cain's line next; two drafts at the gate · 2026-08-01

Paste the block below into the compacted session to resume exactly where we
left off.

---

Continue work on Torah_Grok (private GitHub `Josephtorah/Torah_Grok`, on
**main**, last commit e955ff5 — the gen_09 + gen_10 freeze). Local dev
server: `python3 dev_server.py` (port 8011; one may already be running).

**ABSOLUTE RULE (memory: chat-hebrew-glossing, owner order):** NEVER
reference Hebrew anywhere — script, transliteration, OR Hebrew-derived
jargon (wayyiqtol = "and-then-he-did" narrative form, weqatal =
"and-he-shall-do" law form, middot = "measures"/interpretive rules) —
without its English counterpart inline. Every time. All outputs: chat,
files, commits, comments. This rule is now also CODE: the stepper
(step_unit.py) and the unit-page renderer share a gloss engine — keep
them in sync.

**State: ELEVEN units FROZEN and green** (gen_01..gen_10 — creation
week + Eden complete, Gen 1:1-3:24 gapless — plus lev_13_intake_
quarantine). **TWO DRAFTS GREEN AT THE OWNER'S FREEZE GATE:**
- `gen_11_sentences_exile` (Gen 3:14-24) — first curses (ASSIGN's
  negative pole vs 2:3's holiness), the enmity PATTERN, the
  HANDLER-DELTA flag (armed in-the-day death answered by
  mortality-as-boundary — the corpus's oldest open question as machine
  state), the office split (work->human, guard->cherubim; the
  Mishkan-root debuts stationing guards), Chavah named, skin garments.
- `gen_12_cain_abel` (Gen 4:1-16) — solo-YHWH's first token in the
  MOTHER's mouth; the corpus's first IF (two HANDLERs: se'et/uplift vs
  CHATTAT crouching); the 3:16 pair re-aimed at sin as a LET? pushed
  at 4:7 and VIOLATED at 4:8 (never popped — the queue's standing debt
  is now THREE with gen_08's two); the empty quote (nothing invented);
  the first death = fratricide (harag's whole debut); the first lie +
  keeper-question; bloods-plural [OPEN]; curse #3 (first human); the
  sevenfold HANDLER + the mark; settled in Wandering east of Eden.
  ZERO interpreter extensions for BOTH (2nd and 3rd extension-free
  derivations) — freeze = flip status + re-verify + regression, no
  run_unit.py changes.

**UNCOMMITTED work pile (on disk, safe across compaction — awaiting
owner's commit order):** the two draft unit YAMLs;
WATCHLIST_gen11/gen12_prospective_2026-08-01.md; FETCHLOG entries
(Onkelos Gen 3:14-24 x11 + Gen 4:1-16 x16); WEB APP upgrades —
web/scroll/index.html (frozen badge = switch button to the unit page;
"units" index button; hash deep-links #Gen/3/1 via gotoRef),
dev_server.py (regen chain += render_coverage_index.py — needs server
restart to take effect), logic/pre_logic_methods_2026-07-28/
render_coverage_index.py (NEW: UNIT_INDEX.html — coverage meters +
canonical table), render_unit_html.py (switch links "verse view"/"all
units" + FULL GLOSSING: machine-expression twins, anchor-column
word-glosses, scenario glosses, tree linear lines — imports
step_unit's gloss engine), step_unit.py (gloss dictionary expanded);
12 stable-named UNIT_<uid>.html pages + UNIT_INDEX.html (derived
artifacts; the old dated gen_01-05 pages remain tracked separately).

**Read these first, in order:**
1. `logic/units/gen_12_cain_abel.yaml` + `gen_11_sentences_exile.yaml`
   — the two drafts at the gate (format, the quote-diff and
   handler-delta devices, the violated-LET? scenario pattern).
2. `logic/units/gen_10_serpent_violation_trace.yaml` — freshest frozen
   (the quote-diff baseline gen_11's verbatim-quote closes).
3. `run_unit.py` header micro-grammar — the full operator vocabulary
   (nothing new needed for the two freezes).
4. `logic/middot_scan/WATCHLIST_gen12_prospective_2026-08-01.md` — the
   prospective-run pattern + the diyyuk tripwire prediction.
5. `step_unit.py` — the verse stepper (spacebar; full glossing; the
   gloss engine the web renderer imports).

**TASK 1 — owner's gates, in their order:** (a) freeze gen_11 + gen_12
on owner order (flip status, re-verify, regression-run all frozen
units — no interpreter edits) and commit/push the pile above when
ordered; (b) then derive **gen_13 = Gen 4:17-26** (Cain's line and
Seth), same ritual (prospective watch-list FIRST -> DB morph dump ->
DB trees -> Onkelos Tier-A sequential 0.5s FETCHLOG -> full YAML ->
pre-flight -> gate). Expected content to verify from DB at derive
time: the WANDERER BUILDS THE FIRST CITY (ir's first token, named for
Enoch — the letter's irony after eretz-Nod); seven generations of
Cain's line; the first POLYGAMY (two wives, Adah/Tzillah); the CRAFTS
REGISTRY (Yaval herds/tents, Yuval music, Tuval-Kayin bronze-and-iron
smithing — the civilization installs, avi "father-of" as office
formula); **LAMECH'S BOAST — the 4:15 protective handler QUOTED AND
INFLATED (sevenfold -> seventy-seven: quote-diff device #2, vengeance
arithmetic running away; the sword-song is verse — expect the
near-poetic accents)**; Seth ("God has SET me another seed" — the
shat root echoing 3:15's ashit 'I will set'; tachat Hevel "in place
of Abel" — the first replacement semantics); Enosh; and the close:
az huchal likro be-shem YHWH ("then calling on the NAME of YHWH was
begun" — huchal [OPEN]: begun vs profaned, the chalal ambiguity —
the chain's famous split, named-only).

**TASK 2 — standing queue (all owner-gated):** triages owed — days
6-7, lev_13 (the legal-device tripwire: Sifra Tazria + Mishnah
Negaim), gen_08 (Sanhedrin 56b — seven laws from 2:16), gen_09
(Sanhedrin 58a via Onkelos's bed-chamber), gen_10 (ADRN 1 the fence;
Sanhedrin 29a whoever-adds-subtracts), gen_11 (BR 20:12 garments of
LIGHT — al-tikrei class), gen_12 (Mishnah Sanhedrin 4:5
bloods-plural — diyyuk class); days 2-3 triage backfill; narratives
for everything since day 5 (ASK OWNER FIRST, each one); the PUBLIC
REPORT (owner emphasis pass pending); middot v2; Stage E linker (the
cross-unit firing gen_10/11/12 keep deferring to); repo-tools
proposal pending owner decision (permanent preflight template +
fetch_onkelos_span.py — cuts ~6-8 min/unit and survives compaction);
gen_boot Eden/Cain Python renderings (owner offered-to, not ordered).

**State notes:** dev server on 8011 may be the OLD process (restart
to pick up the regen-chain addition). Web entry points:
`/units/UNIT_INDEX.html` (coverage index), `/#Gen/3/1`-style deep
links, frozen badges = switch buttons. The stepper:
`python3 step_unit.py <unit_id> [...]` (frozen only). DB snapshot
torah_grok.SNAPSHOT-main-51801ca.sqlite still held (gitignored).
Onkelos cache now covers Gen 1:1-4:16 + Lev 13:1-8 (gitignored;
FETCHLOG is provenance). TEMP_return_to_main file: deletable on
owner order.

**Standing rules (non-negotiable):** Pre-Code (logic hand-authored in
frozen YAML; code only interprets; flags never auto-resolve;
dual-track, never merge). Freeze/amend/narrative gates: owner order
only (narratives: ASK FIRST each time). Hebrew ALWAYS glossed in
English — absolute, everywhere, forever. Oral: named location only;
verified from local corpus; tier per the APPROVED provenance register
(material = chain_primary only); machine never derives law (ein adam
dan me-atzmo — "one may not derive on his own"). Sefaria: sequential,
0.5s, small ranges, EVERY fetch logged in Data/FETCHLOG.md. Commit
trailer: `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`.
Repo PRIVATE (Sefaria licensing). gh account Josephtorah.
Disclosure/ + reviews/architecture/NARRATIVE_theory_of_disclosure_
intro are the owner's own docs — NEVER commit them.
