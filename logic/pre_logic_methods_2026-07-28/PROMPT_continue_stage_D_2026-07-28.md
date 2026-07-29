# Resume prompt — Stage D (interpreter) · saved 2026-07-28

Paste the block below into a fresh/compacted session to resume exactly where we left off.

---

Continue work on Torah_Grok (this repo, private GitHub Josephtorah/Torah_Grok, clean at `964281e`).

**Read these first, in order:**
1. `logic/pre_logic_methods_2026-07-28/PLAN_fullstack_architecture_2026-07-28.md` — architecture + roadmap §8 with stage status markers
2. `logic/units/gen_01_creation_boot.yaml` — the frozen Stage C pilot unit (Gen 1:1–5): operator lines, machine-state scenarios S1–S7
3. `logic/TREE_INTERPRETATION_RULES.md` — TIR-026…033 (owner-approved verb-form → operator rules)
4. `reviews/STANDING_DECISIONS.md` §6c — the standing record of those rules

**State:** Stage A ✅ (versioned `logic/lexicon/` v1 + `logic/role_rules/` v1 with goldens; SQLite index `torah_grok.sqlite` — derived/gitignored, rebuild via `python3 build_db.py` ~7 min, then `index_units.py` + `index_oral.py`). Stage B ✅ (TIR-026–033 merged). Stage C ▶ pilot done (`gen_01_creation_boot` frozen, `status: frozen`, reindexed clean).

**Task — Stage D: build `run_unit.py` (repo root).** The dry-run machine as a program:
- Registers: TIME, WORLD, REGISTRY, SPECS, TESTS, LEDGER
- Loads **frozen units only** (refuse `status: draft`); executes the unit's `boot_steps[].operators` lines; asserts the `scenarios` as tests
- Contract (same as the taamim parser): code interprets, never invents; a red scenario means fix the YAML or version the rulebook — never a code hack
- **Exit criteria:** `python3 run_unit.py gen_01_creation_boot --scenarios` reproduces S1–S5 green; S6 enforced as FLAG-not-block (commit-without-test = pattern deviation, it's data); S7 enforced (LET? never auto-upgrades to LET/CMD!)

**After Stage D passes:** extend Stage C — freeze day-2…7 units (Gen 1:6–2:3) one at a time, validating each with the interpreter as it lands (day 2 exercises S6 for real; day 7 exercises the open-transaction/no-COMMIT case). Then Leviticus (casuistic decision tables). Evidence base for the week: `logic/pre_logic_methods_2026-07-28/EXPERIMENT_precode_logic_gen_1_1_to_2_3_2026-07-28.md`.

**Standing rules (non-negotiable):** Pre-Code rule — logic is authored in YAML/markdown documents, code only interprets frozen ones. Hebrew is the only derivation source; every Hebrew string gets he + translit + en (never bare Hebrew). Oral = named location only, verified against local `Data/` where possible, tier-labeled, never merged into Written. Versioned-rules discipline: errors → new version directory + goldens, never silent edits (`logic/role_rules/check_golden.py` must stay ALL GREEN). Commit only when I say commit; end git commits with the Claude co-author trailer.
