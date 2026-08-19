#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# SIMULATION SKETCH — what the Exodus 21 machine looks like as a WORLD,
# not a judge. Prototype (a sketch, not a stamped machine), run on the
# house of David — the first artifact of the simulation direction
# (see docs/ROADMAP_SIMULATION.md).
#
# THE TWO FINDINGS OF THE FIRST RUN (why this sketch is kept):
#   1. The ledger ends with David's heaven-debt at OPEN=1 after the
#      fourfold discharges — and that is CORRECT, not a bug: the four
#      answer the EWE; the open 1 is the blood of Uriah, which the text
#      never closes ('the sword shall never depart from your house').
#      The naive balance-check below expected 0; the doctrine says 1.
#   2. Joab's blood-debts sit on Heaven's docket and the coded execution
#      only clears the COURT docket — surfacing, uninvited, the exact
#      GRA-Netziv question: can the CROWN collect Heaven's ledger?
#      (Solomon's own words say yes: 'the LORD shall RETURN his blood.')
#
# The three upgrades over the rules engine:
#   1. LAWS FIRE AUTOMATICALLY — nobody asks for a verdict; every event
#      passes through every law, like objects passing through gravity.
#   2. LIABILITY IS STATE — the two dockets (court / Heaven) are LEDGERS
#      that persist across world-time and generations.
#   3. CONSEQUENCES ARE COMPUTED — the simulation itself decides what a
#      death discharges and what it newly opens, and we can CHECK its
#      ledger against what the narrative actually reports.
#
# Events are still hand-fed from the text — we simulate the LAW, never
# invent the history. Experimental model — not binding religious law.
# =============================================================================
import importlib.util, os

def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M = load(os.path.join(ROOT, "machines", "exo21", "chapter.py"), "chapter")
b2, b3 = M.b2, M.b3

# ---------------------------------------------------------------------------
# THE WORLD — persistent state + the two dockets as ledgers
# ---------------------------------------------------------------------------
class SimWorld:
    def __init__(self):
        self.year = 0
        self.court_docket = []      # liabilities a human court can collect
        self.heaven_docket = []     # liabilities delegated upward [L12-03]
        self.log = []

    def say(self, msg):
        self.log.append("  year %2d | %s" % (self.year, msg))

    def open_debt(self, docket, debtor, what, units=1):
        entry = {"debtor": debtor, "what": what, "units": units, "open": units}
        (self.heaven_docket if docket == "heaven"
         else self.court_docket).append(entry)
        self.say("%s DOCKET OPENS: %s owes %s (x%d)"
                 % (docket.upper(), debtor, what, units))
        return entry

    def discharge(self, debtor, note, units=1):
        for e in self.heaven_docket:
            if e["debtor"] == debtor and e["open"] > 0:
                e["open"] -= units
                self.say("HEAVEN COLLECTS from %s: %s  [%d/%d discharged]"
                         % (debtor, note, e["units"] - e["open"], e["units"]))
                return
        self.say("(no open heaven-debt for %s at: %s)" % (debtor, note))

    def open_total(self, debtor=None):
        return sum(e["open"] for e in self.heaven_docket
                   if debtor is None or e["debtor"] == debtor)

# ---------------------------------------------------------------------------
# THE LAWS AS PHYSICS — every event passes through every law, automatically.
# Each law consults the REAL machine and writes world-state.
# ---------------------------------------------------------------------------
def law_homicide(w, ev):
    if ev["kind"] != "killing":
        return
    v = b2.homicide_verdict(ev.get("grade", "mezid"),
                            warned_and_persisted=ev.get("witnessed", False))
    actor = ev["by"]
    if ev.get("via_agent"):
        w.say("AGENCY RULE: the striker acts, the sender %s is beyond "
              "the court" % actor)
    if v["track"] == "death" and not ev.get("war"):
        w.open_debt("court", actor, "blood of %s (court-collectable)" % ev["of"])
    elif ev.get("war"):
        w.say("WAR JURISDICTION: killing of %s by %s — no court, no docket"
              % (ev["of"], actor))
    else:
        w.open_debt("heaven", actor, "blood of %s" % ev["of"])

def law_theft_tariff(w, ev):
    if ev["kind"] != "taking":
        return
    t = b3.theft_tariff(ev.get("as_animal", "sheep"))
    w.open_debt("heaven", ev["by"],
                "the ewe taken (%s) — tariff x%d" % (ev["what"], t["multiplier"]),
                units=t["multiplier"])

def law_collection(w, ev):
    if ev["kind"] == "death_in_house":
        w.discharge(ev["house"], ev["who"])
    if ev["kind"] == "execution":
        for e in w.court_docket:
            if e["debtor"] == ev["of"] and e["open"] > 0:
                e["open"] = 0
                w.say("COURT/CROWN COLLECTS: %s executed — %s closed"
                      % (ev["of"], e["what"]))

LAWS = [law_homicide, law_theft_tariff, law_collection]

def run_event(w, year, desc, **ev):
    w.year = year
    w.say("EVENT: " + desc)
    for law in LAWS:
        law(w, ev)

# ---------------------------------------------------------------------------
# THE EVENT STREAM — the house of David, hand-fed from the text
# ---------------------------------------------------------------------------
w = SimWorld()
print("=" * 72)
print("SIMULATION: the house of David under the Exodus 21 physics")
print("=" * 72)

run_event(w, 0, "David takes Bathsheba (the ewe of the parable)",
          kind="taking", by="david", what="the one ewe", as_animal="sheep")
run_event(w, 0, "Uriah killed by letter, through Joab, by Ammonite swords",
          kind="killing", by="david", of="uriah", grade="mezid",
          witnessed=False, via_agent=True)
w.say("NATHAN READS THE LEDGER: 'fourfold' + 'you shall not die' — the "
      "prophet announces what the dockets already hold: heaven-open = %d"
      % w.open_total("david"))
run_event(w, 1, "the child dies", kind="death_in_house",
          house="david", who="the child")
run_event(w, 8, "Amnon killed by Absalom's servants at the feast",
          kind="killing", by="absalom", of="amnon", grade="mezid",
          witnessed=False, via_agent=True)
run_event(w, 8, "— and Amnon's death is also a collection",
          kind="death_in_house", house="david", who="Amnon")
run_event(w, 8, "Tamar left desolate", kind="death_in_house",
          house="david", who="Tamar (the living loss)")
run_event(w, 12, "Absalom dies in the wood, by Joab's hand, in rebellion",
          kind="killing", by="joab", of="absalom", war=True)
run_event(w, 12, "— and Absalom's death is the final collection",
          kind="death_in_house", house="david", who="Absalom")
run_event(w, 12, "— it also closes Absalom's own ledger",
          kind="death_in_house", house="absalom", who="his own fall")
run_event(w, 2, "Joab murders Abner at the gate (peacetime, guile)",
          kind="killing", by="joab", of="abner", grade="mezid",
          witnessed=False)
run_event(w, 10, "Joab murders Amasa on the highway",
          kind="killing", by="joab", of="amasa", grade="mezid",
          witnessed=False)
run_event(w, 40, "Solomon has Joab executed at the altar (1 Kgs 2)",
          kind="execution", of="joab")

print("\n".join(w.log))
print("-" * 72)
open_d = w.open_total("david")
open_a = w.open_total("absalom")
print("FINAL LEDGER: david heaven-debt open = %d | absalom open = %d" %
      (open_d, open_a))
print("court docket rows still open: %d" %
      sum(1 for e in w.court_docket if e["open"]))
print()
print("CHECK vs the tradition's own count (the fourfold = the child,")
print("Amnon, Tamar, Absalom):", "BALANCED" if open_d == 0 else "OPEN=%d" % open_d)
