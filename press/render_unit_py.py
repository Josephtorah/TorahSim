#!/usr/bin/env python3
"""
render_unit_py.py — generate logic/py_units/<unit_id>.py from a FROZEN unit.

Pre-Code contract: the frozen YAML is canonical; the emitted Python is a
DERIVED RENDERING (like the UNIT_*.html pages) — one facade call per
operator, per-verse comments carrying transliteration + English gloss
(the absolute glossing rule), and a final assertion block baked from the
Stage D interpreter's ACTUAL machine truth at generation time. The
generated file is executed before this script reports success, so every
rendering doubles as a standing plain-Python regression test.

Usage:
  python3 render_unit_py.py <unit_id>     # one unit
  python3 render_unit_py.py              # ALL frozen units (regen chain mode)
"""
import importlib.util
import re
import subprocess
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNITS = ROOT / "logic" / "units"
import os as _os
OUT = (Path(_os.environ["TS_OUT"]) if _os.environ.get("TS_OUT")
       else ROOT / "units")

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sys as _vsys; from pathlib import Path as _VP; _vsys.path.insert(0, str(_VP(__file__).resolve().parent / "vendor"))
import yaml
import run_unit as ru
import step_unit as _g   # the gloss engine (display-only) — owner order
                         # 2026-08-02: Hebrew + English in code comments,
                         # every machine token translated, no transliteration
import gloss_db          # per-word English: SNAPSHOT gloss column +
                         # authored overrides; owner order 2026-08-09:
                         # every quoted Hebrew span translated inline


def G(tok):
    """Gloss one machine token into English (falls back to the token)."""
    tok = str(tok).strip()
    g = (_g.GLOSS_EXACT.get(tok) or _g.GLOSS_UNIT.get(tok)
         or _g.GLOSS_CORE.get(tok) or _g.gloss_token(tok))
    return g if g else tok


def GE(s):
    """Gloss a call-shaped expression, e.g. tze(noach, min_ha_tevah)."""
    return _g.gloss_expr(str(s).strip())


def _wrap_comment(text, prefix="# ", width=76):
    out = []
    for ln in textwrap.wrap(text, width=width - len(prefix)) or [""]:
        out.append(prefix + ln)
    return out


def _q(s):
    """Emit a python string literal (double-quoted, escaped)."""
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


def emit_op(op):
    """Map one YAML operator to facade call lines (mirrors run_unit parsing)."""
    kind = op.get("op")
    expr = op.get("expr_en", "")
    L = []
    if kind == "TIME_ANCHOR":
        mt = re.search(r"t0 := (\w+)", expr)
        L.append("m.time_anchor(%s)" % _q(mt.group(1)))
    elif kind == "EVENT":
        verb = re.match(r"(\w+)\(e\d+\)", expr)
        agent = re.search(r"Agent\(e\d+,\s*([\w-]+)\)", expr)
        themes = re.findall(r"Theme\(e\d+,\s*([\w-]+)\)", expr)
        args = [_q(verb.group(1) if verb else "?")]
        if agent:
            args.append("agent=%s" % _q(agent.group(1)))
        if themes:
            args.append("themes=[%s]" % ", ".join(_q(t) for t in themes))
        L.append("m.event(%s)" % ", ".join(args))
    elif kind == "REGISTRY_INSTALL":
        mt = re.search(r"WORLD \+= \{([^}]*)\}", expr)
        names = [x.strip() for x in mt.group(1).split(",") if x.strip()]
        L.append("m.install(%s)" % ", ".join(_q(n) for n in names))
    elif kind == "PRECONDITION_STATE":
        facts = re.findall(r"HOLDS\((.+?),\s*t\d+\)", expr)
        L.append("m.fact(%s)" % (",\n       ".join(_q(f.strip()) for f in facts)))
    elif kind == "INVARIANT":
        mt = re.search(r"INVARIANT\((.+)\)\s*during", expr)
        L.append("m.invariant(%s)" % _q(mt.group(1).strip()))
    elif kind == "NOTE_ZERO_EVENTS":
        L.append("m.note_zero_events()")
    elif kind == "NOTE_PRESUPPOSED":
        mt = re.match(r"(.+?) are READ", expr)
        names = [x.strip() for x in mt.group(1).split(",") if x.strip()]
        L.append("m.presupposed(%s)" % ", ".join(_q(n) for n in names))
    elif kind == "NOTE_SPEC_DELTA":
        mt = re.search(r"spec '(.+?)' delivered '(.+?)'", expr)
        L.append("m.spec_delta(%s,\n             %s)"
                 % (_q(mt.group(1)), _q(mt.group(2))))
    elif kind == "DECLARE":
        speaker = re.search(r"DECLARE\((\w+),", expr)
        mood = ("CMD-US?" if "CMD-US?(" in expr else
                "CMD-US" if "CMD-US(" in expr else
                "LET?" if "LET?(" in expr else
                "LET-NOT" if "LET-NOT(" in expr else "LET")
        dm = re.search(r"(?:LET\??(?:-NOT)?|CMD-US\??)\((.+)\)\)", expr)
        L.append("m.declare(%s, %s,\n          %s)"
                 % (_q(speaker.group(1) if speaker else "?"), _q(mood),
                    _q(dm.group(1).strip() if dm else "?")))
    elif kind == "TRIPLE":
        qm = re.search(r"\{\s*Q:\s*([^}]+)\}", expr)
        L.append("m.triple(%s)" % _q(qm.group(1).strip()))
    elif kind == "RESULT":
        hm = re.search(r"HOLDS\((.+?),\s*t\d+\)", expr)
        tm = re.search(r",\s*(t\d+)\)", expr)
        args = [_q(hm.group(1).strip())]
        if tm:
            args.append("tmark=%s" % _q(tm.group(1)))
        L.append("m.result(%s)" % ", ".join(args))
    elif kind == "TEST":
        mt = re.search(r"(PASS|FAIL)\((\w+),\s*(\w+)\)", expr)
        L.append("m.test(%s, %s, %s)" % (_q(mt.group(1)), _q(mt.group(2)),
                                         _q(mt.group(3))))
    elif kind == "EVENT_PARTITION":
        mt = re.search(r"between\(([\w-]+),\s*([\w-]+)\)", expr)
        L.append("m.partition(%s, %s)" % (_q(mt.group(1)), _q(mt.group(2))))
    elif kind == "NAME":
        for ent, label in re.findall(r"name\(([\w-]+)\)\s*:=\s*(\w+)", expr):
            L.append("m.name(%s, %s)" % (_q(ent), _q(label)))
    elif kind == "ASSIGN":
        for ent, role in re.findall(r"([\w-]+)->([\w-]+)", expr):
            L.append("m.assign(%s, %s)" % (_q(ent), _q(role)))
    elif kind == "BLESS":
        sp = re.search(r"BLESS\((\w+),\s*([\w-]+)\)", expr)
        mt = re.search(r"MANDATE \{([^}]*)\}", expr)
        items = ([x.strip() for x in mt.group(1).split(",") if x.strip()]
                 if mt else [])
        args = [_q(sp.group(1)), _q(sp.group(2))]
        if items:
            args.append("mandate=[%s]" % ", ".join(_q(i) for i in items))
        L.append("m.bless(%s)" % ", ".join(args))
    elif kind == "CASE":
        mt = re.search(r"CASE\((.+)\)\s*ROUTE\(([\w-]+)\)", expr)
        L.append("m.case(%s, %s)" % (_q(mt.group(1).strip()), _q(mt.group(2))))
    elif kind == "HANDLER":
        mt = re.search(r"HANDLER IF\((.+)\) THEN\((.+)\)", expr)
        L.append("m.handler(%s,\n          %s)"
                 % (_q(mt.group(1).strip()), _q(mt.group(2).strip())))
    elif kind == "PATTERN":
        mt = re.search(r"PATTERN\((.+)\)", expr)
        L.append("m.pattern(%s)" % _q(mt.group(1).strip()))
    elif kind == "STATUTE":
        mt = re.search(r"STATUTE (FORBID|BIND)\((.+)\)", expr)
        L.append("m.statute(%s, %s)" % (_q(mt.group(1)), _q(mt.group(2).strip())))
    elif kind == "SECTION":
        mt = re.search(r"SECTION\((\w+),\s*(.+)\)", expr)
        members = [x.strip() for x in mt.group(2).split(",") if x.strip()]
        L.append("m.section(%s)" % ", ".join([_q(mt.group(1))]
                                             + [_q(x) for x in members]))
    elif kind == "ORAL_UTTERANCE":
        mt = re.match(r"UTTERANCE\((\d+),\s*([\w-]+)\)", expr)
        if mt:
            L.append("m.utterance(%s, %s)" % (mt.group(1), _q(mt.group(2))))
        else:
            L.append("m.utterance_disputed(%s)" % _q(op.get("en", "")))
    elif kind == "WITNESS_STATE":
        mt = re.match(r"WITNESS\(([\w-]+),\s*([\w-]+)\)", expr)
        L.append("m.witness_state(%s, %s,\n                cites=[%s])"
                 % (_q(mt.group(1)), _q(mt.group(2)),
                    ", ".join(_q(c) for c in op.get("cites", []))))
    elif kind == "WITNESS_READ":
        mt = re.match(r"WITNESS-READ\(([\w-]+),\s*([\w-]+)\)", expr)
        L.append("m.witness_read(%s, %s,\n                cites=[%s])"
                 % (_q(mt.group(1)), _q(mt.group(2)),
                    ", ".join(_q(c) for c in op.get("cites", []))))
    elif kind == "COMMIT":
        dm = re.search(r"LEDGER\[day (\d+)\]", expr)
        en_note = op.get("en", "")
        form = ("cardinal" if "CARDINAL" in en_note
                else "ordinal" if "ORDINAL" in en_note else None)
        args = [dm.group(1)]
        if form:
            args.append("label_form=%s" % _q(form))
        if op.get("he_translit"):
            args.append("label_translit=%s" % _q(op["he_translit"]))
        L.append("m.commit(%s)" % ", ".join(args))
    else:
        raise SystemExit("unmapped operator kind: %s" % kind)
    return L


def op_comment(op, ref=None):
    """English comment line(s) for one operator — the owner's rule: every
    machine token in the code is translated, in comments interleaved with
    the code (Hebrew snippet first where the YAML carries one, now with
    its own word-by-word English in quotes right after it)."""
    kind = op.get("op")
    expr = op.get("expr_en", "")
    if kind == "TIME_ANCHOR":
        mt = re.search(r"t0 := (\w+)", expr)
        en = "clock anchored: t0 := %s" % G(mt.group(1))
    elif kind == "EVENT":
        verb = re.match(r"(\w+)\(e\d+\)", expr)
        agent = re.search(r"Agent\(e\d+,\s*([\w-]+)\)", expr)
        themes = re.findall(r"Theme\(e\d+,\s*([\w-]+)\)", expr)
        bits = ["event: %s" % G(verb.group(1) if verb else "?")]
        if agent:
            bits.append("agent %s" % G(agent.group(1)))
        if themes:
            bits.append("theme %s" % ", ".join(G(t) for t in themes))
        en = " — ".join([bits[0], "; ".join(bits[1:])]) if bits[1:] else bits[0]
    elif kind == "REGISTRY_INSTALL":
        mt = re.search(r"WORLD \+= \{([^}]*)\}", expr)
        names = [x.strip() for x in mt.group(1).split(",") if x.strip()]
        en = "the world gains: %s" % ", ".join(G(n) for n in names)
    elif kind == "PRECONDITION_STATE":
        facts = re.findall(r"HOLDS\((.+?),\s*t\d+\)", expr)
        en = "fact holds: %s" % "; ".join(GE(f) for f in facts)
    elif kind == "INVARIANT":
        mt = re.search(r"INVARIANT\((.+)\)\s*during", expr)
        en = "standing constraint: %s" % GE(mt.group(1))
    elif kind == "NOTE_ZERO_EVENTS":
        en = "note: zero events in this verse"
    elif kind == "NOTE_PRESUPPOSED":
        mt = re.match(r"(.+?) are READ", expr)
        names = [x.strip() for x in mt.group(1).split(",") if x.strip()]
        en = ("reads without prior install (flag, not fix): %s"
              % ", ".join(G(n) for n in names))
    elif kind == "NOTE_SPEC_DELTA":
        mt = re.search(r"spec '(.+?)' delivered '(.+?)'", expr)
        en = ("spec-delta — spec said %s, delivery says %s"
              % (GE(mt.group(1)), GE(mt.group(2))))
    elif kind == "DECLARE":
        speaker = re.search(r"DECLARE\((\w+),", expr)
        mood = ("CMD-US?" if "CMD-US?(" in expr else
                "CMD-US" if "CMD-US(" in expr else
                "LET?" if "LET?(" in expr else
                "LET-NOT" if "LET-NOT(" in expr else "LET")
        dm = re.search(r"(?:LET\??(?:-NOT)?|CMD-US\??)\((.+)\)\)", expr)
        en = ("%s speaks a demand — %s: %s"
              % (G(speaker.group(1) if speaker else "?"), mood,
                 GE(dm.group(1) if dm else "?")))
    elif kind == "TRIPLE":
        qm = re.search(r"\{\s*Q:\s*([^}]+)\}", expr)
        en = "open question logged: %s" % GE(qm.group(1))
    elif kind == "RESULT":
        hm = re.search(r"HOLDS\((.+?),\s*t\d+\)", expr)
        en = "demand settled (popped from the queue): %s" % GE(hm.group(1))
    elif kind == "TEST":
        mt = re.search(r"(PASS|FAIL)\((\w+),\s*(\w+)\)", expr)
        en = ("test %s — oracle-word %s, on %s"
              % (mt.group(1), G(mt.group(2)), G(mt.group(3))))
    elif kind == "EVENT_PARTITION":
        mt = re.search(r"between\(([\w-]+),\s*([\w-]+)\)", expr)
        en = "partition between %s and %s" % (G(mt.group(1)), G(mt.group(2)))
    elif kind == "NAME":
        pairs = re.findall(r"name\(([\w-]+)\)\s*:=\s*(\w+)", expr)
        en = "named: " + "; ".join("%s := %s" % (G(a), G(b)) for a, b in pairs)
    elif kind == "ASSIGN":
        pairs = re.findall(r"([\w-]+)->([\w-]+)", expr)
        en = "role assigned: " + "; ".join(
            "%s -> %s" % (G(a), G(b)) for a, b in pairs)
    elif kind == "BLESS":
        sp = re.search(r"BLESS\((\w+),\s*([\w-]+)\)", expr)
        mt = re.search(r"MANDATE \{([^}]*)\}", expr)
        en = "blessing: %s blesses %s" % (G(sp.group(1)), G(sp.group(2)))
        if mt:
            items = [x.strip() for x in mt.group(1).split(",") if x.strip()]
            en += " — mandate: %s" % ", ".join(G(i) for i in items)
    elif kind == "CASE":
        mt = re.search(r"CASE\((.+)\)\s*ROUTE\(([\w-]+)\)", expr)
        en = "case %s routes to %s" % (GE(mt.group(1)), G(mt.group(2)))
    elif kind == "HANDLER":
        mt = re.search(r"HANDLER IF\((.+)\) THEN\((.+)\)", expr)
        en = "standing handler — if %s then %s" % (GE(mt.group(1)),
                                                   GE(mt.group(2)))
    elif kind == "PATTERN":
        mt = re.search(r"PATTERN\((.+)\)", expr)
        en = "pattern recorded: %s" % GE(mt.group(1))
    elif kind == "SECTION":
        mt = re.search(r"SECTION\((\w+),\s*(.+)\)", expr)
        members = [x.strip() for x in mt.group(2).split(",") if x.strip()]
        en = "section %s: %s" % (G(mt.group(1)),
                                 ", ".join(G(x) for x in members))
    elif kind == "ORAL_UTTERANCE":
        mt = re.match(r"UTTERANCE\((\d+)", expr)
        en = ("utterance #%s of the ten (ma'amar census)" % mt.group(1)
              if mt else "disputed utterance — machloket carried, not decided")
    elif kind == "WITNESS_STATE":
        mt = re.match(r"WITNESS\(([\w-]+),\s*([\w-]+)\)", expr)
        en = ("witness-grounded state (its own tier): %s on %s"
              % (mt.group(2), mt.group(1)))
    elif kind == "WITNESS_READ":
        mt = re.match(r"WITNESS-READ\(([\w-]+),\s*([\w-]+)\)", expr)
        en = ("witness-tier presupposed read: %s on %s — read, not installed"
              % (mt.group(2), mt.group(1)))
    elif kind == "COMMIT":
        dm = re.search(r"LEDGER\[day (\d+)\]", expr)
        en = "ledger: day %s committed" % dm.group(1)
    else:
        en = ""
    he = str(op.get("he", "")).strip().replace("\n", " ")
    if he and ref:
        span_en = gloss_db.translate_span(he, ref)
        head = ("\u2039%s\u203a (\u201c%s\u201d) \u2014 %s"
                % (he, span_en, en)) if span_en \
            else ("\u2039%s\u203a %s" % (he, en))
    elif he:
        head = "\u2039%s\u203a %s" % (he, en)
    else:
        head = en
    return _wrap_comment(head)


def render(uid):
    path = UNITS / (uid + ".yaml")
    unit = yaml.safe_load(path.read_text(encoding="utf-8"))
    meta = unit["meta"]
    if meta.get("status") != "frozen":
        print("SKIP %s — not frozen (py renderings track frozen units only, "
              "Pre-Code)" % uid)
        return

    truth = ru.run_steps(unit)   # machine truth from the Stage D interpreter
    refs = [st["ref"] for st in unit["boot_steps"]]
    _g.GLOSS_UNIT.clear()
    _g.GLOSS_UNIT.update(gloss_db.build_translit_gloss(refs))  # DB layer
    _g.GLOSS_UNIT.update(_g.build_unit_gloss(unit))     # authored layer wins
    gloss_db.set_unit_tree(unit)

    L = ["#!/usr/bin/env python3",
         "# TorahSim — (c) 2026 Brian LeBlanc · MIT license "
         "(see LICENSE at repo root)",
         "# " + "=" * 77,
         "# %s — %s" % (uid, meta.get("refs", "")),
         "# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py."]
    L += _wrap_comment("The YAML (logic/units/%s.yaml) is CANONICAL (Pre-Code); "
                       "this file is a derived, runnable rendering. Do not edit "
                       "— regenerate. The assertion block at the bottom is baked "
                       "from the Stage D interpreter's actual final state: "
                       "running this file re-proves the unit." % uid)
    L += ["# Experimental model — not binding religious law.",
          "# " + "=" * 77,
          '"""%s"""' % meta.get("title_en", uid),
          "from machine import Machine",
          "",
          'm = Machine("%s")' % uid,
          ""]

    for st in unit["boot_steps"]:
        ref = st["ref"]
        L.append("# " + ("-" * 26) + " %s · %s " % (ref, st.get("op", ""))
                 + "-" * max(1, 74 - 30 - len(ref) - len(st.get("op", ""))))
        he = str(st.get("he", "")).strip().replace("\n", " ")
        if he:
            L += _wrap_comment(he)
        en = st.get("en", "").replace("[EN-AID/JPS] ", "")
        if en:
            L += _wrap_comment('"%s"' % en)
        L.append('m.step("%s")' % ref)
        for op in st.get("operators", []):
            L += op_comment(op, ref)
            L += emit_op(op)
        L.append("")

    # ---- baked assertions from machine truth --------------------------------
    flags = {}
    for f in truth.FLAGS:
        flags[f["kind"]] = flags.get(f["kind"], 0) + 1
    tests = [(t["verdict"], t["oracle"], t["theme"]) for t in truth.TESTS]
    open_d = [e["demand"] for e in truth.SPECS["queue"]]
    L += ["# " + "-" * 26 + " machine truth (baked from the Stage D run) " + "-" * 7,
          'if __name__ == "__main__":',
          "    m.report()",
          "    assert m.created_set() == %s" % (
              "{%s}" % ", ".join(repr(x) for x in sorted(truth.created_set()))
              if truth.created_set() else "set()"),
          "    assert m.presupposed_set() == %s" % (
              "{%s}" % ", ".join(repr(x) for x in
                                 sorted(truth.presupposed_set()))
              if truth.presupposed_set() else "set()"),
          '    assert m.REGISTRY["names"] == %r' % truth.REGISTRY["names"],
          '    assert m.REGISTRY["writes"] == %d' % truth.REGISTRY["writes"],
          "    assert m.tests_list() == %r" % tests,
          "    assert m.open_demands() == %r" % open_d,
          '    assert len(m.SPECS["log"]) == %d' % len(truth.SPECS["log"]),
          "    assert sorted(m.LEDGER) == %r" % sorted(truth.LEDGER),
          "    assert m.flag_counts() == %r" % flags,
          '    assert sorted(m.WORLD["facts"]) == sorted(%r)' % truth.WORLD["facts"],
          '    assert m.WORLD["invariants"] == %r' % truth.WORLD["invariants"],
          '    assert m.WORLD["partitions"] == %r' % truth.WORLD["partitions"],
          "    assert len(m.EVENTS) == %d" % len(truth.EVENTS),
          ]
    # amendment-era registers, asserted only where the unit carries them —
    # units without them reprint byte-identical (the press gate's parity)
    if truth.UTTERANCES:
        L += ['    assert [(u["n"], u["mode"]) for u in m.UTTERANCES] == %r'
              % [(u["n"], u["mode"]) for u in truth.UTTERANCES]]
    if truth.UTTERANCES_DISPUTED:
        L += ["    assert len(m.UTTERANCES_DISPUTED) == %d"
              % len(truth.UTTERANCES_DISPUTED)]
    _wit = truth.WORLD.get("witnessed", {})
    if _wit:
        L += ['    assert sorted(m.WORLD["witnessed"]) == %r' % sorted(_wit)]
        for _e in sorted(_wit):
            L += ['    assert m.WORLD["witnessed"][%s]["cites"] == %r'
                  % (repr(_e), _wit[_e]["cites"]),
                  '    assert all(%r not in f for f in m.WORLD["facts"])'
                  % _wit[_e]["state"]]
    if truth.WITNESS_READS:
        L += ['    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == %r'
              % [(w["entity"], w["state"]) for w in truth.WITNESS_READS]]
        for _i, _w in enumerate(truth.WITNESS_READS):
            L += ['    assert m.WITNESS_READS[%d]["cites"] == %r'
                  % (_i, _w["cites"]),
                  '    assert all(%r not in f for f in m.WORLD["facts"])'
                  % _w["state"]]
            if _w["entity"] not in truth.WORLD.get("witnessed", {}):
                L += ['    assert %r not in m.WORLD["witnessed"]'
                      % _w["entity"]]
    L += [
          '    print("ALL ASSERTIONS GREEN — rendering matches the frozen '
          "unit's machine truth\")",
          ""]

    OUT.mkdir(exist_ok=True)
    out_path = OUT / (uid + ".py")
    out_path.write_text("\n".join(L), encoding="utf-8")

    _env = dict(_os.environ,
                PYTHONPATH=str(ROOT / "units") + _os.pathsep
                + _os.environ.get("PYTHONPATH", ""))
    r = subprocess.run([sys.executable, str(out_path)],
                       capture_output=True, text=True, env=_env)
    if r.returncode != 0:
        sys.stderr.write(r.stdout + r.stderr)
        raise SystemExit("RED: generated rendering failed for %s" % uid)
    _shown = (out_path.relative_to(ROOT)
              if out_path.is_relative_to(ROOT) else out_path)
    print("wrote %s (%d lines) — ran GREEN" % (_shown, len(L)))


def all_frozen():
    out = []
    for p in sorted(UNITS.glob("*.yaml")):
        try:
            d = yaml.safe_load(p.read_text(encoding="utf-8"))
            if isinstance(d, dict) and d.get("meta", {}).get("status") == "frozen":
                out.append(d["meta"]["id"])
        except Exception:
            pass
    return out


if __name__ == "__main__":
    uids = sys.argv[1:] or all_frozen()
    for uid in uids:
        render(uid)
