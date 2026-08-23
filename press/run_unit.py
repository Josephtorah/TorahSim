#!/usr/bin/env python3
"""
run_unit.py — Stage D interpreter: the dry-run machine as a program.

Contract (same as taamim_tree_parse.py):
  * Code INTERPRETS frozen documents; it never invents logic (Pre-Code rule,
    logic/SYSTEM.md / AGENTS.md).
  * Loads units with meta.status: frozen ONLY. Drafts are refused.
  * Executes boot_steps[].operators against six registers:
      TIME / WORLD / REGISTRY / SPECS / TESTS / LEDGER   (+ FLAGS side channel)
  * Asserts the unit's own scenarios. A red scenario means: fix the YAML or
    version the rulebook (TIR) — never a code hack here.
  * Operator micro-grammar: this file parses ONLY notation the frozen unit
    already uses:  WORLD += {a, b} · HOLDS(p, tN) · INVARIANT(p) during tN ·
    DECLARE(x, LET(exists(y))) · DECLARE(x, CMD-US?(make(y), ..)) —
    the CMD-US mood family added at the gen_06 freeze (TIR-033; coded
    imperfect => TIR-028's mandatory ?) · { P: .. } op { Q: .. } · PASS(a, b) ·
    between(a, b) · name(x) := y · REGISTRY: x->role (ASSIGN) ·
    BLESS(s, r) [MANDATE {..}] — the mandate clause made OPTIONAL at the
    gen_07 freeze (2:3 blesses a day with no quoted speech) ·
    CASE(..) ROUTE(x) and HANDLER IF(..) THEN(..) — the LAW-GENRE installers
    added at the lev_13 freeze (2026-08-01): the ki ("when") case-opener and
    the weqatal ("and-he-shall-do", TIR-029) chains, recorded as STANDING
    WORLD FACTS (the BLESS-mandate precedent) — the law installs; only
    cases execute · SECTION(label, ..) — the toledot ("generations")
    section-header device added at the gen_08 freeze (2026-08-01): a header
    labels, it installs NOTHING (event only, zero register writes) ·
    PATTERN(p) — the narrator's al-ken ("therefore") etiology added at the
    gen_09 freeze: a standing generalization in law grammar with no trigger
    and no addressee — a WORLD fact, not a handler · PASS(a, b) | FAIL(a, b)
    — the TEST verdict FAIL added at the gen_09 freeze (Gen 2:18 lo-tov:
    the week's instrument firing negative; verdicts are data, never blocks) ·
    LEDGER[day N] := {..} · t0 := x.
    Any operator kind outside the dispatch table is a rulebook gap: hard stop.
  * Negative contracts:
      S6 — COMMIT with empty TESTS => FLAG pattern deviation, never block
           (day 2 commits without a test; the flag is data, not an error).
      S7 — LET? never auto-upgrades to LET/CMD! (TIR-028); an upgrade requires
           an explicit per-unit citation or the run fails validation. The same
           guard covers EVERY ?-mood (CMD-US? since gen_06).
      S10 (gen_08) — LET-NOT has NO resolution path at all: it is not a
           ?-mood, so resolve_spec refuses outright, citation or none — no
           path exists that flips a prohibition (lo + imperfect in a command
           frame, TIR-034) into a permission. First firing: Gen 2:17.

Usage:
  python3 run_unit.py gen_01_creation_boot --scenarios
  python3 run_unit.py gen_01_creation_boot --trace
"""

import argparse
import re
import sys
from pathlib import Path

import sys as _vsys; from pathlib import Path as _VP; _vsys.path.insert(0, str(_VP(__file__).resolve().parent / "vendor"))
import yaml

ROOT = Path(__file__).resolve().parents[1]
UNITS_DIR = ROOT / "logic" / "units"


class ContractError(Exception):
    """The unit (or a caller) asked for something the contract forbids."""


# ---------------------------------------------------------------------------
# The machine: six registers + FLAGS side channel
# ---------------------------------------------------------------------------

class Machine:
    def __init__(self):
        self.TIME = {"t0": None, "marks": []}
        self.WORLD = {"entities": {}, "facts": [], "invariants": [], "partitions": [],
                      "witnessed": {}}
        self.REGISTRY = {"names": {}, "writes": 0}
        self.SPECS = {"queue": [], "log": []}
        self.TESTS = []
        self.LEDGER = {}
        self.FLAGS = []
        self.EVENTS = []
        self.TRIPLES = []
        self.UTTERANCES = []
        self.UTTERANCES_DISPUTED = []
        self.WITNESS_READS = []
        self._step_ref = None

    # -- entity helpers ------------------------------------------------------
    def install(self, name, mode, by, step):
        ent = self.WORLD["entities"].get(name)
        if ent is None:
            self.WORLD["entities"][name] = {"mode": mode, "by": by, "step": step}
        elif ent["mode"] == "presupposed" and mode == "created":
            ent.update(mode="created", by=by, step=step)

    def created_set(self):
        return {n for n, e in self.WORLD["entities"].items() if e["mode"] == "created"}

    def presupposed_set(self):
        return {n for n, e in self.WORLD["entities"].items() if e["mode"] == "presupposed"}

    def flag(self, kind, detail):
        self.FLAGS.append({"kind": kind, "detail": detail, "step": self._step_ref})

    def event(self, verb, agent=None, themes=()):
        self.EVENTS.append({"verb": verb, "agent": agent,
                            "themes": list(themes), "step": self._step_ref})

    def events_in_step(self, ref):
        return [e for e in self.EVENTS if e["step"] == ref]

    # -- S7 guard: the ONLY path that changes a LET? mood ---------------------
    def resolve_spec(self, demand, new_mood, cite=None):
        # generalized at the gen_06 freeze: EVERY ?-mood (LET?, CMD-US?)
        # refuses upgrade without a per-unit citation — TIR-028's contract
        for entry in self.SPECS["log"]:
            if entry["demand"] == demand and entry["mood"].endswith("?"):
                if not cite and not new_mood.endswith("?"):
                    raise ContractError(
                        "TIR-028: %s never auto-upgrades to %s — a per-unit "
                        "judgment citation is required (demand: %s)"
                        % (entry["mood"], new_mood, demand))
                entry["mood"] = new_mood
                entry["resolution_cite"] = cite
                return entry
        raise ContractError("no ?-mood spec found for demand: %s" % demand)


# ---------------------------------------------------------------------------
# Operator handlers — one per op kind that appears in frozen units.
# Each parses the document's own notation; nothing else.
# ---------------------------------------------------------------------------

def h_time_anchor(m, op, step):
    mt = re.search(r"t0 := (\w+)", op.get("expr_en", ""))
    if not mt:
        raise ContractError("TIME_ANCHOR without 't0 := x' notation")
    m.TIME["t0"] = mt.group(1)


def h_event(m, op, step):
    expr = op.get("expr_en", "")
    verb = re.match(r"(\w+)\(e\d+\)", expr)
    agent = re.search(r"Agent\(e\d+,\s*([\w-]+)\)", expr)
    themes = re.findall(r"Theme\(e\d+,\s*([\w-]+)\)", expr)
    m.event(verb.group(1) if verb else "?",
            agent.group(1) if agent else None, themes)


def h_registry_install(m, op, step):
    mt = re.search(r"WORLD \+= \{([^}]*)\}", op.get("expr_en", ""))
    if not mt:
        raise ContractError("REGISTRY_INSTALL without 'WORLD += {..}' notation")
    for name in [x.strip() for x in mt.group(1).split(",") if x.strip()]:
        m.install(name, "created", "narration", step["ref"])


def h_precondition_state(m, op, step):
    for p in re.findall(r"HOLDS\((.+?),\s*t\d+\)", op.get("expr_en", "")):
        m.WORLD["facts"].append(p.strip())


def h_invariant(m, op, step):
    mt = re.search(r"INVARIANT\((.+)\)\s*during", op.get("expr_en", ""))
    if not mt:
        raise ContractError("INVARIANT without 'INVARIANT(p) during tN' notation")
    m.WORLD["invariants"].append(mt.group(1).strip())


def h_note_zero_events(m, op, step):
    fired = m.events_in_step(step["ref"])
    if fired:
        raise ContractError(
            "unit claims zero events in %s but %d fired — fix the YAML"
            % (step["ref"], len(fired)))


def h_note_presupposed(m, op, step):
    mt = re.match(r"(.+?) are READ", op.get("expr_en", ""))
    if not mt:
        raise ContractError("NOTE_PRESUPPOSED without '<list> are READ' notation")
    for name in [x.strip() for x in mt.group(1).split(",") if x.strip()]:
        m.install(name, "presupposed", "read-before-install", step["ref"])
        m.flag("read_before_install", name)


def h_declare(m, op, step):
    # CMD-US mood family added at the gen_06 freeze (TIR-033: the 1cp
    # volitive na'aseh, "let US make"; coded imperfect => mandatory ?)
    expr = op.get("expr_en", "")
    speaker = re.search(r"DECLARE\((\w+),", expr)
    if "CMD-US?(" in expr:
        mood = "CMD-US?"
    elif "CMD-US(" in expr:
        mood = "CMD-US"
    elif "LET?(" in expr:
        mood = "LET?"
    elif "LET-NOT(" in expr:
        mood = "LET-NOT"
    elif "LET(" in expr:
        mood = "LET"
    else:
        raise ContractError("DECLARE without LET/LET-NOT/LET?/CMD-US payload: %s" % expr)
    dm = re.search(r"(?:LET\??(?:-NOT)?|CMD-US\??)\((.+)\)\)", expr)
    demand = dm.group(1).strip() if dm else "?"
    entry = {"demand": demand, "mood": mood,
             "speaker": speaker.group(1) if speaker else None,
             "pushed_step": step["ref"], "satisfied_step": None,
             "resolution_cite": None}
    m.SPECS["queue"].append(entry)
    m.SPECS["log"].append(entry)
    m.event("declare", entry["speaker"], [demand])


def h_triple(m, op, step):
    qm = re.search(r"\{\s*Q:\s*([^}]+)\}", op.get("expr_en", ""))
    if not qm:
        raise ContractError("TRIPLE without '{ Q: .. }' notation")
    m.TRIPLES.append({"q": qm.group(1).strip(), "step": step["ref"],
                      "discharged": False})


def h_result(m, op, step):
    expr = op.get("expr_en", "")
    hm = re.search(r"HOLDS\((.+?),\s*t\d+\)", expr)
    if not hm:
        raise ContractError("RESULT without 'HOLDS(q, tN)' notation")
    q = hm.group(1).strip()
    tm = re.search(r",\s*(t\d+)\)", expr)
    if tm:
        m.TIME["marks"].append(tm.group(1))
    # pop the matching spec (demanded-Q becomes holds-Q; mood untouched — TIR-028)
    for entry in list(m.SPECS["queue"]):
        if entry["demand"] == q:
            entry["satisfied_step"] = step["ref"]
            m.SPECS["queue"].remove(entry)
            break
    em = re.search(r"exists\((\w+)\)", q)
    if em:
        m.install(em.group(1), "created", "fiat-result", step["ref"])
    for tr in m.TRIPLES:
        if not tr["discharged"] and tr["q"] == q:
            tr["discharged"] = True
    m.event("result", None, [q])


def h_test(m, op, step):
    """TEST extended at the gen_09 freeze (2026-08-01): verdicts PASS and
    FAIL. The FAIL class opens at Gen 2:18 (lo-tov — the week's oracle word
    negated, in speech mode; Tier-A warrant: Onkelos la takkin = day 6's own
    verdict word negated). Verdicts are DATA: a FAIL blocks nothing."""
    mt = re.search(r"(PASS|FAIL)\((\w+),\s*(\w+)\)", op.get("expr_en", ""))
    if not mt:
        raise ContractError("TEST without 'PASS(a, b)' or 'FAIL(a, b)' notation")
    m.TESTS.append({"oracle": mt.group(2), "theme": mt.group(3),
                    "verdict": mt.group(1), "step": step["ref"]})


def h_event_partition(m, op, step):
    mt = re.search(r"between\(([\w-]+),\s*([\w-]+)\)", op.get("expr_en", ""))
    if not mt:
        raise ContractError("EVENT_PARTITION without 'between(a, b)' notation")
    m.WORLD["partitions"].append((mt.group(1), mt.group(2)))
    m.event("divide", None, [mt.group(1), mt.group(2)])


def h_note_spec_delta(m, op, step):
    mt = re.search(r"spec '(.+?)' delivered '(.+?)'", op.get("expr_en", ""))
    if not mt:
        raise ContractError("NOTE_SPEC_DELTA without \"spec '..' delivered '..'\" notation")
    m.flag("spec_delta", "spec '%s' -> delivered '%s'" % (mt.group(1), mt.group(2)))


def h_name(m, op, step):
    pairs = re.findall(r"name\(([\w-]+)\)\s*:=\s*(\w+)", op.get("expr_en", ""))
    if not pairs:
        raise ContractError("NAME without 'name(x) := y' notation")
    for ent, label in pairs:
        if ent not in m.WORLD["entities"]:
            m.flag("named_before_any_presence", ent)
        m.REGISTRY["names"][ent] = label
        m.REGISTRY["writes"] += 1
        m.event("name", None, [ent, label])


def h_assign(m, op, step):
    """ASSIGN (introduced gen_04, 2026-07-30): dative role/office binding —
    a REGISTRY write distinct from NAME (no va-yiqra formula). Notation:
    'REGISTRY: entity->role[, entity->role]'."""
    pairs = re.findall(r"([\w-]+)->([\w-]+)", op.get("expr_en", ""))
    if not pairs:
        raise ContractError("ASSIGN without 'entity->role' notation")
    for ent, role in pairs:
        if ent not in m.WORLD["entities"]:
            m.flag("assigned_before_any_presence", ent)
        m.REGISTRY["names"][ent] = role
        m.REGISTRY["writes"] += 1
        m.event("assign", None, [ent, role])


def h_bless(m, op, step):
    """BLESS (introduced gen_05, 2026-07-30): benediction speech act — the
    corpus's first second-person address. Mandate items are recorded as
    STANDING WORLD FACTS, never pushed to SPECS: the text provides no receipt
    for them (their horizon exceeds the unit) and still commits the day
    clean — a SPECS push would falsify that. The MANDATE clause was made
    OPTIONAL at the gen_07 freeze (2026-07-31): Gen 2:3 blesses the seventh
    day with NO quoted speech — the mandate was a parameter of the day-5/6
    blessings, not the operator's essence. Notation:
    'BLESS(speaker, recipients) [MANDATE {item, item, ..}]'."""
    expr = op.get("expr_en", "")
    sp = re.search(r"BLESS\((\w+),\s*([\w-]+)\)", expr)
    if not sp:
        raise ContractError(
            "BLESS without 'BLESS(speaker, recipients)' notation")
    mt = re.search(r"MANDATE \{([^}]*)\}", expr)
    items = [x.strip() for x in mt.group(1).split(",") if x.strip()] if mt else []
    for item in items:
        m.WORLD["facts"].append("mandate: %s" % item)
    m.event("bless", sp.group(1), [sp.group(2)] + items)


def h_case(m, op, step):
    """CASE (introduced lev_13, 2026-08-01): the law genre's ki ('when')
    case-opener — an intake filter + routing clause, recorded as a standing
    WORLD fact. The law installs; only cases execute. Notation:
    'CASE(subject, filter) ROUTE(destination)'."""
    expr = op.get("expr_en", "")
    mt = re.search(r"CASE\((.+)\)\s*ROUTE\(([\w-]+)\)", expr)
    if not mt:
        raise ContractError("CASE without 'CASE(..) ROUTE(..)' notation")
    m.WORLD["facts"].append("case: %s -> %s" % (mt.group(1).strip(), mt.group(2)))
    m.event("case_installed", None, [mt.group(2)])


def h_handler(m, op, step):
    """HANDLER (introduced lev_13, 2026-08-01): the weqatal chain
    ('and-he-shall-do', TIR-029) — IF(predicates) THEN(actions), recorded as
    a standing WORLD fact (the day-5 BLESS-mandate precedent: standing
    directives with horizons beyond the unit are facts, never SPECS).
    Handlers are installed, never executed — no receipt is owed because
    nothing was demanded of the narrative present. Notation:
    'HANDLER IF(..) THEN(..)'."""
    expr = op.get("expr_en", "")
    mt = re.search(r"HANDLER IF\((.+)\) THEN\((.+)\)", expr)
    if not mt:
        raise ContractError("HANDLER without 'HANDLER IF(..) THEN(..)' notation")
    m.WORLD["facts"].append("handler: IF(%s) THEN(%s)"
                            % (mt.group(1).strip(), mt.group(2).strip()))
    m.event("handler_installed", None, [mt.group(1).strip()[:40]])


def h_pattern(m, op, step):
    """PATTERN (introduced gen_09, 2026-08-01): the narrator's al-ken
    ('therefore') etiology — a standing generalization in law grammar
    (imperfect + weqatal, TIR-029) with NO trigger clause and NO addressee:
    not a HANDLER (nothing fires it), not a demand (nothing is owed) — a
    standing WORLD fact. First token: Gen 2:24 (leave-cleave-one-flesh).
    Notation: 'PATTERN(p)'."""
    mt = re.search(r"PATTERN\((.+)\)", op.get("expr_en", ""))
    if not mt:
        raise ContractError("PATTERN without 'PATTERN(p)' notation")
    m.WORLD["facts"].append("pattern: %s" % mt.group(1).strip())
    m.event("pattern_installed", None, [mt.group(1).strip()[:40]])


def h_statute(m, op, step):
    """STATUTE (introduced lev_19, 2026-08-07, the probe wave's apodictic
    operator): the law-code's direct standing directive — addressee-bound
    (the frame's distribution list), NO trigger clause: not a HANDLER
    (no IF fires it), not a PATTERN (it binds someone), not a demand (the
    law frame re-types decree grammar and jussive alike — the lev_13
    ki-retyping extended to the relay frame; letter witness Lev 19:4:
    el-jussive and lo-imperfect coordinated in ONE prohibition list).
    Recorded as a standing WORLD fact; installed, never executed.
    Notation: 'STATUTE FORBID(x)' / 'STATUTE BIND(x)'."""
    mt = re.search(r"STATUTE (FORBID|BIND)\((.+)\)", op.get("expr_en", ""))
    if not mt:
        raise ContractError("STATUTE without 'STATUTE FORBID(x)/BIND(x)' notation")
    m.WORLD["facts"].append("statute: %s(%s)" % (mt.group(1), mt.group(2).strip()))
    m.event("statute_installed", None, [mt.group(2).strip()[:40]])


def h_section(m, op, step):
    """SECTION (introduced gen_08, 2026-08-01): the toledot ('generations')
    section-header device — first of 13 in Genesis at Gen 2:4, the corpus's
    own table of contents. A header LABELS; it installs nothing: the handler
    records an event only — zero register writes (contrast REGISTRY_INSTALL).
    Notation: 'SECTION(label, member, member)'."""
    mt = re.search(r"SECTION\((\w+),\s*(.+)\)", op.get("expr_en", ""))
    if not mt:
        raise ContractError("SECTION without 'SECTION(label, ..)' notation")
    members = [x.strip() for x in mt.group(2).split(",") if x.strip()]
    m.event("section", None, [mt.group(1)] + members)


def h_commit(m, op, step):
    expr = op.get("expr_en", "")
    dm = re.search(r"LEDGER\[day (\d+)\]", expr)
    if not dm:
        raise ContractError("COMMIT without 'LEDGER[day N]' notation")
    day = int(dm.group(1))
    claims_m = re.search(r":=\s*\{([^}]*)\}", expr)
    claims = claims_m.group(1) if claims_m else ""

    spec_ok = (not m.SPECS["queue"]
               and all(e["satisfied_step"] for e in m.SPECS["log"]))
    test_pass = any(t["verdict"] == "PASS" for t in m.TESTS)
    names_n = m.REGISTRY["writes"]

    # verify the document's claims against machine state (mismatch = red)
    if "spec" in claims and not spec_ok:
        raise ContractError("day %d claims 'spec ok' but SPECS unsatisfied" % day)
    if "test PASS" in claims and not test_pass:
        raise ContractError("day %d claims 'test PASS' but TESTS has none" % day)
    nm = re.search(r"names (\d+)", claims)
    if nm and int(nm.group(1)) != names_n:
        raise ContractError("day %d claims names %s but REGISTRY writes = %d"
                            % (day, nm.group(1), names_n))

    # S6 policy: missing test is a FLAG (pattern deviation), never a block
    if not test_pass:
        m.flag("commit_without_test", "day %d cycle closed with TESTS empty" % day)

    en_note = op.get("en", "")
    label_form = ("cardinal" if "CARDINAL" in en_note
                  else "ordinal" if "ORDINAL" in en_note else None)
    m.LEDGER[day] = {"closed": True, "spec_ok": spec_ok, "test_pass": test_pass,
                     "names": names_n, "label_form": label_form,
                     "label_he": op.get("he", ""),
                     "label_translit": op.get("he_translit", ""),
                     "step": step["ref"]}


def h_oral_utterance(m, op, step):
    """ORAL_UTTERANCE — the ma'amarot ("utterances") census (Avot 5:1).
    Counted form: UTTERANCE(n, mode). Disputed form: UTTERANCE(?, disputed)
    with the positions in en — a machloket ("recorded dispute"), carried
    as data, never decided. Amendment 2026-08-20."""
    expr = op.get("expr_en", "")
    mt = re.match(r"UTTERANCE\((\d+),\s*([\w-]+)\)", expr)
    if mt:
        m.UTTERANCES.append({"n": int(mt.group(1)), "mode": mt.group(2),
                             "step": step["ref"]})
        return
    if re.match(r"UTTERANCE\(\?,\s*disputed\)", expr):
        m.UTTERANCES_DISPUTED.append({"positions": op.get("en", ""),
                                      "step": step["ref"]})
        return
    raise ContractError("ORAL_UTTERANCE expr unparsed: %r" % expr)


def h_witness_state(m, op, step):
    """WITNESS_STATE — aggadic testimony writes world state in its own
    witness-grounded tier (owner ruling 2026-08-20): entity present so
    later texts find it mechanically; never mixed into text-grounded
    facts (the tier wall is asserted at rendering)."""
    mt = re.match(r"WITNESS\(([\w-]+),\s*([\w-]+)\)", op.get("expr_en", ""))
    if not mt:
        raise ContractError("WITNESS_STATE expr unparsed: %r"
                            % op.get("expr_en", ""))
    m.WORLD["witnessed"][mt.group(1)] = {"state": mt.group(2),
                                         "cites": list(op.get("cites", [])),
                                         "step": step["ref"]}


def h_witness_read(m, op, step):
    """WITNESS_READ — the presupposed-read discipline at witness tier
    (amendment 2026-08-21): the unit reads a state another unit
    witnessed, records the read with its cites, installs nothing in
    any tier. Form: WITNESS-READ(entity, state)."""
    mt = re.match(r"WITNESS-READ\(([\w-]+),\s*([\w-]+)\)",
                  op.get("expr_en", ""))
    if not mt:
        raise ContractError("WITNESS_READ expr unparsed: %r"
                            % op.get("expr_en", ""))
    m.WITNESS_READS.append({"entity": mt.group(1), "state": mt.group(2),
                            "cites": list(op.get("cites", [])),
                            "step": step["ref"]})


HANDLERS = {
    "TIME_ANCHOR": h_time_anchor,
    "EVENT": h_event,
    "REGISTRY_INSTALL": h_registry_install,
    "PRECONDITION_STATE": h_precondition_state,
    "INVARIANT": h_invariant,
    "NOTE_ZERO_EVENTS": h_note_zero_events,
    "NOTE_PRESUPPOSED": h_note_presupposed,
    "NOTE_SPEC_DELTA": h_note_spec_delta,
    "DECLARE": h_declare,
    "TRIPLE": h_triple,
    "RESULT": h_result,
    "TEST": h_test,
    "EVENT_PARTITION": h_event_partition,
    "NAME": h_name,
    "ASSIGN": h_assign,
    "BLESS": h_bless,
    "CASE": h_case,
    "HANDLER": h_handler,
    "STATUTE": h_statute,
    "SECTION": h_section,
    "PATTERN": h_pattern,
    "COMMIT": h_commit,
    "ORAL_UTTERANCE": h_oral_utterance,
    "WITNESS_STATE": h_witness_state,
    "WITNESS_READ": h_witness_read,
}


# ---------------------------------------------------------------------------
# Loading + static validation
# ---------------------------------------------------------------------------

_TRIAGE_CACHE = []


def _triage_ledger_text():
    """The concatenated triage ledgers (logic/oral_triage/) — the record of
    every oral source actually read. Loaded once, lazily."""
    if not _TRIAGE_CACHE:
        parts = []
        tdir = ROOT / "logic" / "oral_triage"
        if tdir.is_dir():
            for f in sorted(tdir.glob("*.md")):
                parts.append(f.read_text(encoding="utf-8"))
        _TRIAGE_CACHE.append("\n".join(parts))
    return _TRIAGE_CACHE[0]


def load_unit(unit_id):
    path = UNITS_DIR / ("%s.yaml" % unit_id)
    if not path.exists():
        raise ContractError("no such unit: %s" % path)
    unit = yaml.safe_load(path.read_text(encoding="utf-8"))
    status = (unit.get("meta") or {}).get("status")
    if status != "frozen":
        raise ContractError(
            "REFUSED: unit %s has status '%s' — the interpreter loads frozen "
            "units only (SYSTEM.md Step J)" % (unit_id, status))
    return unit


def validate_unit(unit):
    """Static checks before any execution. Errors here = fix YAML or version TIR."""
    problems = []
    let_q_demands = []
    for step in unit.get("boot_steps", []):
        for op in step.get("operators", []):
            kind = op.get("op")
            if kind not in HANDLERS:
                problems.append(
                    "rulebook gap: operator '%s' in %s has no interpretation — "
                    "version the rulebook or fix the unit" % (kind, step.get("id")))
            for cite in op.get("cites") or []:
                # a cite is valid if it names a TIR catalog entry, or a
                # source actually READ in the triage ledger (amendment-era
                # rule 2026-08-20: every oral cite must be a read source)
                if not re.fullmatch(r"TIR-\d{3}", cite) \
                        and cite not in _triage_ledger_text():
                    problems.append("bad cite '%s' in %s" % (cite, step.get("id")))
            expr = op.get("expr_en", "")
            for dm in re.findall(r"LET\?\((.+?)\)", expr):
                let_q_demands.append((step.get("id"), dm))
    # S7 static: any LET? demand later written as LET(/CMD!( needs a citation
    for sid, dm in let_q_demands:
        for step in unit.get("boot_steps", []):
            for op in step.get("operators", []):
                expr = op.get("expr_en", "")
                if ("LET(%s)" % dm in expr or "CMD!(%s)" % dm in expr):
                    if not op.get("resolution_cite"):
                        problems.append(
                            "TIR-028 violation: LET?(%s) from %s upgraded in %s "
                            "without resolution_cite" % (dm, sid, step.get("id")))
    if problems:
        raise ContractError("static validation failed:\n  - " + "\n  - ".join(problems))


# ---------------------------------------------------------------------------
# Execution
# ---------------------------------------------------------------------------

def run_steps(unit, upto_step_id=None, trace=False):
    m = Machine()
    steps = sorted(unit.get("boot_steps", []), key=lambda s: s.get("order", 0))
    for step in steps:
        m._step_ref = step["ref"]
        if trace:
            print("\n%s  %s  [%s]" % (step["id"], step["ref"], step.get("op", "")))
            print("  he: %s" % step.get("he", ""))
            print("      %s | %s" % (step.get("he_translit", ""),
                                     step.get("en", "").replace("[EN-AID] ", "")))
        for op in step.get("operators", []):
            HANDLERS[op["op"]](m, op, step)
            if trace:
                cites = ",".join(op.get("cites") or []) or "-"
                print("   - %-18s %s   [%s]" % (op["op"], op.get("expr_en", ""), cites))
        if trace:
            print("  Δ WORLD=%s +presup:%d | SPECS q:%d | TESTS:%d | "
                  "REG writes:%d | LEDGER:%s | FLAGS:%d"
                  % (sorted(m.created_set()), len(m.presupposed_set()),
                     len(m.SPECS["queue"]), len(m.TESTS), m.REGISTRY["writes"],
                     sorted(m.LEDGER.keys()), len(m.FLAGS)))
        if upto_step_id and step["id"] == upto_step_id:
            break
    return m


# ---------------------------------------------------------------------------
# Scenario assertions — micro-grammar over the unit's own expect_en notation
# ---------------------------------------------------------------------------

def build_alias(unit):
    """en-aid word -> translit core, from the unit's own tree_coverage table."""
    en_pre = ("and-", "the-", "to-", "in-")
    tr_pre = ("va-", "ve-", "ha-", "la-", "be-", "u-")
    alias = {}
    for verse in (unit.get("tree_coverage") or {}).get("verses", []):
        for w in verse.get("words", []):
            en, tr = str(w.get("en", "")), str(w.get("he_translit", ""))
            changed = True
            while changed:
                changed = False
                for p in en_pre:
                    if en.startswith(p):
                        en, changed = en[len(p):], True
                for p in tr_pre:
                    if tr.startswith(p):
                        tr, changed = tr[len(p):], True
            if en and tr:
                alias.setdefault(en.lower(), tr)
    return alias


def fact_token_holds(token, facts, alias):
    """token like 'tohu' or 'darkness-over-deep': every part must appear
    (literally or via the unit's own en->translit alias) in a single fact."""
    parts = token.split("-")
    for fact in facts:
        if all(p in fact or alias.get(p.lower(), "\x00") in fact for p in parts):
            return True
    return False


def check_clause(clause, m, step_ref, alias):
    c = clause.strip().rstrip(".")
    if not c:
        return None

    mt = re.search(r"WORLD = \{([^}]*)\}", c)
    if mt:
        want = {x.strip() for x in mt.group(1).split(",")}
        got = m.created_set()
        return (got == want, "created=%s" % sorted(got))

    mt = re.search(r"TIME t0 = (\w+)", c)
    if mt:
        return (m.TIME["t0"] == mt.group(1), "t0=%s" % m.TIME["t0"])

    if re.search(r"SPECS empty", c):
        return (not m.SPECS["queue"], "queue=%d" % len(m.SPECS["queue"]))

    if "no test, no name" in c:
        ok = not m.TESTS and not m.REGISTRY["names"]
        return (ok, "tests=%d names=%d" % (len(m.TESTS), len(m.REGISTRY["names"])))

    mt = re.match(r"Facts (.+?) HOLD", c)
    if mt:
        tokens = [t.strip() for t in mt.group(1).split("/")]
        missing = [t for t in tokens if not fact_token_holds(t, m.WORLD["facts"], alias)]
        return (not missing, "missing=%s" % missing if missing else
                "%d facts" % len(m.WORLD["facts"]))

    mt = re.search(r"STATUTES (\d+) standing", c)
    if mt:
        n = sum(1 for f in m.WORLD["facts"] if f.startswith("statute:"))
        return (n == int(mt.group(1)), "statutes=%d" % n)

    mt = re.search(r"(\w+) INVARIANT active", c)
    if mt:
        ok = any(mt.group(1) in inv for inv in m.WORLD["invariants"])
        return (ok, "invariants=%s" % m.WORLD["invariants"])

    if "ZERO events fired" in c:
        n = len(m.events_in_step(step_ref))
        return (n == 0, "events_in_step=%d" % n)

    mt = re.search(r"flags (\S+) as read-before-install", c)
    if mt:
        want = [x.strip() for x in mt.group(1).split("/")]
        flagged = {f["detail"] for f in m.FLAGS if f["kind"] == "read_before_install"}
        missing = [w for w in want if w not in flagged]
        return (not missing, "flagged=%s" % sorted(flagged))

    mt = re.search(r"LET\((.+?)\) pushed then satisfied in the SAME verse", c)
    if mt:
        d = mt.group(1)
        for e in m.SPECS["log"]:
            if e["demand"] == d:
                ok = (e["satisfied_step"] == e["pushed_step"] == step_ref)
                return (ok, "pushed=%s satisfied=%s" % (e["pushed_step"],
                                                        e["satisfied_step"]))
        return (False, "no spec with demand %s" % d)

    mt = re.search(r"LET\((.+?)\) pushed and OPEN", c)
    if mt:
        ok = any(e["demand"] == mt.group(1) and not e["satisfied_step"]
                 for e in m.SPECS["queue"])
        return (ok, "queue=%s" % [e["demand"] for e in m.SPECS["queue"]])

    mt = re.search(r"LET\?\((.+?)\) mood remains LET\?", c)
    if mt:
        for e in m.SPECS["log"]:
            if e["demand"] == mt.group(1):
                return (e["mood"] == "LET?", "mood=%s" % e["mood"])
        return (False, "no spec with demand %s" % mt.group(1))

    if "machine flags commit-without-test" in c:
        ok = any(f["kind"] == "commit_without_test" for f in m.FLAGS)
        return (ok, "flags=%s" % sorted({f["kind"] for f in m.FLAGS}))

    if "machine flags spec-delta" in c:
        ok = any(f["kind"] == "spec_delta" for f in m.FLAGS)
        return (ok, "flags=%s" % sorted({f["kind"] for f in m.FLAGS}))

    if "commit is clean" in c:
        ok = not any(f["kind"] == "commit_without_test" for f in m.FLAGS)
        return (ok, "flags=%s" % sorted({f["kind"] for f in m.FLAGS}))

    mt = re.search(r"day label is ORDINAL (\w+)", c)
    if mt:
        entry = m.LEDGER.get(max(m.LEDGER)) if m.LEDGER else None
        ok = bool(entry) and entry["label_form"] == "ordinal" \
            and mt.group(1) in entry["label_translit"]
        return (ok, "label=%s form=%s" % (entry and entry["label_translit"],
                                          entry and entry["label_form"]))

    mt = re.search(r"WORLD \+= (\w+)\b", c)
    if mt:
        ent = m.WORLD["entities"].get(mt.group(1))
        ok = bool(ent) and ent["mode"] == "created" and ent["step"] == step_ref
        return (ok, "entity=%s" % ent)

    mt = re.search(r"triple .*\{([^}]+)\}\s*discharged", c)
    if mt:
        q = mt.group(1).strip()
        ok = any(t["discharged"] and t["q"] == q for t in m.TRIPLES)
        return (ok, "triples=%s" % m.TRIPLES)

    mt = re.search(r"TESTS \+= PASS\((\w+),\s*(\w+)\)", c)
    if mt:
        ok = any(t["oracle"] == mt.group(1) and t["theme"] == mt.group(2)
                 and t["verdict"] == "PASS" for t in m.TESTS)
        return (ok, "tests=%s" % [(t["oracle"], t["theme"]) for t in m.TESTS])

    mt = re.search(r"partition (\w+) ∩ (\w+) = ∅", c)
    if mt:
        ok = (mt.group(1), mt.group(2)) in m.WORLD["partitions"]
        return (ok, "partitions=%s" % m.WORLD["partitions"])

    mt = re.search(r"REGISTRY: ([\w-]+)->(\w+), ([\w-]+)->(\w+) \((\d+) writes\)", c)
    if mt:
        want = {mt.group(1): mt.group(2), mt.group(3): mt.group(4)}
        ok = m.REGISTRY["names"] == want and m.REGISTRY["writes"] == int(mt.group(5))
        return (ok, "names=%s writes=%d" % (m.REGISTRY["names"], m.REGISTRY["writes"]))

    mt = re.search(r"REGISTRY: ([\w-]+)->(\w+) \((\d+) writes?\)", c)
    if mt:
        want = {mt.group(1): mt.group(2)}
        ok = m.REGISTRY["names"] == want and m.REGISTRY["writes"] == int(mt.group(3))
        return (ok, "names=%s writes=%d" % (m.REGISTRY["names"], m.REGISTRY["writes"]))

    # ---- pattern added at the gen_45 remediation (2026-08-06, owner-authorized) ----
    mt = re.search(r"REGISTRY (\d+) writes", c)
    if mt:
        ok = m.REGISTRY["writes"] == int(mt.group(1))
        return (ok, "writes=%d names=%s" % (m.REGISTRY["writes"],
                                            sorted(m.REGISTRY["names"])))

    mt = re.search(r"LEDGER\[day (\d+)\] committed with (.+)", c)
    if mt:
        entry = m.LEDGER.get(int(mt.group(1)))
        if not entry or not entry["closed"]:
            return (False, "no closed ledger entry for day %s" % mt.group(1))
        fields, notes = mt.group(2), []
        ok = True
        if "spec" in fields and not entry["spec_ok"]:
            ok = False; notes.append("spec not ok")
        if "test PASS" in fields and not entry["test_pass"]:
            ok = False; notes.append("no test pass")
        nm = re.search(r"names (\d+)", fields)
        if nm and entry["names"] != int(nm.group(1)):
            ok = False; notes.append("names=%d" % entry["names"])
        return (ok, "; ".join(notes) or "entry=%s" % entry)

    mt = re.search(r"day label is CARDINAL (\w+)", c)
    if mt:
        entry = m.LEDGER.get(max(m.LEDGER)) if m.LEDGER else None
        ok = bool(entry) and entry["label_form"] == "cardinal" \
            and mt.group(1) in entry["label_translit"]
        return (ok, "label=%s form=%s" % (entry and entry["label_translit"],
                                          entry and entry["label_form"]))

    # ---- patterns added at the gen_06/gen_07 freeze (2026-07-31) ----
    mt = re.search(r"CMD-US\?\((.+?)\) pushed and OPEN", c)
    if mt:
        ok = any(e["demand"] == mt.group(1) and not e["satisfied_step"]
                 for e in m.SPECS["queue"])
        return (ok, "queue=%s" % [e["demand"] for e in m.SPECS["queue"]])

    mt = re.search(r"CMD-US\?\((.+?)\) mood remains CMD-US\?", c)
    if mt:
        for e in m.SPECS["log"]:
            if e["demand"] == mt.group(1):
                return (e["mood"] == "CMD-US?", "mood=%s" % e["mood"])
        return (False, "no spec with demand %s" % mt.group(1))

    mt = re.search(r"triple .*\{([^}]+)\}\s*stands undischarged", c)
    if mt:
        q = mt.group(1).strip()
        for tr in m.TRIPLES:
            if tr["q"] == q:
                return (not tr["discharged"], "discharged=%s" % tr["discharged"])
        return (False, "no triple with q=%s" % q)

    mt = re.search(r"flags (\S+) as assigned-before-presence", c)
    if mt:
        want = [x.strip() for x in mt.group(1).split("/")]
        flagged = {f["detail"] for f in m.FLAGS
                   if f["kind"] == "assigned_before_any_presence"}
        missing = [w for w in want if w not in flagged]
        return (not missing, "flagged=%s" % sorted(flagged))

    if re.search(r"LEDGER stays EMPTY \(open transaction\)", c):
        return (not m.LEDGER, "ledger_days=%s" % sorted(m.LEDGER))

    # ---- patterns added at the gen_08 freeze (2026-08-01) ----
    mt = re.search(r"LET\?\((.+?)\) pushed and OPEN", c)
    if mt:
        ok = any(e["demand"] == mt.group(1) and not e["satisfied_step"]
                 for e in m.SPECS["queue"])
        return (ok, "queue=%s" % [e["demand"] for e in m.SPECS["queue"]])

    mt = re.search(r"LET-NOT\((.+?)\) pushed and OPEN", c)
    if mt:
        ok = any(e["demand"] == mt.group(1) and not e["satisfied_step"]
                 for e in m.SPECS["queue"])
        return (ok, "queue=%s" % [e["demand"] for e in m.SPECS["queue"]])

    mt = re.search(r"LET-NOT\((.+?)\) mood remains LET-NOT", c)
    if mt:
        for e in m.SPECS["log"]:
            if e["demand"] == mt.group(1):
                return (e["mood"] == "LET-NOT", "mood=%s" % e["mood"])
        return (False, "no spec with demand %s" % mt.group(1))

    # ---- pattern added at the gen_09 freeze (2026-08-01) ----
    mt = re.search(r"TESTS \+= FAIL\((\w+),\s*(\w+)\)", c)
    if mt:
        ok = any(t["oracle"] == mt.group(1) and t["theme"] == mt.group(2)
                 and t["verdict"] == "FAIL" for t in m.TESTS)
        return (ok, "tests=%s" % [(t["verdict"], t["oracle"], t["theme"])
                                  for t in m.TESTS])

    return ("UNCHECKED", c)


# ---------------------------------------------------------------------------
# Negative-contract self-tests (S6 / S7)
# ---------------------------------------------------------------------------

def contract_commit_without_test():
    """S6: cycle close with TESTS empty must FLAG, never block."""
    m = Machine()
    m._step_ref = "synthetic.day2-shape"
    op = {"op": "COMMIT", "en": "",
          "expr_en": "cycle(erev -> boqer); LEDGER[day 99] := {names 0}"}
    try:
        h_commit(m, op, {"ref": "synthetic.day2-shape"})
    except ContractError as e:
        return [("commit with empty TESTS did not block", False, str(e))]
    flagged = any(f["kind"] == "commit_without_test" for f in m.FLAGS)
    committed = 99 in m.LEDGER and m.LEDGER[99]["closed"]
    return [
        ("commit proceeded (not blocked)", committed, "LEDGER=%s" % sorted(m.LEDGER)),
        ("pattern deviation FLAGGED", flagged,
         "flags=%s" % [f["kind"] for f in m.FLAGS]),
    ]


def contract_let_never_upgrades():
    """S7: LET? -> LET/CMD! without a per-unit citation must refuse."""
    m = Machine()
    m._step_ref = "synthetic.let?"
    h_declare(m, {"op": "DECLARE",
                  "expr_en": "DECLARE(Elohim, LET?(swarm(mayim)))"},
              {"ref": "synthetic.let?"})
    mood = m.SPECS["log"][0]["mood"]
    results = [("imperfect-in-command parsed as LET? (question mark kept)",
                mood == "LET?", "mood=%s" % mood)]
    try:
        m.resolve_spec("swarm(mayim)", "LET", cite=None)
        results.append(("auto-upgrade REFUSED", False, "upgrade went through!"))
    except ContractError as e:
        results.append(("auto-upgrade REFUSED", True, str(e)[:60] + "..."))
    entry = m.resolve_spec("swarm(mayim)", "LET",
                           cite="per-unit judgment (owner), TIR-028 resolution")
    results.append(("upgrade WITH citation allowed",
                    entry["mood"] == "LET" and bool(entry["resolution_cite"]),
                    "cite=%s" % entry["resolution_cite"]))
    return results


def contract_cmd_us_never_upgrades():
    """S9 (gen_06): CMD-US? -> CMD-US/CMD! without a per-unit citation must
    refuse — the new mood family inherits TIR-028's contract unchanged."""
    m = Machine()
    m._step_ref = "synthetic.cmd-us?"
    h_declare(m, {"op": "DECLARE",
                  "expr_en": "DECLARE(Elohim, CMD-US?(make(adam), spec=b_tzelem_k_demut))"},
              {"ref": "synthetic.cmd-us?"})
    mood = m.SPECS["log"][0]["mood"]
    results = [("volitive 1cp parsed as CMD-US? (question mark kept)",
                mood == "CMD-US?", "mood=%s" % mood)]
    try:
        m.resolve_spec("make(adam), spec=b_tzelem_k_demut", "CMD-US", cite=None)
        results.append(("auto-upgrade REFUSED", False, "upgrade went through!"))
    except ContractError as e:
        results.append(("auto-upgrade REFUSED", True, str(e)[:60] + "..."))
    entry = m.resolve_spec("make(adam), spec=b_tzelem_k_demut", "CMD-US",
                           cite="per-unit judgment (owner), TIR-028 resolution")
    results.append(("upgrade WITH citation allowed",
                    entry["mood"] == "CMD-US" and bool(entry["resolution_cite"]),
                    "cite=%s" % entry["resolution_cite"]))
    return results


def contract_let_not_never_resolves():
    """S10 (gen_08): a prohibition has NO resolution path — LET-NOT is not
    a ?-mood, so resolve_spec must refuse OUTRIGHT, citation or none: no
    path exists that flips a prohibition into a permission. The mood a
    prohibition is born with is the mood it keeps (first firing: Gen 2:17
    lo tokhal, 'you shall not eat' — TIR-034)."""
    m = Machine()
    m._step_ref = "synthetic.let-not"
    h_declare(m, {"op": "DECLARE",
                  "expr_en": "DECLARE(YHWH_Elohim, LET-NOT(akhal(adam, me_etz_ha_daat_tov_va_ra)))"},
              {"ref": "synthetic.let-not"})
    mood = m.SPECS["log"][0]["mood"]
    results = [("prohibitive lo+imperfect parsed as LET-NOT",
                mood == "LET-NOT", "mood=%s" % mood)]
    try:
        m.resolve_spec("akhal(adam, me_etz_ha_daat_tov_va_ra)", "LET", cite=None)
        results.append(("resolution without citation REFUSED", False, "went through!"))
    except ContractError as e:
        results.append(("resolution without citation REFUSED", True, str(e)[:60] + "..."))
    try:
        m.resolve_spec("akhal(adam, me_etz_ha_daat_tov_va_ra)", "LET",
                       cite="per-unit judgment (owner)")
        results.append(("resolution WITH citation ALSO refused (no ?-mood path)",
                        False, "went through!"))
    except ContractError as e:
        results.append(("resolution WITH citation ALSO refused (no ?-mood path)",
                        True, str(e)[:60] + "..."))
    still = m.SPECS["log"][0]["mood"]
    results.append(("mood unchanged after both attempts",
                    still == "LET-NOT", "mood=%s" % still))
    return results


# ---------------------------------------------------------------------------
# Scenario runner
# ---------------------------------------------------------------------------

def run_scenarios(unit):
    alias = build_alias(unit)
    all_ok = True
    for sc in unit.get("scenarios", []):
        sid, title = sc.get("id", "?"), sc.get("title_en", "")
        print("\n=== %s — %s" % (sid, title))
        if sc.get("value_he"):
            print("    %s (%s)" % (sc["value_he"], sc.get("value_he_translit", "")))

        if sid.endswith("_negative"):
            expect = sc.get("expect_en", "")
            if "CMD-US?" in expect:
                checks = contract_cmd_us_never_upgrades()
            elif "LET-NOT" in expect:
                checks = contract_let_not_never_resolves()
            elif "LET?" in expect:
                checks = contract_let_never_upgrades()
            elif "FLAG" in expect:
                checks = contract_commit_without_test()
            else:
                print("    UNCHECKED contract scenario"); all_ok = False; continue
            for label, ok, note in checks:
                print("    %s  %s  (%s)" % ("PASS" if ok else "FAIL", label, note))
                all_ok = all_ok and ok
            continue

        mt = re.search(r"after (STEP_\w+)", title)
        if not mt:
            print("    UNCHECKED: no 'after STEP_x' anchor"); all_ok = False; continue
        step_id = mt.group(1)
        step = next(s for s in unit["boot_steps"] if s["id"] == step_id)
        m = run_steps(unit, upto_step_id=step_id)
        expect = " ".join(str(sc.get("expect_en", "")).split())
        for clause in expect.split(";"):
            res = check_clause(clause, m, step["ref"], alias)
            if res is None:
                continue
            ok, note = res
            if ok == "UNCHECKED":
                print("    UNCHECKED  %s" % note); all_ok = False
            else:
                print("    %s  %s  (%s)" % ("PASS" if ok else "FAIL",
                                            clause.strip(), note))
                all_ok = all_ok and ok
    return all_ok


# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Stage D interpreter (frozen units only)")
    ap.add_argument("unit_id")
    ap.add_argument("--scenarios", action="store_true",
                    help="assert the unit's scenarios (S*)")
    ap.add_argument("--trace", action="store_true",
                    help="print per-step register deltas")
    args = ap.parse_args()

    try:
        unit = load_unit(args.unit_id)
        validate_unit(unit)
    except ContractError as e:
        print("CONTRACT: %s" % e, file=sys.stderr)
        sys.exit(2)

    meta = unit["meta"]
    print("unit: %s — %s [%s]" % (meta["id"], meta.get("title_en", ""),
                                  meta.get("status")))

    try:
        m = run_steps(unit, trace=args.trace)
    except ContractError as e:
        print("RED (fix YAML or version the rulebook): %s" % e, file=sys.stderr)
        sys.exit(1)

    print("\nfinal state: WORLD=%s (+%d presupposed) | REGISTRY=%s | "
          "TESTS=%d PASS | LEDGER days=%s | FLAGS=%s"
          % (sorted(m.created_set()), len(m.presupposed_set()),
             m.REGISTRY["names"], len(m.TESTS), sorted(m.LEDGER),
             [f["kind"] for f in m.FLAGS]))

    if args.scenarios:
        ok = run_scenarios(unit)
        print("\n%s" % ("ALL SCENARIOS GREEN" if ok else "SCENARIOS RED"))
        sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
