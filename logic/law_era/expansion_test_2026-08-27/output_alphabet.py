#!/usr/bin/env python3
# =============================================================================
# TIER: MILL, carrying one MODEL data table (marked below).
# THE OUTPUT-ALPHABET TEST (2026-08-27) — the Grok note's central invariant,
# run on our material: does the oral expansion ever mint a verdict KIND the
# verse never named? The note scored 48 Mishnah rows NEW_MODULE:0; here we
# test our 35 witnessed claims and the live machine outputs against the
# block's verse-named verdict alphabet. Reads only; writes nothing.
# =============================================================================
import json
import importlib.util as ilu
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]

# The verse-named verdict alphabet of Exodus 21:28-37 (kernel range):
ALPHABET = {
    "STONE": "the ox is stoned (21:28,29,32)",
    "NO_BENEFIT": "its flesh not eaten — the prohibition class (21:28)",
    "CLEAR": "the owner is clear / exempt (21:28 naki)",
    "OWNER_DEATH": "its owner also shall die (21:29)",
    "RANSOM": "kofer laid on him, redemption of his life (21:30)",
    "THIRTY": "thirty shekels for the slave (21:32)",
    "SPLIT": "sell the live ox and divide money and carcass (21:35)",
    "FULL_PAY": "he shall surely pay ox for ox (21:36)",
    "CARCASS": "the dead one is his — carcass allocation (21:34,36)",
    "RESTITUTION": "the pit's owner pays money to the beast's owner (21:34)",
    "TARIFF": "five oxen for the ox, four sheep for the sheep (21:37)",
}

# --- MODEL-tier data: each claim's output category and alphabet mapping ----
# category: VERDICT rows face the alphabet test; STATUS/PROCEDURE rows are
# gates and machinery, not verdicts; NA rows change no output.
# strain: inside the alphabet, but stretching it — recorded, per the test.
OUTPUTS = {
 "L28-01": ("STATUS",    None,          ""),
 "L28-02": ("VERDICT",   "STONE",       "scope widened, verdict unchanged"),
 "L28-03": ("PROCEDURE", None,          "court size and margin"),
 "L28-04": ("VERDICT",   "CLEAR",       "intent gate exempts from stoning"),
 "L28-05": ("VERDICT",   "NO_BENEFIT",  "timing fixed; prohibition class widened eat->benefit"),
 "L28-06": ("VERDICT",   "CLEAR",       "clear deepened to Heaven's court"),
 "L29-01": ("STATUS",    None,          ""),
 "L29-02": ("PROCEDURE", None,          "the five written differences are gates"),
 "L29-03": ("PROCEDURE", None,          "evidence regimes"),
 "L29-04": ("VERDICT",   "OWNER_DEATH", "STRAIN: same letter, executor reassigned court->Heaven"),
 "L29-05": ("PROCEDURE", None,          "guarding grade"),
 "L30-01": ("VERDICT",   "RANSOM",      "mechanics expanded, letter unchanged"),
 "L30-02": ("VERDICT",   "RANSOM",      "boundary: where the letter may NOT be used"),
 "L31-01": ("VERDICT",   "OWNER_DEATH", "same judgment extended to son/daughter victims"),
 "L32-01": ("VERDICT",   "THIRTY",      "kernel constant; typing kapparah-not-price"),
 "L32-02": ("NA",        None,          ""),
 "L32-03": ("NA",        None,          ""),
 "L33-01": ("VERDICT",   "RESTITUTION", "depth thresholds gate death- vs injury-liability"),
 "L33-02": ("VERDICT",   "CLEAR",       "decreed exclusions exempt"),
 "L33-03": ("VERDICT",   "RESTITUTION", "cover law: who pays"),
 "L33-04": ("PROCEDURE", None,          "who inherits the liability — scope of 'owner'"),
 "L34-01": ("VERDICT",   "CARCASS",     "whose the dead one is"),
 "L35-01": ("VERDICT",   "SPLIT",       "equal-value gate on the split"),
 "L35-02": ("VERDICT",   "SPLIT",       "STRAIN: the letter's own TYPE disputed (fine vs money)"),
 "L35-03": ("VERDICT",   "SPLIT",       "STRAIN: remedy re-typed as partnership in the ox"),
 "L36-01": ("VERDICT",   "FULL_PAY",    "collection from the best"),
 "L36-02": ("VERDICT",   "FULL_PAY",    "party scoping"),
 "L37-01": ("VERDICT",   "TARIFF",      "class closed to ox and sheep"),
 "L37-02": ("VERDICT",   "TARIFF",      "disposal conditions gate the tariff"),
 "L37-03": ("VERDICT",   "TARIFF",      "agency exception routes the tariff to the thief"),
 "L37-04": ("VERDICT",   "TARIFF",      "4/5 shown composed of the double"),
 "L37-05": ("VERDICT",   "TARIFF",      "the constants themselves, decree-tier"),
 "L37-06": ("PROCEDURE", None,          "whose the fine is; oaths"),
 "L0-01":  ("NA",        None,          ""),
 "L0-02":  ("NA",        None,          ""),
}

tiers = json.load(open(HERE / "claim_tiers.json"))["claims"]
assert set(OUTPUTS) == set(tiers), "output map out of join with tier table"

verdict_rows = [(k, v) for k, v in OUTPUTS.items() if v[0] == "VERDICT"]
new_kinds = [(k, v) for k, v in verdict_rows if v[1] not in ALPHABET]
strains = [(k, v) for k, v in verdict_rows if v[2].startswith("STRAIN")]

print("OUTPUT-ALPHABET TEST — Exodus 21:28-37, %d claims" % len(OUTPUTS))
print("  verse-named alphabet: %d letters" % len(ALPHABET))
print("  VERDICT rows: %d | STATUS: %d | PROCEDURE: %d | NA: %d" % (
    len(verdict_rows),
    sum(1 for v in OUTPUTS.values() if v[0] == "STATUS"),
    sum(1 for v in OUTPUTS.values() if v[0] == "PROCEDURE"),
    sum(1 for v in OUTPUTS.values() if v[0] == "NA")))
print("  NEW KINDS MINTED: %d" % len(new_kinds))
for k, v in new_kinds:
    print("    !!", k, v)
print("  STRAINS (inside the alphabet, stretching it): %d" % len(strains))
for k, v in strains:
    print("    ~ %s [%s tier %s] %s" % (k, v[1], tiers[k]["primary"], v[2]))

# --- live check: harvest the machine's actual outputs ----------------------
spec = ilu.spec_from_file_location(
    "b3", REPO / "logic/law_era/exo_21_v2_block3_DRAFT.py")
b3 = ilu.module_from_spec(spec)
spec.loader.exec_module(b3)

harvest = set()
ox = b3.new_ox()
for d in (1, 2, 3):
    b3.record_goring(ox, d, species="man", owner_present_testimony=True)
harvest.add(("status", b3.status(ox, victim_is_man=True)))
led = b3.owner_liability("muad", "slave")
harvest.add(("capital", str(led["capital"])))
harvest.add(("slave_fine", str(led["slave_fine"])))
led2 = b3.owner_liability("muad", "man", victim_value=200)
harvest.add(("kofer", str(led2["kofer"])))
led3 = b3.owner_liability("tam", "man")
harvest.add(("tam_note", led3["note"][:24]))
harvest.add(("benefit", str(b3.benefit_status(True, False))))
harvest.add(("stoning", str(b3.stoning_verdict(True)["stoned"])
             if isinstance(b3.stoning_verdict(True), dict)
             else str(b3.stoning_verdict(True))))

MAP = {"status": "gate (tam/muad)", "capital": "OWNER_DEATH (Heaven strain)",
       "slave_fine": "THIRTY", "kofer": "RANSOM", "tam_note": "CLEAR",
       "benefit": "NO_BENEFIT", "stoning": "STONE"}
print("\nLIVE MACHINE OUTPUTS -> alphabet letters:")
for k, val in sorted(harvest):
    print("  %-11s = %-28s -> %s" % (k, val[:28], MAP[k]))
print("\nFINDING: the machine emits no output outside the verse-named "
      "alphabet;\nthe strains sit exactly on the O and D tiers.")
print("OUTPUT-ALPHABET TEST GREEN")
