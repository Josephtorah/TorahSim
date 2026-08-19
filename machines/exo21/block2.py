#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# LAW ERA v2 DERIVATION — DRAFT (pre-freeze)
# exo_21 block 2: Exodus 21:12-27 — homicide & refuge, parents, kidnap,
# the injury engine (five heads), slave homicide, the fetus clause,
# eye-for-eye, limb-tip manumission
#
# Derived 2026-08-12 from the COMPLETE oral inversion (block 2: 36 bites,
# 1,639/1,639 rows, census satisfied; chapter ledger 4,903 = census EXACT).
# Witness layer:
#   scans/manifests/law02_exo_21_12_27_claims.json (L12..L26, L0)
# Every rule below carries its claim-ID; every claim carries its sources.
#
# STATUS: DRAFT. Chapter scan gate is GREEN; the v2 YAML + freeze land after
# chapter assembly. Experimental model — not binding religious law.
# =============================================================================

# ---------------------------------------------------------------------------
# CONSTANTS — the block's numbers (each with its derivation status)
# ---------------------------------------------------------------------------
DEATH_SEVERITY = ("stoning", "burning", "sword", "chenek")  # severe->light [L12-04]
DEFAULT_DEATH = "chenek"   # unmarked מות יומת ("he shall surely die")     [L12-04]
MURDER_DEATH = "sword"     # נקם ינקם ("avenged be avenged") + eglah hekesh [L12-04]
CURSER_DEATH = "stoning"   # דמיו בו ("his blood is on him")               [L17-01]
WINDOW_HOURS = 24          # יום או יומים = me'et le'et (time-to-time)     [L20-01]
TECHUM_CUBITS = 2000       # the makom->makom chain off the refuge verse   [L13-03]
LIMB_TIPS = 24             # rashei evarim (exposed, non-regenerating)     [L26-01]
FIVE_HEADS = ("nezek", "tzaar", "shevet", "rippui", "boshet")            # [L19-01]
CAPITAL_CEASED_YEARS_BEFORE_CHURBAN = 40   # the jurisdictional clock      [L14-03]

# ---------------------------------------------------------------------------
# CASE — the homicide fork over the two-verse grid (21:12-14)   [L12, L13, L14]
# grades: mezid / shogeg / karov_le_mezid / karov_le_ones
# ---------------------------------------------------------------------------
def homicide_verdict(grade, striker="man", victim="free_man",
                     victim_viable=True, whole_soul=True,
                     warned_and_persisted=True):
    """The mens-rea fork. Victim gates run first (the two-verse grid closes
    each verse's gaps), then causation, then jurisdiction, then intent."""
    if striker == "minor":
        return {"track": "exempt", "note": "minor-striker excluded by verse — "
                "the child matures OUT of cruelty [L12-01]"}
    if not victim_viable:
        return {"track": "exempt",
                "note": "nefalim: the victim must be bar kayama [L12-01]"}
    if not whole_soul:
        return {"track": "exempt", "note": "ten men with ten sticks: ALL "
                "exempt — only the taker of the whole soul; the FINISHER of "
                "a beaten man is that taker [L12-02]"}
    if victim == "ger_toshav":
        return {"track": "heaven", "note": "רעהו ('his fellow') exclusion — "
                "'exempt before courts of flesh and blood, his judgment "
                "handed to Heaven' [L12-03]"}
    if grade == "mezid":
        if not warned_and_persisted:
            return {"track": "no_court_death",
                    "note": "no hatraah -> can plead shogeg; the kipah cell "
                    "and crown-law tracks remain [L14-01]"}
        return {"track": "death", "mode": MURDER_DEATH,
                "note": "warned and STILL willful — the imperfect aspect of "
                "וכי יזד ('if he schemes') carries the law [L14-01]"}
    if grade == "shogeg":
        return {"track": "exile", "note": "pure accident: refuge absorbs [L13-01]"}
    if grade == "karov_le_mezid":
        return {"track": "avenger_exposed", "refuge": False,
                "note": "meant two cubits, threw four — above refuge's band; "
                "the avenger who kills him goes free [L13-01]"}
    return {"track": "exempt", "note": "karov le-ones: guilt too small to "
            "need atonement [L13-01]"}

def refuge(grade, avenger_exists=True, high_priest_died=False):
    """Refuge absorbs the pure shogeg only; the institution is ATONEMENT
    (runs even with no avenger — the slave victim proves it). [L13-01,L13-04]"""
    absorbs = grade == "shogeg"
    return {"absorbs": absorbs,
            "boundary_cubits": TECHUM_CUBITS,        # city + surround [L13-03]
            "atonement": True, "needs_avenger": False,
            "bones_carried_after_death": True,
            "term": "unfixed — until the high priest dies: a divinely-"
                    "indexed variable sentence [L13-04]",
            "released": high_priest_died,
            "one_exile_covers_many_killings": True}

def divine_scheduler(old_killer, new_killer):
    """והאלהים אנה לידו ('and God caused it to meet his hand'): the inn.
    Two unwitnessed killers -> one event pays both ledgers. [L13-02]"""
    assert old_killer == "mezid_unwitnessed" and new_killer == "shogeg_unwitnessed"
    return {"the_mezid": "dies under the ladder (sentencing algebra: the "
                         "sudden harsher death equals the anticipated lighter)",
            "the_shogeg": "falls, kills him, exiles WITH witnesses this time",
            "engine": "God supplies the CAUSE, not the event"}

# ---------------------------------------------------------------------------
# CASE — the altar and the jurisdiction clock (21:14)            [L14-02..03]
# ---------------------------------------------------------------------------
def altar_shelter(sentence="death", convicted_by="torah_court",
                  priest_mid_service=False):
    """מעם מזבחי תקחנו למות ('from beside My altar you shall take him to
    die') — the altar as a jurisdictional filter. [L14-02]"""
    if sentence != "death":
        return {"sheltered": True,
                "note": "taken 'to die' ONLY — money, lashes, exile sheltered"}
    if convicted_by == "torah_court":
        return {"sheltered": False,
                "taken": "after finishing the service" if priest_mid_service
                         else "at once (מעם not מעל — the not-yet-started)"}
    # crown-law / extra-Torah executions: the standing machloket, ON RECORD
    return {"sheltered": None, "machloket": {
        "GRA": "the altar shields FROM crown-law until beit-din convicts",
        "Netziv": "the stealth-killer clause IS crown-law — no shield "
                  "even from the king"}}

def capital_jurisdiction(temple_standing, sanhedrin_in_chamber):
    """The clock: both keys or no capital courts. [L14-03]"""
    return temple_standing and sanhedrin_in_chamber

def override_lattice():
    """The execution calendar, stabilized by the מושבות ("your dwellings")
    gezerah shavah (verbal analogy). [L14-03]"""
    return {"execution_overrides_temple_service": True,
            "execution_overrides_shabbat": False,
            "capital_trial_on_friday": False,   # the verdict would sink
            "pikuach_nefesh_overrides_shabbat": True,  # derived from OUR clause
            "source": "R. Shimon b. Menasya's kal-vachomer on מעם מזבחי"}

# ---------------------------------------------------------------------------
# CASE — the parent laws (21:15, 21:17)                          [L15, L17]
# ---------------------------------------------------------------------------
def parent_strike(wound=True, parent_alive=True, parent_wicked=False,
                  parent_repented=False, healing_context=False,
                  authorized_beforehand=False):
    if healing_context:
        return {"verdict": "permitted",
                "note": "the healing carve — but prefer another physician "
                "(YD 241) [L15-03]"}
    if authorized_beforehand:
        return {"verdict": "exempt", "note": "pre-authorization removes the "
                "lav (the 'strike me' of 1 Kgs 20:35) [L15-03]"}
    if parent_wicked and not parent_repented:
        return {"verdict": "exempt", "note": "'one who acts as your people' "
                "— forbidden, exempt-if-done; boshet still owed [L15-03]"}
    if not parent_alive:
        return {"verdict": "exempt_capital",
                "note": "strike after death exempt — a wound needs flesh; "
                "the CURSE differs [L17-01]"}
    if not wound:
        return {"verdict": "damages_only",
                "note": "chaburah required — even a drop of congealed "
                "blood counts [L15-01]"}
    return {"verdict": "death", "mode": DEFAULT_DEATH,
            "either_parent_suffices": True,   # vav = OR [L15-01]
            "evidence": "rov: 'most intercourse follows the husband' — "
                        "courts execute on presumptions [L15-02]"}

def parent_curse(name_used=True, after_death=False, epithet_only=False):
    if epithet_only:
        return {"verdict": "lashes", "note": "curse by kinnui: lav [L15-03]"}
    if not name_used:
        return {"verdict": "no_capital",
                "note": "the curse must carry the NAME [L17-01]"}
    return {"verdict": "death", "mode": CURSER_DEATH,
            "after_death_liable": True,       # the curse wounds the soul
            "note": "words over deeds: striker strangled, curser stoned — "
                    "the curse bears the Name, reaches past death [L17-01]"}

# ---------------------------------------------------------------------------
# CASE — kidnap (21:16)                                          [L16-01..04]
# ---------------------------------------------------------------------------
def kidnap_verdict(stole=True, into_domain=True, used=True, sold=True,
                   sold_whole=True, witnesses_theft=True, witnesses_sale=True,
                   victim_matzuy=False, victim_viable=True):
    """The element pipeline: ALL gates or exempt. [L16-01]"""
    if victim_matzuy:
        return {"verdict": "exempt", "note": "מצוי — the regularly-present "
                "(father, teacher, guardian) cannot be 'found' [L16-01]"}
    if not victim_viable:
        return {"verdict": "exempt", "note": "bar kayama required [L12-01]"}
    missing = [name for ok, name in (
        (stole, "theft"), (into_domain, "his domain (ונמצא בידו)"),
        (used, "use (והתעמר בו)"), (sold, "sale"),
        (sold_whole, "sold WHOLE, not half"),
        (witnesses_theft, "witnesses on the theft"),
        (witnesses_sale, "witnesses on the sale")) if not ok]
    if missing:
        return {"verdict": "exempt", "missing": missing}
    return {"verdict": "death", "mode": DEFAULT_DEATH,
            "azharah": "the Decalogue's לא תגנב ('you shall not steal') — "
                       "capital by its neighbors [L16-02]",
            "yeush": "never lapses — no owner-despair on a person [L16-01]"}

def joseph_case():
    """Gen 37 run against the element list: sold FROM THE PIT, the buyers
    pulled him out — possession/use unmet -> exempt. [L16-04]"""
    return kidnap_verdict(stole=True, into_domain=False, used=False, sold=True)

# ---------------------------------------------------------------------------
# CASE — the injury engine (21:18-19)                            [L18-01..03]
# ---------------------------------------------------------------------------
def assess_instrument(produced_in_court=True, lethal_capable_at_spot=True):
    """Omed: instrument AND spot must be death-capable, and the court must
    see the instrument. [L18-01]"""
    if not produced_in_court:
        return {"capital_track": False,
                "damages": "the victim swears and collects (CM 420:28)"}
    return {"capital_track": lethal_capable_at_spot,
            "poles": "stone = instrument-lethality, fist = spot-lethality"}

def injury_case(assessed_for="death", outcome="walked_on_health"):
    """The Tosefta BK 9:2 typed state machine. [L18-02, L18-03]"""
    if assessed_for == "death":
        if outcome == "died":
            return {"verdict": "death", "mode": MURDER_DEATH,
                    "custody_held": True}
        if outcome == "walked_on_health":
            return {"verdict": "cleared", "custody_released": True,
                    "pays": ("shevet", "rippui"),
                    "note": "ונקה המכה = released from prison; walking = "
                    "on HIS OWN health (Onkelos על בוריה) [L18-02]"}
        if outcome == "improved_then_died":
            return {"verdict": "liable (the sages: died of the first blow)",
                    "minority": "R. Nechemiah: the walking acquitted him",
                    "second_assessment": "payment retroactive FROM THE BLOW"}
    if assessed_for == "life" and outcome == "died":
        return {"verdict": "exempt_capital", "pays_heirs": FIVE_HEADS,
                "note": "יעמד is a COURT verb: assessed to stand = acquitted "
                "even if he later dies [L18-03]"}
    return {"verdict": "money_track", "pays": FIVE_HEADS}

# ---------------------------------------------------------------------------
# CASE — the five heads (21:19, 24-25 + Deut 25:11)              [L19-01..03]
# ---------------------------------------------------------------------------
def five_heads_award(limb_lost=True, pain=True, idle=True, healing=True,
                     shamed=False, mens_rea="mezid", intended_shame=False,
                     victim_pampered=False, relapse_from_wound=False,
                     victim_disobeyed_doctor=False):
    """One damage event, five heads, each with its own formula, its own
    mens-rea gate, and its own nullability. [L19-01, L19-02]"""
    award = {}
    if limb_lost:
        award["nezek"] = ("market worth before minus after (slave-valuation)"
                          " — strict liability: אדם מועד לעולם, awake or "
                          "asleep, even ones [L19-02]")
    if pain and mens_rea == "mezid":
        award["tzaar"] = ("pay-to-avoid: drug instead of knife" +
                          ("; DOUBLED — the pampered man's pain [L19-01]"
                           if victim_pampered else
                           "; owed even at zero damage (spit-burn, stones, snow)"))
    if idle and mens_rea == "mezid":
        award["shevet"] = ("idle cucumber-watchman wage — the hand-price was "
                           "already paid under nezek (anti-double-count)")
    if healing and mens_rea == "mezid" and not victim_disobeyed_doctor:
        award["rippui"] = ("EARMARKED to the physicians — the victim cannot "
                           "pocket it; no self-healing offer, no free doctor "
                           "[L19-03]" +
                           ("; relapse from the wound: liable AGAIN "
                            "(the doubled verb)" if relapse_from_wound else ""))
    if shamed and intended_shame:
        award["boshet"] = ("by the shamer and the shamed (Deut 25:11) — "
                           "the only head that requires INTENT [L19-02]")
    return award

def physicians_license():
    """ורפא ירפא ('heal, he shall heal') — medicine authorized at our verse,
    codified to YD 336:1. [L19-03]"""
    return {"license": True, "mitzvah": True, "within": "pikuach nefesh",
            "erred_with_court_license": "exempt below, liable in Heaven's court",
            "killed_and_knows_it": "exile",
            "counter_pole_on_record": "Ibn Ezra — man-inflicted external "
                                      "wounds only; God's blow God heals"}

# ---------------------------------------------------------------------------
# CASE — kim leih (the one-penalty family)                       [L12-05]
# ---------------------------------------------------------------------------
def kim_leih(death_class=False, heaven_capital=False, payment_same_act=True,
             sequential=False):
    """Death-class liability swallows co-liable payment — ONE wickedness;
    Heaven's ason (karet) welds in via Gen 42:38; sequential acts split."""
    if (death_class or heaven_capital) and payment_same_act and not sequential:
        return {"payment": "absorbed",
                "note": "even the coat-hole is not collected (Hirsch's "
                "dignity rationale) [L12-05]"}
    return {"payment": "owed"}

def lashes_vs_payment(injury_case_=True):
    """Ulla: where money and lashes meet -> pay, don't flog; the Yom-Kippur
    injurer is the lone explicit exception (רק שבתו יתן 'only his idleness
    he shall give' — a ribui, an expander). [L12-05]"""
    return "pay, don't flog" if injury_case_ else "flog"

# ---------------------------------------------------------------------------
# CASE — slave homicide (21:20-21)                               [L20-01..03]
# ---------------------------------------------------------------------------
def slave_homicide(instrument="rod", exclusive_title=True,
                   current_subjection=True, survived_hours=30,
                   victim="canaanite_slave"):
    """The two-key gate + rod-only + the 24-hour window."""
    if victim != "canaanite_slave":
        return {"verdict": "regular homicide law",
                "note": "the Hebrew slave is an Israelite in every law; "
                "עבד ואמה paired = Canaanite (the Gra's class-rule) [L20-03]"}
    if instrument != "rod":
        return {"verdict": "death", "mode": MURDER_DEATH,
                "note": "sword-class assessed-lethal: murder-mode, executed "
                "even a year later (Rambam 2:14) [L20-02]"}
    if not (exclusive_title and current_subjection):
        return {"verdict": "death", "mode": MURDER_DEATH,
                "note": "the two-key gate: כספו (exclusive title) AND תחתיו "
                "(current subjection) — seller/buyer/partners/half-slave "
                "all fail [L20-01]"}
    if survived_hours >= WINDOW_HOURS:
        return {"verdict": "exempt",
                "note": "כי כספו הוא ('for he is his money') — the survived "
                "window attributes death to a new cause [L20-01, L20-02]"}
    return {"verdict": "death", "mode": MURDER_DEATH,
            "goel": "the community of Israel — the slave has no kin, so "
                    "Israel rises as his blood-avenger [L20-03]"}

# ---------------------------------------------------------------------------
# CASE — the fetus clause (21:22-23)                             [L22-01..03]
# ---------------------------------------------------------------------------
def fetus_payment(ason_in_woman=False, husband_alive=True,
                  conception_husband="the husband at conception",
                  husband_sued=True):
    """דמי ולדות ('fetus-value'): a right of the husband's line, timestamped
    at conception; extinguished by the greater liability."""
    if ason_in_woman:
        return {"payment": 0, "note": "the greater swallows — kim leih on "
                "one victim carrying both money and death [L12-05, L22-02]"}
    if not husband_sued:
        return {"payment": 0, "note": "the husband must CLAIM — no suit, no "
                "collection; the AMOUNT is the court's (בפללים) [L22-03]"}
    return {"payment": "assessed fine, judges cap",
            "includes": "the pregnancy premium",
            "to": conception_husband if husband_alive
                  else "the woman herself (the line lapsed)",
            "note": "fetus not a nefesh until birth — עובר ירך אמו (its "
                    "mother's limb) [L22-02]"}

def transferred_intent(meant="man", force_sufficient_for_intended=True,
                       equally_vulnerable_spot=True):
    """The Sanhedrin 9:2 force-vector matrix + the live tannaitic fork.
    [L22-01]"""
    if meant in ("beast", "gentile", "nonviable"):
        return {"verdict": "exempt", "note": "the intent-object was outside "
                "the statute"}
    if not (force_sufficient_for_intended and equally_vulnerable_spot):
        return {"verdict": "exempt", "note": "sufficiency is evaluated on "
                "the INTENDED vector"}
    return {"verdict": "machloket",
            "sages": "liable — real execution (the brawl is intended killing)",
            "rebbi": "money — נפש תחת נפש = payment (netinah↔netinah)"}

def rodef_rescue(could_stop_by_maiming):
    """Sanhedrin 74a FROM our verse: the surviving payment obligation proves
    the licensed response was sub-lethal. [claims: L12-05 family]"""
    return {"rescuer_liable_if_killed": could_stop_by_maiming}

# ---------------------------------------------------------------------------
# CASE — the tachat series (21:23-25)                            [L24-01..03]
# ---------------------------------------------------------------------------
def tachat_payment(item):
    """The type boundary: נפש literal, everything else money — Num 35:31
    bars ransom for a LIFE, 'but you DO take ransom for limbs'. [L24-01]"""
    if item == "nefesh":
        return {"mode": "death", "ransom": False,
                "note": "no kofer for the murderer (Num 35:31); Rebbi's "
                "money-reading preserved as the fork's other voice [L22-01]"}
    return {"mode": "money", "ransom": True,
            "assessment": "slave-market before minus after [L24-01]",
            "semantics": "תחת = the ANTECEDENT cause (vs נפש בנפש of the "
                         "plotting witnesses — the cause yet to come); "
                         "Onkelos: חלף ('in exchange for') [L24-02]",
            "ideal_measure": "liability literal, execution monetary — the "
                             "measure courts approximate, never exceed "
                             "[L24-03]"}

# ---------------------------------------------------------------------------
# CASE — limb-tip manumission (21:26-27)                         [L26-01..05]
# ---------------------------------------------------------------------------
def manumission(organ="eye", exposed=True, non_regenerating=True,
                act_on_organ=True, intent_at_organ=True,
                destroyed_irreversibly=True, proven="court_witnesses",
                via_agent=False, exclusive_title=True, slave="canaanite",
                second_organ_later=False):
    """The exit predicate + the kenas machinery + composition."""
    if slave != "canaanite":
        return {"free": False, "note": "the Hebrew slave never exits by "
                "tooth/eye — לא תצא כצאת העבדים [L26-05]"}
    if via_agent:
        return {"free": False, "note": "agency shields the exit as it "
                "shielded the sword: 'the striker dies, not the sender' "
                "[L26-02]"}
    if not exclusive_title:
        return {"free": False, "note": "melog/tzon-barzel split title fails "
                "כספו in both directions [L26-05]"}
    if proven == "self_admission":
        return {"free": False, "note": "the exit is a KENAS — modeh bi-knas "
                "patur (R. Gamliel could not free Tabi) [L26-02]"}
    if not (exposed and non_regenerating):
        return {"free": False, "note": "the predicate pair: exposed AND "
                "non-returning (milk-tooth regrows; castration not exposed) "
                "[L26-01]"}
    if not act_on_organ:
        return {"free": False, "note": "shouted beside his ear: no physical "
                "act ON the organ — flight was possible [L26-01]"}
    if not intent_at_organ:
        return {"free": False, "note": "a stone thrown at an animal frees "
                "no one — עד שיתכוון [L26-01]"}
    if not destroyed_irreversibly:
        return {"free": False, "note": "dimmed sight / removable film: "
                "destruction must be real [L26-01]"}
    return {"free": True,
            "classification": "KENAS — flat award exceeding the damage: "
                              "care owed slaves EXCEEDS care owed free men "
                              "[L26-02]",
            "mechanism": "the self-payment loop: the master cannot pay his "
                         "own slave, so the money becomes his RANSOM from "
                         "his master's hand [L26-03]",
            "writ": "machloket — R. Shimon: get shichrur required "
                    "(shiluach↔shiluach); R. Meir: free from the blow "
                    "[L26-05]",
            "second_organ": ("PAID like any injured freeman — exit and "
                             "damages compose [L26-05]"
                             if second_organ_later else None),
            "aetiology": "slavery entered through Ham's eye and mouth; it "
                         "exits through eye and tooth [L26-04]"}

# ---------------------------------------------------------------------------
# SYSTEM RULES                                                    [L0-01..03]
# ---------------------------------------------------------------------------
def ein_onshin_min_hadin():
    """No punishment from inference: derivable != enforceable; k"v may
    SPECIFY (gilui milta) but never create liability. [L0-01]"""
    return {"kv_creates_liability": False, "kv_specifies_written_law": True,
            "guards_third_parties": "the rodef-inversion: a k\"v leniency "
            "to the master would convict the slave's RESCUER"}

def class_exit_ledger():
    """The yatza-mi-klalo ('it exited its class') operator, three runs in
    one block. [L0-02]"""
    return {"parent_striker": "exits the payment class STRICTER (death)",
            "slave_death": "exits the homicide class LENIENT (the window)",
            "slave_maiming": "exits work-them-forever STRICTER on the master "
                             "(emancipation)",
            "davar_chadash": "a total exit never back-propagates — no "
                             "free-man day-window ever",
            "return_clause": "כי כספו הוא restores the slave to the class "
                             "after 24 hours"}

def two_tablets_map():
    """Mishpatim as the Decalogue's enforcement layer. [L0-03]"""
    return {"slave_laws": "the first word of the first tablet (out of the "
                          "house of slaves)",
            "homicide": "לא תרצח ('you shall not murder') — warned there, "
                        "punished here",
            "kidnap": "לא תגנב ('you shall not steal') — the azharah slot "
                      "[L16-02]"}

# ===========================================================================
# THE RUN — assertion battery
# ===========================================================================
def run():
    # --- the homicide fork --------------------------------------------------
    v = homicide_verdict("mezid")
    assert v["track"] == "death" and v["mode"] == "sword", "the murderer's sword"
    assert homicide_verdict("mezid", striker="woman")["track"] == "death", \
        "woman-striker liable — the two-verse grid [L12-01]"
    assert homicide_verdict("mezid", striker="minor")["track"] == "exempt", \
        "minor-striker excluded [L12-01]"
    assert homicide_verdict("mezid", victim_viable=False)["track"] == "exempt", \
        "nefalim excluded [L12-01]"
    assert homicide_verdict("mezid", whole_soul=False)["track"] == "exempt", \
        "ten sticks: all exempt [L12-02]"
    assert homicide_verdict("mezid", victim="ger_toshav")["track"] == "heaven", \
        "רעהו exclusion -> Heaven's docket [L12-03]"
    assert homicide_verdict("mezid",
                            warned_and_persisted=False)["track"] == "no_court_death", \
        "no hatraah -> no court death [L14-01]"
    assert homicide_verdict("shogeg")["track"] == "exile"
    klm = homicide_verdict("karov_le_mezid")
    assert klm["track"] == "avenger_exposed" and klm["refuge"] is False, \
        "above refuge's band [L13-01]"
    assert homicide_verdict("karov_le_ones")["track"] == "exempt", \
        "below refuge's band [L13-01]"
    assert DEATH_SEVERITY.index("sword") < DEATH_SEVERITY.index("chenek"), \
        "sword severer than chenek; stoning tops [L12-04]"

    # --- refuge & the scheduler ----------------------------------------------
    r = refuge("shogeg")
    assert r["absorbs"] and r["atonement"] and not r["needs_avenger"], \
        "exile is atonement — the avenger-less slave proves it [L13-04]"
    assert r["boundary_cubits"] == TECHUM_CUBITS == 2000, \
        "the makom->makom chain: refuge measures the Shabbat domain [L13-03]"
    assert not refuge("karov_le_mezid")["absorbs"]
    assert refuge("shogeg", high_priest_died=True)["released"], \
        "the divinely-indexed term ends with the high priest [L13-04]"
    inn = divine_scheduler("mezid_unwitnessed", "shogeg_unwitnessed")
    assert "ladder" in inn["the_mezid"] and "exiles" in inn["the_shogeg"], \
        "Reish Lakish's inn [L13-02]"

    # --- the altar & the clock -----------------------------------------------
    assert altar_shelter(sentence="exile")["sheltered"], \
        "taken 'to die' only [L14-02]"
    assert altar_shelter()["sheltered"] is False, "no shelter from the court"
    assert "finishing" in altar_shelter(priest_mid_service=True)["taken"], \
        "מעם not מעל — mid-service finishes [L14-02]"
    crown = altar_shelter(convicted_by="crown")
    assert "GRA" in crown["machloket"] and "Netziv" in crown["machloket"], \
        "the crown-interface machloket ON RECORD [L14-02]"
    assert capital_jurisdiction(True, True)
    assert not capital_jurisdiction(True, False), \
        "the Sanhedrin exiled from its chamber: the clock stops [L14-03]"
    lat = override_lattice()
    assert lat["execution_overrides_temple_service"]
    assert not lat["execution_overrides_shabbat"]
    assert not lat["capital_trial_on_friday"]
    assert lat["pikuach_nefesh_overrides_shabbat"], \
        "life-saving derived from the executioner's clause [L14-03]"

    # --- the parent laws -----------------------------------------------------
    ps = parent_strike()
    assert ps["verdict"] == "death" and ps["mode"] == "chenek"
    assert ps["either_parent_suffices"], "vav = OR [L15-01]"
    assert "rov" in ps["evidence"], "executed on presumptions [L15-02]"
    assert parent_strike(wound=False)["verdict"] == "damages_only", \
        "chaburah required [L15-01]"
    assert parent_strike(parent_alive=False)["verdict"] == "exempt_capital", \
        "strike-after-death exempt [L17-01]"
    assert parent_strike(parent_wicked=True)["verdict"] == "exempt"
    assert parent_strike(parent_wicked=True,
                         parent_repented=True)["verdict"] == "death", \
        "repentance flips liability back on [L15-03]"
    assert parent_strike(healing_context=True)["verdict"] == "permitted", \
        "the bloodletting carve [L15-03]"
    assert parent_strike(authorized_beforehand=True)["verdict"] == "exempt", \
        "pre-authorization removes the lav [L15-03]"
    pc = parent_curse()
    assert pc["verdict"] == "death" and pc["mode"] == "stoning"
    assert pc["after_death_liable"], "the curse reaches past death [L17-01]"
    assert parent_curse(name_used=False)["verdict"] == "no_capital"
    assert parent_curse(epithet_only=True)["verdict"] == "lashes"

    # --- kidnap ---------------------------------------------------------------
    k = kidnap_verdict()
    assert k["verdict"] == "death" and k["mode"] == "chenek"
    assert "לא תגנב" in k["azharah"], "the Decalogue azharah [L16-02]"
    assert kidnap_verdict(sold_whole=False)["verdict"] == "exempt", \
        "sold whole, not half [L16-01]"
    assert kidnap_verdict(victim_matzuy=True)["verdict"] == "exempt", \
        "the matzuy exclusion [L16-01]"
    assert kidnap_verdict(used=False)["verdict"] == "exempt", \
        "והתעמר בו — the use element [L16-01]"
    j = joseph_case()
    assert j["verdict"] == "exempt" and len(j["missing"]) == 2, \
        "Gen 37 vs the element list: the brothers exempt [L16-04]"

    # --- the injury engine ----------------------------------------------------
    a = assess_instrument(produced_in_court=False)
    assert not a["capital_track"] and "swears" in a["damages"], \
        "lost instrument: money-track, victim swears [L18-01]"
    assert assess_instrument()["capital_track"], "omed green"
    ic = injury_case("death", "walked_on_health")
    assert ic["verdict"] == "cleared" and ic["custody_released"], \
        "ונקה המכה = out of prison [L18-02]"
    assert ic["pays"] == ("shevet", "rippui")
    assert injury_case("death", "died")["mode"] == "sword"
    itd = injury_case("death", "improved_then_died")
    assert "sages" in itd["verdict"] and "Nechemiah" in itd["minority"], \
        "the state machine's contested edge [L18-03]"
    heirs = injury_case("life", "died")
    assert heirs["verdict"] == "exempt_capital" and heirs["pays_heirs"] == FIVE_HEADS, \
        "assessed-to-live who died: heirs paid [L18-03]"

    # --- the five heads --------------------------------------------------------
    full = five_heads_award(shamed=True, intended_shame=True,
                            victim_pampered=True, relapse_from_wound=True)
    assert set(full) == set(FIVE_HEADS), "all five heads live"
    assert "DOUBLED" in full["tzaar"], "subjective pain [L19-01]"
    assert "liable AGAIN" in full["rippui"], "the relapse ladder [L19-03]"
    shogeg = five_heads_award(mens_rea="shogeg", shamed=True)
    assert list(shogeg) == ["nezek"], \
        "the shogeg pays NEZEK only — per-head mens-rea gates [L19-02]"
    unintended = five_heads_award(shamed=True, intended_shame=False)
    assert "boshet" not in unintended, "boshet alone requires intent [L19-02]"
    assert "rippui" not in five_heads_award(victim_disobeyed_doctor=True), \
        "honey against orders: רק exempts [L19-03]"
    lic = physicians_license()
    assert lic["license"] and lic["mitzvah"], "ורפא ירפא codified [L19-03]"
    assert lic["killed_and_knows_it"] == "exile"

    # --- kim leih ---------------------------------------------------------------
    assert kim_leih(death_class=True)["payment"] == "absorbed", \
        "the block-seam law: no money where he dies [L12-05]"
    assert kim_leih(heaven_capital=True)["payment"] == "absorbed", \
        "the ason-weld: Heaven's docket absorbs too [L12-05]"
    assert kim_leih(death_class=True, sequential=True)["payment"] == "owed", \
        "sequential acts split [L12-05]"
    assert kim_leih()["payment"] == "owed"
    assert lashes_vs_payment() == "pay, don't flog", "Ulla's rule [L12-05]"

    # --- slave homicide -----------------------------------------------------------
    sh = slave_homicide()
    assert sh["verdict"] == "exempt", "rod + two keys + survived window"
    assert slave_homicide(survived_hours=23)["verdict"] == "death", \
        "died within 24 hours: the sword [L20-01]"
    assert slave_homicide(instrument="sword")["verdict"] == "death", \
        "rod-only: sword-class is murder-mode even a year later [L20-02]"
    assert slave_homicide(exclusive_title=False)["verdict"] == "death", \
        "the two-key gate: no title, no window [L20-01]"
    assert slave_homicide(current_subjection=False)["verdict"] == "death", \
        "no subjection, no window [L20-01]"
    hb = slave_homicide(victim="hebrew_slave")
    assert hb["verdict"] == "regular homicide law", \
        "the Hebrew slave is an Israelite in every law [L20-03]"
    died = slave_homicide(survived_hours=10)
    assert "community of Israel" in died["goel"], \
        "Israel is the slave's blood-avenger [L20-03]"
    assert WINDOW_HOURS == 24, "me'et le'et [L20-01]"

    # --- the fetus clause ------------------------------------------------------------
    f = fetus_payment()
    assert f["payment"] != 0 and "conception" in f["to"], \
        "timestamped at conception [L22-02]"
    assert fetus_payment(ason_in_woman=True)["payment"] == 0, \
        "the greater swallows [L22-02]"
    assert fetus_payment(husband_sued=False)["payment"] == 0, \
        "the husband must claim; the amount is the court's [L22-03]"
    assert "woman herself" in fetus_payment(husband_alive=False)["to"], \
        "the line lapsed: she keeps it [L22-02]"
    ti = transferred_intent()
    assert ti["verdict"] == "machloket" and "money" in ti["rebbi"], \
        "the live tannaitic fork [L22-01]"
    assert transferred_intent(meant="beast")["verdict"] == "exempt", \
        "intent-object outside the statute [L22-01]"
    assert transferred_intent(force_sufficient_for_intended=False)["verdict"] \
        == "exempt", "sufficiency on the INTENDED vector [L22-01]"
    assert rodef_rescue(could_stop_by_maiming=True)["rescuer_liable_if_killed"], \
        "the proportionality rule FROM our verse"

    # --- the tachat series ------------------------------------------------------------
    eye = tachat_payment("eye")
    assert eye["mode"] == "money" and eye["ransom"], \
        "eye for eye = money; ransom avails for limbs [L24-01]"
    nefesh = tachat_payment("nefesh")
    assert nefesh["mode"] == "death" and not nefesh["ransom"], \
        "Num 35:31 bars ransom for a LIFE — the type boundary [L24-01]"
    assert "חלף" in eye["semantics"], "Onkelos's exchange-word [L24-02]"
    for limb in ("tooth", "hand", "foot", "burn", "wound", "bruise"):
        assert tachat_payment(limb)["mode"] == "money", \
            "the whole tachat-series pays (Ben Azzai) [L24-02]"

    # --- manumission ---------------------------------------------------------------------
    m = manumission()
    assert m["free"] and "KENAS" in m["classification"], \
        "the flat exceeding award is a fine [L26-02]"
    assert "RANSOM" in m["mechanism"], "the self-payment loop [L26-03]"
    assert "Ham" in m["aetiology"], "the measure-for-measure undoing [L26-04]"
    assert manumission(proven="self_admission")["free"] is False, \
        "modeh bi-knas — Tabi stays a slave [L26-02]"
    assert manumission(via_agent=True)["free"] is False, \
        "agency shields the exit [L26-02]"
    assert manumission(organ="milk_tooth",
                       non_regenerating=False)["free"] is False, \
        "the milk-tooth regrows [L26-01]"
    assert manumission(act_on_organ=False)["free"] is False, \
        "shouted beside the ear: not freed [L26-01]"
    assert manumission(intent_at_organ=False)["free"] is False, \
        "a stone at an animal frees no one [L26-01]"
    assert manumission(destroyed_irreversibly=False)["free"] is False, \
        "dimmed sight is not destruction [L26-01]"
    assert manumission(exclusive_title=False)["free"] is False, \
        "split title fails both directions [L26-05]"
    assert manumission(slave="hebrew")["free"] is False, \
        "the Hebrew fence [L26-05]"
    seq = manumission(second_organ_later=True)
    assert seq["free"] and "PAID" in seq["second_organ"], \
        "exit and damages compose [L26-05]"
    assert LIMB_TIPS == 24, "the rashei evarim [L26-01]"

    # --- system rules ------------------------------------------------------------------------
    eo = ein_onshin_min_hadin()
    assert not eo["kv_creates_liability"] and eo["kv_specifies_written_law"], \
        "derivable != enforceable; gilui milta lives [L0-01]"
    ce = class_exit_ledger()
    assert "STRICTER" in ce["parent_striker"] and "LENIENT" in ce["slave_death"]
    assert "no free-man day-window" in ce["davar_chadash"], \
        "davar chadash never back-propagates [L0-02]"
    tt = two_tablets_map()
    assert "לא תרצח" in tt["homicide"] and "לא תגנב" in tt["kidnap"], \
        "the enforcement layer, tablet by tablet [L0-03]"

    print("BLOCK 2 DRAFT: all asserts GREEN.")
    print("homicide fork / refuge / altar / parents / kidnap / injury engine /"
          " five heads / kim leih / slave window / fetus / tachat / manumission"
          " / system rules: OK")

# ===========================================================================
# CROSS-VERSE DEPENDENCY PROOF (block-1 pattern)
# ===========================================================================
DEPENDS = [
    ("the azharah the block enforces", "Exodus", 20, 13, "back", "L0-03",
     "לא תרצח + לא תגנב — the Decalogue warned; Mishpatim punishes"),
    ("the parent-laws' declaration layer", "Exodus", 20, 12, "back", "L15-01",
     "כבד את אביך — the honor-command whose dark twin is 21:15/17"),
    ("the block seam itself", "Exodus", 21, 11, "back", "L12-05",
     "אין כסף closing block 1 — kim leih read off the seam"),
    ("the sword's charter", "Genesis", 9, 6, "back", "L12-04",
     "שפך דם האדם — the image-of-God ground the murder-law executes"),
    ("the manumission aetiology", "Genesis", 9, 22, "back", "L26-04",
     "וירא ויגד ('he saw, and told') — the curse the exit undoes"),
    ("the kidnap statute's test case", "Genesis", 37, 28, "back", "L16-04",
     "Joseph sold from the pit — the element list runs and exempts"),
    ("the ason-genus import", "Genesis", 42, 38, "back", "L12-05",
     "פן יקראנו אסון — Jacob's word welds Heaven's docket to man's"),
    ("the tachat-idiom in the flesh", "Genesis", 44, 33, "back", "L24-02",
     "ישב נא עבדך תחת הנער — Judah offers substitution in person"),
    ("the unwitnessed killer's file", "Exodus", 2, 12, "back", "L13-02",
     "Moses and the Egyptian — no witnesses is itself Heaven's sign"),
    ("the techum's other anchor", "Exodus", 16, 29, "back", "L13-03",
     "אל יצא איש ממקומו — the manna verse the makom-chain welds to refuge"),
    ("the healing counter-pole", "Exodus", 15, 26, "back", "L19-03",
     "אני ה' רפאך — soft divine healing vs our hard ורפא ירפא (dagesh-law)"),
    ("the plague-verb defined here", "Exodus", 12, 23, "back", "L22-01",
     "נגף — Shemot Rabbah defines Egypt's blow by OUR ונגפו אשה הרה"),
    # ---- forward demands: verses consumed but NOT yet derived ----
    ("the Emor complement", "Leviticus", 24, 20, "fwd", "L24-01",
     "שבר תחת שבר + כן ינתן בו — the two-verse grid's other half"),
    ("the ransom type-boundary", "Numbers", 35, 31, "fwd", "L24-01",
     "לא תקחו כפר לנפש רצח — why נפש is literal and עין is money"),
    ("the refuge release-clock", "Numbers", 35, 25, "fwd", "L13-04",
     "until the death of the high priest — the divinely-indexed term"),
    ("the preposition system's other pole", "Deuteronomy", 19, 21, "fwd", "L24-02",
     "נפש בנפש — the plotting witnesses' bet vs our tachat"),
    ("the kidnap parallel", "Deuteronomy", 24, 7, "fwd", "L16-01",
     "והתעמר בו ומכרו — the use-element's own verse"),
    ("boshet's source verse", "Deuteronomy", 25, 11, "fwd", "L19-01",
     "ושלחה ידה — the fifth head's intent requirement"),
    ("the strike-azharah", "Deuteronomy", 25, 3, "fwd", "L15-01",
     "לא יוסיף — every death-liability needs its lav"),
    ("the class the exit carves", "Leviticus", 25, 46, "fwd", "L26-03",
     "לעלם בהם תעבדו — work-them-forever, exited stricter on the master"),
    ("the curser's stoning anchor", "Leviticus", 20, 9, "fwd", "L17-01",
     "דמיו בו — the gezerah shavah that fixes stoning"),
    ("the altar-clause at monarchy scale", "I Kings", 2, 28, "fwd", "L14-02",
     "Joab grasps the horns — 21:14 executed verbatim (tanakh-run flagship)"),
    ("the guile paradigm", "II Samuel", 3, 27, "fwd", "L14-01",
     "Joab lures Abner into the gate — בערמה in narrative"),
    ("the inn-parable's David locus", "I Samuel", 24, 14, "fwd", "L13-02",
     "משל הקדמני — 'from the wicked comes forth wickedness'"),
]

def _frozen_spans():
    import json, re, os
    path = os.path.join(os.path.dirname(__file__),
                        "..", "..", "data", "units_index.json")
    spans = []
    with open(path, encoding="utf-8") as f:
        units = json.load(f)["units"]
    for u in units:
        m = re.match(r"^(\d+):(\d+)-(?:(\d+):)?(\d+)$", u["refs"].strip())
        if not m:
            continue
        c1, v1 = int(m.group(1)), int(m.group(2))
        c2 = int(m.group(3)) if m.group(3) else c1
        v2 = int(m.group(4))
        spans.append((u["book"], c1, v1, c2, v2, u["unit_id"]))
    return spans

def verify_dependencies(verbose=True):
    spans = _frozen_spans()
    def resolve(book, ch, vs):
        for b, c1, v1, c2, v2, uid in spans:
            if b != book:
                continue
            if (ch, vs) >= (c1, v1) and (ch, vs) <= (c2, v2):
                return uid
        return None
    resolved, forward = [], []
    for elem, book, ch, vs, expect, claim, what in DEPENDS:
        uid = resolve(book, ch, vs)
        row = (elem, "%s %d:%d" % (book, ch, vs), claim, what, uid)
        if uid:
            resolved.append(row)
        else:
            forward.append(row)
        assert (uid is not None) == (expect == "back"), \
            "dependency misdeclared: %s <- %s (%s)" % (elem, row[1], uid)
    if verbose:
        print("\nDEPENDENCY PROOF — %d edges verified against units_index.json:"
              % len(DEPENDS))
        print("  RESOLVED (source verse inside a frozen unit): %d" % len(resolved))
        for elem, ref, claim, what, uid in resolved:
            print("    %-36s <- %-14s [%s] unit=%s" % (elem[:36], ref, claim, uid))
        print("  FORWARD demands (source verse NOT yet derived): %d" % len(forward))
        for elem, ref, claim, what, uid in forward:
            print("    %-36s <- %-14s [%s] OPEN" % (elem[:36], ref, claim))
    return resolved, forward

if __name__ == "__main__":
    run()
    verify_dependencies()
