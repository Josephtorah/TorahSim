#!/usr/bin/env python3
"""build_world.py — PASS 1: compile the frozen receipts into the world
journal (L0 scripture events + L1 structure events), index it, emit the
world_tree.json view, and verify the tutoring document's claims.

Read-only over the physics. Walks the frozen YAMLs in corpus_world's
canonical order, replicating its global op seq exactly (proven pattern:
world_player/build_trace.py). Deterministic: no timestamps in segments;
canonical JSON; run twice and byte-compare (peer delta 2).

THE WITNESS GATE (peer delta 1, mechanical): no L1 event other than
witness.note may ground in a WITNESS_* op — enforced at emit time, and
re-scanned after the fold. A tag is a label; this is the wall.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]                     # .../Torah_Grok
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import yaml                                # noqa: E402
import corpus_world as cw                  # noqa: E402
from worldledger import Segment, index_sqlite, canon  # noqa: E402

DATA = Path(os.environ.get("WORLD_OUT_DIR", str(HERE / "data")))
DATA.mkdir(exist_ok=True)

REG = {p.stem: yaml.safe_load((HERE / "registers" / (p.stem + ".yaml"))
                              .read_text(encoding="utf-8"))
       for p in (HERE / "registers").glob("*.yaml")}
KNOWN_KINDS = {k["id"] for k in REG["event_kinds"]["kinds"]}
NODE_CLASS = dict(REG["classes"]["assignments"])
TYPE_IDS = {k["id"] for k in REG["kinds"]["kinds"]}

# v0 containment seed: entity -> parent container (targeted; honest —
# unlisted entities stay unplaced)
PARENT = {"raqia": "shamayim", "yamim": "aretz", "yabasha": "aretz",
          "gan": "eden", "eden": "aretz", "nahar": "eden",
          "nahar_1": "nahar", "nahar_2": "nahar", "nahar_3": "nahar",
          "nahar_4": "nahar", "ir": "aretz", "tevah": "aretz",
          "adam": "aretz", "chavah": "aretz", "keruvim": "gan",
          "shinar": "aretz", "goshen": "aretz",
          "etz_ha_chayim": "gan", "etz_ha_daat_tov_va_ra": "gan"}
# registry-kind -> node-class (the registry's own knowledge classifies
# what the assignments table does not)
REGKIND_CLASS = {"person": "person", "collective": "people",
                 "people": "people", "place": "place", "divine": "divine",
                 "compound": "people"}
# Exodus dialect (stress-test lesson 2026-08-24): the forward-era units
# install nothing — entities are born by NAMING. Prefix -> class.
NAME_BORN = {"maqom": "place", "mizbeach": "object", "ha-lechem": "object",
             "beer_": "well"}
LOC_MAP = {"raqia_ha_shamayim": "raqia", "pnei_raqia_ha_shamayim": "raqia"}
WELL_CLASS_PREFIX = "beer_"


def main():
    tokmap, reg_entities, _ = cw.load_config()
    regkind = {e["id"]: e.get("kind") for e in reg_entities}

    def ent(token, uid):
        return cw.entity_for(tokmap, token, uid)

    L0 = Segment("L0", "build_world/0")
    L1 = Segment("L1", "build_world/0")
    stats = {"unclassified_nodes": 0, "witness_notes": 0}

    def emit(kind, subj, data, uid, ref, op_kind, op_seq):
        # ---- THE WITNESS GATE (mechanical, at the pen) ----
        if op_kind.startswith("WITNESS") and kind != "witness.note":
            raise SystemExit("WITNESS GATE: %s tried to ground %s in %s"
                             % (subj, kind, op_kind))
        if kind not in KNOWN_KINDS:
            raise SystemExit("unregistered event kind: %s (register first)"
                             % kind)
        return L1.append(kind, subj, data,
                         {"unit": uid, "ref": ref, "opk": op_kind},
                         op=op_seq)

    def born(token, uid, ref, opk, seq, cls=None, parent=None):
        eid = ent(token, uid)
        c = cls or NODE_CLASS.get(token) or NODE_CLASS.get(eid)
        if c is None and regkind.get(eid) in REGKIND_CLASS:
            c = REGKIND_CLASS[regkind[eid]]
        if c is None and token.startswith(WELL_CLASS_PREFIX):
            c = "well"
        if c is None:
            c = "entity"
            stats["unclassified_nodes"] += 1
        p = parent if parent is not None else PARENT.get(token, PARENT.get(eid))
        d = {"class": c}
        if p:
            d["parent"] = ent(p, uid)
        emit("node.born", eid, d, uid, ref, opk, seq)

    seq = 0
    for uid, unit in cw.frozen_units_in_canonical_order():
        for st in unit["boot_steps"]:
            ref = st["ref"]
            for op in st.get("operators", []):
                seq += 1
                k = str(op.get("op", ""))
                x = str(op.get("expr_en", ""))
                L0.append("scripture.op", uid, {"k": k, "x": x[:160]},
                          {"unit": uid, "ref": ref}, op=seq)

                # ---------------- generic extractors ----------------
                if k == "REGISTRY_INSTALL":
                    m = re.search(r"WORLD \+= \{([^}]*)\}", x)
                    for tok in (t.strip() for t in m.group(1).split(",")):
                        if tok:
                            born(tok, uid, ref, k, seq)
                elif k == "NAME":
                    for a, b in re.findall(r"name\(([\w-]+)\)\s*:=\s*(\w+)", x):
                        for pref, ncls in NAME_BORN.items():
                            if a.startswith(pref):
                                born(a, uid, ref, k, seq, cls=ncls,
                                     parent="aretz")
                                break
                        emit("name.set", ent(a, uid), {"label": b},
                             uid, ref, k, seq)
                        if a == "raqia":   # the day-2 join: built IS Heaven
                            emit("edge.insert", "raqia",
                                 {"into": ent("shamayim", uid),
                                  "why": "name join — the firmament IS the "
                                         "container named Heaven"},
                                 uid, ref, k, seq)
                elif k == "EVENT_PARTITION":
                    m = re.search(r"between\(([\w-]+),\s*([\w-]+)\)", x)
                    emit("partition.split",
                         "%s|%s" % (m.group(1), m.group(2)),
                         {"a": m.group(1), "b": m.group(2)},
                         uid, ref, k, seq)
                elif k == "NOTE_PRESUPPOSED":
                    m = re.match(r"(.+?) are READ", x)
                    known = "known geography" in x
                    for tok in (t.strip() for t in m.group(1).split(",")):
                        if tok:
                            emit("node.presupposed", ent(tok, uid),
                                 {"class": "place" if known else "presup"},
                                 uid, ref, k, seq)
                elif k == "RESULT":
                    em = re.search(r"exists\((\w+)\)", x)
                    lm = re.search(r"loc=([\w-]+)", x)
                    pm = re.search(r"product=([\w-]+)", x)
                    vm = re.search(r"HOLDS\((\w+)\((\w+)\)", x)
                    if em and not lm:
                        born(em.group(1), uid, ref, k, seq)
                    if lm:
                        subj = em.group(1) if em else (
                            vm.group(2) if vm else "?")
                        into = LOC_MAP.get(lm.group(1), lm.group(1))
                        emit("edge.insert", ent(subj, uid),
                             {"into": ent(into, uid), "loc_raw": lm.group(1)},
                             uid, ref, k, seq)
                        if em:
                            born(em.group(1), uid, ref, k, seq,
                                 parent=into)
                    if pm and vm:
                        val = pm.group(1)
                        emit("slot.set", ent(vm.group(2), uid),
                             {"slot": "produce", "value": val,
                              "typed": val in TYPE_IDS or
                              "le_minah" in val or val.endswith("_le_minah")},
                             uid, ref, k, seq)
                elif k in ("WITNESS_STATE", "WITNESS_READ"):
                    m = re.search(r"WITNESS(?:-READ)?\((\w+),\s*(\w+)\)", x)
                    stats["witness_notes"] += 1
                    emit("witness.note",
                         ent(m.group(1), uid) if m else "?",
                         {"state": m.group(2) if m else x[:80],
                          "walled": True},
                         uid, ref, k, seq)
                elif k in ("CASE", "HANDLER", "STATUTE", "PATTERN"):
                    if uid == "gen_22_covenant_bow" and k == "HANDLER":
                        emit("trigger.install", "qeshet",
                             {"in": "anan", "domain": ent("shamayim", uid),
                              "if": "the bow is seen in the cloud",
                              "then": "I will remember My covenant"},
                             uid, ref, k, seq)
                    else:
                        emit("law.install", uid, {"kind": k, "x": x[:120]},
                             uid, ref, k, seq)

                # ---------------- targeted extractors ----------------
                if uid == "gen_08_toledot_garden_first_rule":
                    if ref == "Gen.2.8" and k == "EVENT" and "plant" in x:
                        emit("edge.insert", ent("gan", uid),
                             {"into": ent("eden", uid), "how": "planted"},
                             uid, ref, k, seq)
                    if k == "PRECONDITION_STATE":
                        cm = re.search(r"sovev_kol_eretz_(\w+)\((nahar_\d)\)", x)
                        if cm:
                            emit("edge.link", ent(cm.group(2), uid),
                                 {"rel": "circles",
                                  "to": ent(cm.group(1), uid)},
                                 uid, ref, k, seq)
                        if "sham_ha_zahav" in x:
                            emit("edge.link", ent("chavilah", uid),
                                 {"rel": "resource", "to": "zahav",
                                  "en": "there is the gold"},
                                 uid, ref, k, seq)
                if uid == "gen_11_sentences_exile":
                    if ref == "Gen.3.18" and "kotz_ve_dardar" in x:
                        emit("slot.update", ent("adamah", uid),
                             {"slot": "produce", "value": ["kotz", "dardar"],
                              "was_ref": "Gen.1.12",
                              "en": "thorn and thistle — the curse rewrites "
                                    "the produce slot; kinds carried as the "
                                    "tradition's new-or-redirected question"},
                             uid, ref, k, seq)
                    if ref == "Gen.3.24" and k == "EVENT" and "station" in x:
                        emit("guard.station", ent("keruvim", uid),
                             {"at": "east of the garden",
                              "facing": "etz_ha_chayim",
                              "with": "lahat_ha_cherev"},
                             uid, ref, k, seq)
                if uid == "gen_16_ark_spec" and k == "PRECONDITION_STATE":
                    if "shelosh_meot_amah" in x:
                        emit("slot.set", ent("tevah", uid),
                             {"slot": "dimensions",
                              "value": {"length_amot": 300, "width_amot": 50,
                                        "height_amot": 30}},
                             uid, ref, k, seq)
                    if "tzohar_la_tevah" in x:
                        emit("slot.set", ent("tevah", uid),
                             {"slot": "features",
                              "value": ["tzohar (light)", "door in side",
                                        "three decks"]},
                             uid, ref, k, seq)
                    if "shnayim_mi_kol" in x:
                        emit("slot.set", ent("tevah", uid),
                             {"slot": "manifest",
                              "value": "two of every kind, by its kind "
                                       "(le-minehu) — the type column as "
                                       "the loading list's sort key"},
                             uid, ref, k, seq)
                if uid == "gen_17_boarding" and k == "EVENT":
                    if "mayenot_tehom" in x and "split" in x:
                        emit("partition.breach", "mayim-under|mayim-over",
                             {"side": "below",
                              "via": "the fountains of the great deep"},
                             uid, ref, k, seq)
                    if "arubot_ha_shamayim" in x and "open" in x:
                        emit("partition.breach", "mayim-under|mayim-over",
                             {"side": "above",
                              "via": "the windows of the heavens"},
                             uid, ref, k, seq)
                if uid == "gen_19_the_remembering" and "stop_up" in x:
                    emit("partition.restore", "mayim-under|mayim-over",
                         {"via": "fountains and windows stopped up"},
                         uid, ref, k, seq)
                if uid == "gen_24_nations_table" and k == "PRECONDITION_STATE":
                    if "le_mishpechotam" in x or "mishpechot" in x:
                        emit("census.population", ent("aretz", uid),
                             {"row": x[:110],
                              "columns": ["family", "tongue", "land",
                                          "nation"]},
                             uid, ref, k, seq)
                    if "niflegah_ha_aretz" in x:
                        emit("partition.split", ent("aretz", uid),
                             {"by": "peleg",
                              "en": "in his days the earth was divided"},
                             uid, ref, k, seq)
                if uid == "gen_25_babel" and k == "EVENT" and "scatter" in x:
                    emit("mandate.enforce", ent("aretz", uid),
                         {"mandate": "fill the earth (Gen 1:28)",
                          "refusal": "lest we be scattered (Gen 11:4)",
                          "en": "the scatter executes the fill instruction"},
                         uid, ref, k, seq)
                if uid == "gen_33_shaddai_covenant_flesh" and \
                        k == "PRECONDITION_STATE":
                    if "lo_yiqare_od_shimkha_avram" in x:
                        emit("name.replace", ent("avram", uid),
                             {"old": "avram", "new": "avraham",
                              "semantics": "old key retired (Babylonian "
                                           "Talmud, Berakhot 13a)"},
                             uid, ref, k, seq)
                    if "lo_tiqra_et_shemah_saray" in x:
                        emit("name.replace", ent("saray", uid),
                             {"old": "saray", "new": "sarah",
                              "semantics": "old key retired"},
                             uid, ref, k, seq)
                if uid == "gen_55_two_camps_wrestled_name" and \
                        "lo_yaaqov_yeamer_od" in x:
                    emit("name.alias", ent("yaaqov", uid),
                         {"add": "yisrael", "keeps": "yaaqov",
                          "semantics": "alias — both keys live (decree "
                                       "fact; the text keeps using Yaakov)"},
                         uid, ref, k, seq)
                if uid == "gen_45_wells_covenant_esau_wives" and \
                        "restore_names_like_father" in x:
                    emit("name.restore", ent("beerot_avraham", uid),
                         {"from": "the previous generation's registry",
                          "en": "called by the names his father called them"},
                         uid, ref, k, seq)
                if uid == "gen_39_machpelah_purchase" and \
                        k == "EVENT" and "weigh_silver" in x:
                    emit("deed.transfer", "sde_machpelah",
                         {"from": ent("efron", uid), "to": ent("avraham", uid),
                          "price": "400 shekels of silver, weighed",
                          "witnessed": "at the city gate"},
                         uid, ref, k, seq)
                if uid == "gen_48_bethel_ladder_vow" and \
                        "sulam_earthward" in x:
                    emit("channel.open", "sulam",
                         {"between": [ent("aretz", uid), ent("shamayim", uid)],
                          "traffic": "angels ascending and descending",
                          "gate_named": "shaar ha-shamayim (the gate of the "
                                        "heavens) — an earth address"},
                         uid, ref, k, seq)
                if uid == "gen_70_goshen_and_the_fifth" and k == "RESULT" \
                        and "goshen" in x:
                    emit("grant.assign", ent("goshen", uid),
                         {"to": ent("bene_yaaqov", uid),
                          "by": "pharaoh's grant settling the spoken demand"},
                         uid, ref, k, seq)

    # ---------------- write segments + index ----------------
    p0, p1 = DATA / "L0_scripture.jsonl", DATA / "L1_structure.jsonl"
    L0.write(p0)
    L1.write(p1)
    assert Segment.verify(p0) and Segment.verify(p1), "chain verify failed"
    n = index_sqlite(DATA / "world.sqlite", [p0, p1])

    # ---- post-fold witness wall re-scan (belt over the braces) ----
    for ev in L1.events:
        if ev["prov"]["opk"].startswith("WITNESS"):
            assert ev["kind"] == "witness.note", "WALL LEAK: %r" % ev

    # ---------------- the tree view ----------------
    nodes, timeline, breaches = {}, [], []
    open_breach = {}
    def touch(s):
        """Provisional node — a spec can precede its build (the ark:
        dimensions at 6:15, existence at 6:22)."""
        if s not in nodes:
            nodes[s] = {"class": NODE_CLASS.get(s, "entity"),
                        "parent": PARENT.get(s), "born": None, "ref": None,
                        "names": [], "slots": {}, "wit": [], "marks": []}
        return nodes[s]

    for ev in L1.events:
        k, s = ev["kind"], ev["subj"]
        if k == "node.born":
            nd = touch(s)
            if nd["born"] is None:
                nd.update(born=ev["op"], ref=ev["prov"]["ref"],
                          **{"class": ev["data"]["class"]})
                if ev["data"].get("parent"):
                    nd["parent"] = ev["data"]["parent"]
        if k == "node.presupposed":
            nd = touch(s)
            if nd["born"] is None:
                nd.update(born=ev["op"], ref=ev["prov"]["ref"],
                          presupposed=True,
                          **{"class": ev["data"]["class"]})
        nd = nodes[s] if s in nodes else (
            touch(s) if k in ("slot.set", "slot.update", "name.set",
                              "name.replace", "name.alias", "edge.insert",
                              "witness.note", "guard.station",
                              "trigger.install", "channel.open",
                              "deed.transfer", "grant.assign",
                              "name.restore") else None)
        if nd:
            if k == "name.set":
                nd["names"].append({"label": ev["data"]["label"],
                                    "op": ev["op"]})
            if k in ("name.replace", "name.alias"):
                nd["names"].append({"label": ev["data"].get("new") or
                                    ev["data"].get("add"),
                                    "mode": k.split(".")[1], "op": ev["op"]})
            if k in ("slot.set", "slot.update"):
                nd["slots"][ev["data"]["slot"]] = {
                    "value": ev["data"]["value"], "op": ev["op"],
                    "updated": k == "slot.update"}
            if k == "edge.insert" and ev["data"].get("into"):
                nd["parent"] = ev["data"]["into"]
            if k == "witness.note":
                nd["wit"].append({"state": ev["data"]["state"],
                                  "op": ev["op"]})
            if k in ("guard.station", "trigger.install", "channel.open",
                     "deed.transfer", "grant.assign", "name.restore"):
                nd["marks"].append({"kind": k, "op": ev["op"]})
        if k == "partition.breach":
            open_breach.setdefault(s, ev["op"])
        if k == "partition.restore" and s in open_breach:
            breaches.append({"subj": s, "open": open_breach.pop(s),
                             "close": ev["op"]})
        timeline.append({"op": ev["op"], "kind": k, "subj": s})

    view = {"contract": "world-tree/0",
            "counts": {"L0": len(L0.events), "L1": len(L1.events),
                       "nodes": len(nodes),
                       "unclassified": stats["unclassified_nodes"]},
            "nodes": nodes, "timeline": timeline, "breaches": breaches}
    (DATA / "world_tree.json").write_text(
        canon(view), encoding="utf-8")
    (DATA / "world_tree.json").write_text(canon(view), encoding="utf-8")

    # ---------------- per-book dialect report (CODE, not a hand scan;
    # the 2026-08-24 Exodus finding, made a standing gate) ----------------
    def book_of(uid):
        return uid.split("_")[0]
    dial = {}
    for ev in L0.events:
        b = book_of(ev["prov"]["unit"])
        d = dial.setdefault(b, {"ops": 0, "installs": 0, "names": 0,
                                "partitions": 0, "L1": 0, "born": 0})
        d["ops"] += 1
        k = ev["data"]["k"]
        if k == "REGISTRY_INSTALL":
            d["installs"] += 1
        if k == "NAME":
            d["names"] += 1
        if k == "EVENT_PARTITION":
            d["partitions"] += 1
    for ev in L1.events:
        b = book_of(ev["prov"]["unit"])
        dial[b]["L1"] += 1
        if ev["kind"] == "node.born":
            dial[b]["born"] += 1
    print("\n--- DIALECT REPORT (per book) ---")
    for b in sorted(dial):
        d = dial[b]
        print("  %-4s ops %-5d installs %-3d names %-3d partitions %-2d "
              "-> L1 events %-4d born %d"
              % (b, d["ops"], d["installs"], d["names"], d["partitions"],
                 d["L1"], d["born"]))

    # ---------------- verification checklist ----------------
    kinds_seen = {}
    for ev in L1.events:
        kinds_seen[ev["kind"]] = kinds_seen.get(ev["kind"], 0) + 1
    exo_born = [ev for ev in L1.events if ev["kind"] == "node.born"
                and book_of(ev["prov"]["unit"]) == "exo"]
    exo_law = sum(1 for ev in L1.events if ev["kind"] == "law.install"
                  and ev["prov"]["unit"] == "exo_21_the_ordinances")
    checks = [
        ("roots born at Gen 1:1", nodes.get("shamayim", {}).get("ref") ==
         "Gen.1.1" and nodes.get("aretz", {}).get("ref") == "Gen.1.1"),
        ("garden inside Eden inside earth",
         nodes.get("gan", {}).get("parent") == "eden" and
         nodes.get("eden", {}).get("parent") == "aretz"),
        ("firmament joined to Heaven",
         nodes.get("raqia", {}).get("parent") == "shamayim"),
        ("luminaries inserted with location",
         nodes.get("meorot", {}).get("parent") == "raqia"),
        ("ark has dimensions + manifest",
         "dimensions" in nodes.get("tevah", {}).get("slots", {}) and
         "manifest" in nodes.get("tevah", {}).get("slots", {})),
        ("flood breach opened twice and restored",
         kinds_seen.get("partition.breach", 0) == 2 and
         len(breaches) == 1),
        ("curse updated the produce slot",
         any(n.get("slots", {}).get("produce", {}).get("updated")
             for n in nodes.values())),
        ("rename replace present (Avraham)",
         kinds_seen.get("name.replace", 0) == 2),
        ("rename alias present (Yisrael)",
         kinds_seen.get("name.alias", 0) == 1),
        ("registry restore present (the wells)",
         kinds_seen.get("name.restore", 0) == 1),
        ("nations census rows", kinds_seen.get("census.population", 0) == 5),
        ("Babel enforcement", kinds_seen.get("mandate.enforce", 0) == 1),
        ("deed + grant present", kinds_seen.get("deed.transfer", 0) == 1 and
         kinds_seen.get("grant.assign", 0) == 1),
        ("sky trigger installed", kinds_seen.get("trigger.install", 0) == 1),
        ("channel opened (the ladder)",
         kinds_seen.get("channel.open", 0) == 1),
        ("boundary guard stationed",
         kinds_seen.get("guard.station", 0) == 1),
        ("witness wall held (all witness ops -> witness.note only)", True),
        ("forming/filling symmetry — day 4 fills day 2's vault, day 5 "
         "fills day 2's waters + vault, day 6 fills day 3's land",
         any(e["kind"] == "edge.insert" and e["data"].get("into") == "raqia"
             and e["prov"]["unit"].startswith("gen_04")
             for e in L1.events) and
         any(e["kind"] == "slot.set" and e["subj"] == "mayim"
             and e["prov"]["unit"].startswith("gen_05")
             for e in L1.events) and
         any(e["kind"] == "edge.insert" and e["data"].get("into") == "raqia"
             and e["prov"]["unit"].startswith("gen_05")
             for e in L1.events) and
         any(e["kind"] == "slot.set" and e["subj"] == "aretz"
             and e["prov"]["unit"].startswith("gen_06")
             for e in L1.events)),
        # ---- Exodus dialect gates (pinned expectations: if a future
        # re-derivation changes the dialect, these BREAK LOUDLY) ----
        ("Exodus dialect pinned: zero REGISTRY_INSTALLs in the book",
         dial.get("exo", {}).get("installs", -1) == 0),
        ("Exodus births by naming: places + altar + manna present",
         any(ev["subj"].startswith("maqom") for ev in exo_born) and
         any(ev["subj"] == "mizbeach" for ev in exo_born) and
         any(ev["subj"] == "ha-lechem" for ev in exo_born)),
        ("Exodus 21 standing law installed (27 ordinance ops, pinned)",
         exo_law == 27),
    ]
    print("\n=== WORLD JOURNAL BUILT ===")
    print("L0 %d scripture events · L1 %d structure events · %d nodes "
          "(%d unclassified) · %d indexed rows" %
          (len(L0.events), len(L1.events), len(nodes),
           stats["unclassified_nodes"], n))
    print("event kinds:", canon(kinds_seen))
    ok = True
    for label, passed in checks:
        print(("  PASS  " if passed else "  FAIL  ") + label)
        ok = ok and passed
    print("CHECKLIST: " + ("ALL GREEN" if ok else "FAILURES ABOVE"))


def selftest_determinism():
    """Byte-grade determinism gate (peer delta 2, codified): fold in a
    SEPARATE PROCESS into a temp dir, byte-compare both segments."""
    import filecmp
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        env = dict(os.environ, WORLD_OUT_DIR=td)
        r = subprocess.run([sys.executable, __file__], env=env,
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout[-800:], r.stderr[-800:])
            raise SystemExit("determinism selftest: second fold failed")
        for seg in ("L0_scripture.jsonl", "L1_structure.jsonl"):
            if not filecmp.cmp(str(HERE / "data" / seg),
                               str(Path(td) / seg), shallow=False):
                raise SystemExit("DETERMINISM FAIL: %s differs across "
                                 "processes" % seg)
    print("DETERMINISM: byte-identical across two processes — GREEN")


if __name__ == "__main__":
    main()
    if "--selftest" in sys.argv:
        selftest_determinism()
