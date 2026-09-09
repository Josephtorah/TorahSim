#!/usr/bin/env python3
"""run_cases.py — PASS 2: run declared scenes through the Exodus 21 v2
chapter machine and append the world journal's first L2 case events.

The truth split (peer delta 1): primary/scenes.yaml is the PRIMARY record
(declared inputs, not derivable, append-only). This runner derives the L2
segment from it deterministically — same scenes + same law = byte-identical
segment. Verdicts are computed by the law machine, never authored here.

Single-writer rule: this runner appends journal events; the sqlite index
is rebuilt from segments, never written directly.
"""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

import yaml                                          # noqa: E402
from worldledger import Segment, index_sqlite, canon  # noqa: E402


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


M = _load(ROOT / "logic" / "law_era" / "exo_21_v2_DRAFT.py", "exo21")

DATA = HERE / "data"
SCENES = yaml.safe_load((HERE / "primary" / "scenes.yaml")
                        .read_text(encoding="utf-8"))["scenes"]
BASIS = "Exodus 21 v2 chapter machine (logic/law_era/exo_21_v2_DRAFT.py)"


def run_scene(scene, seg):
    w = M.World()
    handles = {}          # scene-local name -> machine id
    prov = {"scene": scene["id"], "source": "primary/scenes.yaml"}
    seg.append("scene.open", scene["id"],
               {"title": scene["title"], "en": scene["en"],
                "inputs": scene["script"]}, prov)
    verdicts = []
    for step in scene["script"]:
        if "act" in step:
            a = step["act"]
            if a == "register_ox":
                handles[step["ox"]] = w.register_ox(step["ox"])
            elif a == "goring":
                w.goring(handles[step["ox"]],
                         owner_present_testimony=step.get("testimony",
                                                          False))
            elif a == "petting_day":
                w.petting_day(handles[step["ox"]])
            elif a == "advance":
                w.advance(step["days"])
            elif a == "enslave":
                sid, why = w.enslave_by_court(
                    step["theft"], step["worth_six_years_labor"])
                handles[step["slave"]] = sid
                verdicts.append(("court sale valid", why))
            elif a == "condemn":
                w.condemn(handles[step["ox"]])
            elif a == "execute":
                w.execute(handles[step["ox"]])
            else:
                raise SystemExit("unknown act %r" % a)
            seg.append("scene.act", scene["id"],
                       {"act": {k: v for k, v in step.items()},
                        "day": w.day}, prov)
        else:
            q = step["q"]
            if q == "ox_status":
                r = w.ox_status(handles[step["ox"]],
                                victim_is_man=step.get("victim_is_man",
                                                       False))
            elif q == "ox_benefit":
                r = w.ox_benefit(handles[step["ox"]])
            elif q == "slave_status":
                r = w.slave_status(handles[step["slave"]])
            elif q == "ox_vs_ox":
                st = w.ox_status(handles[step["ox"]])
                r = M.b3.ox_vs_ox(st if isinstance(st, str) else st[0],
                                  step["gorer_live_value"],
                                  step["gored_value"],
                                  step["carcass_value"])
            else:
                raise SystemExit("unknown query %r" % q)
            verdicts.append((q, r))
            seg.append("case.verdict", scene["id"],
                       {"q": {k: v for k, v in step.items()},
                        "result": r, "basis": BASIS, "day": w.day}, prov)
    seg.append("scene.close", scene["id"],
               {"snapshot": w.snapshot()}, prov)
    return verdicts


def main():
    seg = Segment("L2", "run_cases/0")
    report = []
    for scene in SCENES:
        report.append((scene["id"], scene["title"], run_scene(scene, seg)))
    p2 = DATA / "L2_cases.jsonl"
    seg.write(p2)
    assert Segment.verify(p2), "chain verify failed"
    n = index_sqlite(DATA / "world.sqlite",
                     [DATA / "L0_scripture.jsonl",
                      DATA / "L1_structure.jsonl", p2])

    # cases view for the dashboard / site
    view = {"contract": "world-cases/0", "basis": BASIS,
            "scenes": [{"id": sid, "title": t,
                        "verdicts": [{"q": q, "result": r}
                                     for q, r in vs]}
                       for sid, t, vs in report]}
    (DATA / "world_cases.json").write_text(
        canon(view), encoding="utf-8")

    print("=== PASS 2 — THE LIVING LAYER ===")
    print("L2 %d case events across %d scenes · %d rows indexed (L0+L1+L2)"
          % (len(seg.events), len(SCENES), n))
    for sid, title, vs in report:
        print("\n· %s — %s" % (sid, title))
        for q, r in vs:
            print("    %-14s -> %s" % (q, json.dumps(r, ensure_ascii=False)
                                       if not isinstance(r, str) else r))


if __name__ == "__main__":
    main()
