#!/usr/bin/env python3
# =============================================================================
# TIER: MILL — transforms and reports; asserts nothing new about the text.
# The expansion-lens provenance report (owner's test, 2026-08-27).
# Reads (never writes): the block-3 claims manifest, the block-3 draft
# machine's source, and this folder's MODEL-tier claim_tiers.json.
# Then instruments the machine and RUNS a scene, reporting which
# provenance tiers actually fire on the code path.
# =============================================================================
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
MANIFEST = REPO / "logic/oral_audit/manifests/law03_exo_21_28_37_claims.json"
BLOCK3 = REPO / "logic/law_era/exo_21_v2_block3_DRAFT.py"

claims = {c["id"]: c for c in json.load(open(MANIFEST))}
tiers = json.load(open(HERE / "claim_tiers.json"))["claims"]

# --- gate 1: the tier table covers the manifest exactly, both ways ---------
assert set(claims) == set(tiers), (
    "tier table out of join with manifest: only-in-manifest=%s only-in-table=%s"
    % (sorted(set(claims) - set(tiers)), sorted(set(tiers) - set(claims))))

# --- the machine tally (primary tiers) -------------------------------------
tally = {}
for cid, t in tiers.items():
    tally[t["primary"]] = tally.get(t["primary"], 0) + 1
print("MACHINE TALLY (primary tier, all %d claims):" % len(tiers))
for k in sorted(tally, key=lambda k: -tally[k]):
    print("  %s : %2d" % (k, tally[k]))
compiled = sum(tally.get(k, 0) for k in ("K", "I", "M"))
installs = tally.get("G", 0)
print("  kernel-compiled (K+I+M): %d of %d | self-declared installs (G): %d"
      % (compiled, len(tiers), installs))

# --- map machine functions -> cited claims -> tiers ------------------------
src = open(BLOCK3).read()
chunks = re.split(r"^(?=def |[A-Z_]+ =)", src, flags=re.M)
print("\nMACHINE PROVENANCE (block-3 draft, per definition):")
seen_ids = set()
for ch in chunks:
    name = ch.split("(")[0].split("=")[0].replace("def ", "").strip()
    ids = sorted(set(re.findall(r"\[(L\d+-\d+|L0-\d+)", ch)))
    if not name or not ids or "\n" not in ch:
        continue
    seen_ids.update(i for i in ids if i in tiers)
    profile = sorted({tiers[i]["primary"] for i in ids if i in tiers})
    print("  %-28s cites %-30s tiers %s"
          % (name[:28], ",".join(ids), "".join(profile)))

# --- gate 2: every machine-cited claim id resolves in the manifest ---------
all_cited = set(re.findall(r"\[(L\d+-\d+|L0-\d+)", src))
unresolved = sorted(i for i in all_cited if i not in claims)
assert not unresolved, "machine cites unknown claim ids: %s" % unresolved
print("\ngate: all %d machine-cited claim ids resolve in the manifest"
      % len(all_cited & set(claims)))

# --- RUN: instrument the machine, execute a scene, report tiers fired ------
sys.path.insert(0, str(REPO / "logic/law_era"))
import importlib.util as ilu


def _load(name):
    spec = ilu.spec_from_file_location(name, REPO / ("logic/law_era/%s.py" % name))
    mod = ilu.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b3 = _load("exo_21_v2_block3_DRAFT")
fn_ids = {}
for ch in chunks:
    if ch.startswith("def "):
        nm = ch[4:].split("(")[0].strip()
        fn_ids[nm] = sorted(set(re.findall(r"\[(L\d+-\d+|L0-\d+)", ch)))
fired = []
for nm, ids in fn_ids.items():
    if hasattr(b3, nm) and callable(getattr(b3, nm)):
        def wrap(f, nm=nm):
            def g(*a, **kw):
                fired.append(nm)
                return f(*a, **kw)
            return g
        setattr(b3, nm, wrap(getattr(b3, nm)))

print("\nSCENE (live run): three gorings on three days, owner warned; "
      "the ox kills a slave; then one clean petting day")
ox = b3.new_ox("reuven")
for day in (1, 2, 3):
    b3.record_goring(ox, day, species="man", context="weekday",
                     owner_present_testimony=True)
st = b3.status(ox, victim_is_man=True)
assert st == "muad", st
led = b3.owner_liability("muad", "slave")
assert led["slave_fine"] == 30, led
b3.record_clean_petting_day(ox)
assert b3.status(ox, victim_is_man=True) == "tam"
print("  verdict: status vested muad -> slave fine 30 -> one petting day reverts to tam")

fired_ids = sorted({i for nm in fired for i in fn_ids.get(nm, []) if i in tiers})
prof = {}
for i in fired_ids:
    prof[tiers[i]["primary"]] = prof.get(tiers[i]["primary"], 0) + 1
print("  functions fired: %s" % ", ".join(dict.fromkeys(fired)))
print("  claims on the code path: %s" % ", ".join(fired_ids))
print("  TIER PROFILE OF THE VERDICT: %s"
      % "  ".join("%s:%d" % (k, prof[k]) for k in sorted(prof)))
print("\nEXPANSION REPORT GREEN")
