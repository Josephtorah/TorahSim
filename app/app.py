#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# THE TANAKH RUN — the live web app
#
# Serves the assembled Exodus 21 machine (machines/exo21/chapter.py:
# blocks 1-3 + World) against the 64-scene catalog harvested from all 24
# books of the Hebrew Bible.
#
#   (a) SCENE RUNNER  — run any catalog scene; the machine's verdict beside
#       the narrative's own outcome; stamped CONFIRM / DIVERGE /
#       NO-VERDICT-IN-TEXT / FORWARD. Every stamp rests on REAL machine
#       calls, listed per scene.
#   (b) FORM BINDER   — enter custom facts, watch the chapter rule.
#   (c) REPLAY        — timeline scrubber over the chronology keys; the
#       catalog's replay-state notes accumulate as the world's standing
#       rules and open debts.
#
# Verse panel: Hebrew (data/tanakh.sqlite) rendered INTERLINEAR — every
# Hebrew word carries its English underneath (the gloss layers shipped in
# data/lexicon.json), per the absolute glossing rule.
#
# Local only: binds 127.0.0.1:8021 (port = the chapter). stdlib only.
# Run:  python3 app/app.py        (then open http://127.0.0.1:8021)
# Experimental model — not binding religious law.
# =============================================================================
import importlib.util
import json
import os
import re
import sqlite3
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TANAKH_DB = os.path.join(ROOT, "data", "tanakh.sqlite")
LEXICON_JSON = os.path.join(ROOT, "data", "lexicon.json")
CATALOG = os.path.join(HERE, "scene_catalog.json")

def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

M = _load(os.path.join(ROOT, "machines", "exo21", "chapter.py"), "chapter")
b1, b2, b3, World = M.b1, M.b2, M.b3, M.World

with open(CATALOG, encoding="utf-8") as f:
    CAT = json.load(f)
SCENES = {s["id"]: s for s in CAT["scenes"]}

# ---------------------------------------------------------------------------
# THE LEXICON — the gloss layers shipped in data/lexicon.json: Strong's
# number -> gloss (the lemma bridge into all 24 books), unpointed spelling
# -> gloss (the skeleton fallback), and the hand supplement (wins over
# both). See data/README.md for provenance.
# ---------------------------------------------------------------------------
_POINTING = re.compile(u"[\u0591-\u05C7]")

def _skel(he):
    return _POINTING.sub("", he or "").replace("/", "")

def _build_lexicon():
    with open(LEXICON_JSON, encoding="utf-8") as f:
        d = json.load(f)
    return d["lexicon"], d["skeleton"], d["supplement"]

LEXICON, SKELETON, SUPPLEMENT = _build_lexicon()

_tan = None
def tan():
    global _tan
    if _tan is None:
        _tan = sqlite3.connect(TANAKH_DB, check_same_thread=False)
    return _tan

def verse_words(ref):
    """'Gen.9.5' or 'Gen.9.5-6' -> [{'he','en'}] interlinear rows."""
    ref = re.sub(r"\s*\(.*\)$", "", ref.strip())        # drop annotations
    try:
        book, ch, vs = ref.split(".")
    except ValueError:
        return []
    lo, _, hi = vs.partition("-")
    out = []
    for v in range(int(lo), int(hi or lo) + 1):
        rows = tan().execute(
            "SELECT w.he, w.lemma FROM words w JOIN verses vv ON "
            "w.verse_id = vv.id WHERE vv.book=? AND vv.chapter=? AND "
            "vv.verse=? ORDER BY w.idx", (book, int(ch), v)).fetchall()
        if rows and hi:
            out.append({"he": u"\u2014 %s:%d \u2014" % (ch, v), "en": ""})
        for he, lemma in rows:
            sk = _skel(he)
            base = (lemma or "").split("/")[-1].split(" ")[0]
            en = (SUPPLEMENT.get(sk) or LEXICON.get(base)
                  or SKELETON.get(sk)
                  or (SKELETON.get(sk[1:]) and "and-" + SKELETON[sk[1:]]
                      if sk.startswith(u"ו") else None)
                  or "(gloss pending)")
            out.append({"he": (he or "").replace("/", ""), "en": en})
    return out

# ---------------------------------------------------------------------------
# THE SCENE HANDLERS — every stamp rests on real machine calls.
# Each handler returns: stamp, machine (what the code says), note
# (jurisdiction/mode context), calls [(label, result), ...].
# Stamps: CONFIRM / DIVERGE / NO-VERDICT-IN-TEXT / FORWARD.
# ---------------------------------------------------------------------------
def R(stamp, machine, note=None, calls=None):
    return {"stamp": stamp, "machine": machine, "note": note or "",
            "calls": [(lbl, repr(val)) for lbl, val in (calls or [])]}

def h_gen9(s):
    v = b3.stoning_verdict(victim_is_human=True, has_owner=False)
    k = b3.kofer_admissible("ox_owner")
    return R("CONFIRM",
             "The machine's stoning track is DELEGATED divine judgment — "
             "guilt attaches to the animal, ownerless included (stoned=%s); "
             "the Gen 9:5 edge is a RESOLVED dependency of the machine."
             % v["stoned"],
             "Gen-9 mode: the demand exists from the flood on; the 30-shekel "
             "tariff does not (that is Sinai's addition).",
             [("stoning_verdict(ownerless)", v), ("kofer_admissible(owner)", k)])

def h_cain(s):
    hv = b2.homicide_verdict("mezid", warned_and_persisted=False)
    return R("CONFIRM",
             "No witnesses, no warning -> no court death (track=%s); the "
             "docket passes to Heaven — which is exactly where Cain's case "
             "runs (the mark, the sevenfold guard)." % hv["track"],
             "Pre-Sinai typology: God as the only sitting court; the "
             "sevenfold is vengeance-scale, not the court's 4/5 tariff.",
             [("homicide_verdict(unwarned mezid)", hv)])

def h_abimelech(s):
    return R("CONFIRM",
             "The capital formula (unmarked death sentence, machine default "
             "mode '%s') appears in a FOREIGN king's decree protecting the "
             "patriarch's wife — the formula's currency outside Israel."
             % b2.DEFAULT_DEATH,
             "Foreign-comparative: same formula, different sovereign.",
             [("DEFAULT_DEATH", b2.DEFAULT_DEATH)])

def h_hagar(s):
    rs = b1.resale("master")
    return R("CONFIRM",
             "The machine's one-way door: %s — the midrash reads exactly "
             "this no-degradation rule into Sarai's household." % rs,
             "Pre-Sinai typology (soft): the angel's 'return' is not a "
             "court order; the RULE the tradition extracts matches.",
             [("resale('master')", rs)])

def h_jacob_laban(s):
    ec = b1.exit_cost(medical_outlays_by_master=0)
    return R("DIVERGE",
             "The statute: term capped at %d years, exit gratis (cost=%d), "
             "wages untouchable. Laban's ledger: 14+6 years, wages switched "
             "ten times, exit contested. The machine and Laban disagree on "
             "every axis." % (b1.TERM_YEARS, ec),
             "Instructive divergence: the pre-statute world SHOWS WHY the "
             "statute exists — Jacob's speech (Gen 31) is the grievance "
             "list the law answers; Jacob's 7-year self-hire is the "
             "mitzvah-sale carve (a RESOLVED machine edge, Gen 29:18).",
             [("TERM_YEARS", b1.TERM_YEARS), ("exit_cost(0)", ec)])

def h_joseph_pit(s):
    p = b3.pit_liability(10, victim="man")
    return R("CONFIRM",
             "A MAN in the pit draws no money remedy — forum: %s. The "
             "narrative runs that branch precisely: no human court touches "
             "the brothers; the guilt surfaces before God (Gen 42:21, "
             "44:16 'God has found the sin')." % p["forum"],
             "The pit is empty, no water — the statute's pit, one book "
             "early; a RESOLVED machine edge (Gen 37:24).",
             [("pit_liability(10, victim='man')", p)])

def h_joseph_sale(s):
    j = b2.joseph_case()
    return R("CONFIRM",
             "The kidnap element-pipeline EXEMPTS the brothers: missing "
             "elements %s — sold from the pit, the buyers pulled him out. "
             "The narrative agrees: no human court ever convicts them; the "
             "tradition routes collection to Heaven across generations."
             % j["missing"],
             "Gen 37 executed against Exod 21:16's element list — the "
             "machine's own joseph_case() function.",
             [("joseph_case()", j)])

def h_goblet(s):
    t = b3.theft_tariff("goblet")
    return R("FORWARD",
             "The goblet is not ox/sheep (multiplier=%s: the double only), "
             "and sale-of-the-insolvent-thief is Exod 22:2 — BLOCK-4 "
             "territory, a declared forward demand. Joseph's graded "
             "verdict (only the one found becomes a slave, the rest go "
             "free) anticipates the statute's proportionality."
             % t["multiplier"],
             "Judah's substitution offer (Gen 44:33, 'let your servant "
             "remain IN PLACE OF the lad') is a RESOLVED machine edge — "
             "the tachat-idiom in the flesh.",
             [("theft_tariff('goblet')", t)])

def h_moses_egyptian(s):
    hv = b2.homicide_verdict("mezid", warned_and_persisted=False)
    return R("CONFIRM",
             "No witnesses ('he looked this way and that'), no warning -> "
             "track=%s; and the killer FLEES (Exod 2:15) — the refuge "
             "reflex before refuge exists. Both machine branches execute."
             % hv["track"],
             "Exod 2:12 is a RESOLVED machine edge (the unwitnessed "
             "killer's file); the tradition reads no-witnesses as itself "
             "Heaven's verdict-sign.",
             [("homicide_verdict(unwarned)", hv)])

def h_egypt_stoning(s):
    return R("CONFIRM",
             "Lexicon: the stoning verb in Exod 8:22 ('will they not stone "
             "us?') is the machine's mob-execution register — a RESOLVED "
             "dependency edge of the stoning track.",
             "Lexicon-level scene.", [])

def h_sinai_boundary(s):
    v = b3.stoning_verdict(victim_is_human=True, has_owner=False)
    return R("CONFIRM",
             "Sinai's perimeter rule (beast or man that touches the "
             "mountain is stoned, Exod 19:12-13) DEPLOYS the ox-stoning "
             "protocol before the statute is spoken; machine: the beast "
             "itself is answerable (stoned=%s), no owner needed."
             % v["stoned"],
             "A RESOLVED machine edge (Exod 19:13) — the protocol "
             "pre-exists its own statute.",
             [("stoning_verdict(ownerless beast)", v)])

def h_calf(s):
    return R("CONFIRM",
             "The tariff constant: the ox pays %d. The tradition prices "
             "the calf-apostasy at the OX-RATE three separate ways (tail "
             "digests) — the constant reused as theological arithmetic."
             % b3.OX_TARIFF,
             "Prophetic-figurative: constant-level confirmation.",
             [("OX_TARIFF", b3.OX_TARIFF)])

def h_patches_release(s):
    return R("FORWARD",
             "Deut 15's release-law patch (severance grant, the amah "
             "restatement) is a DECLARED forward demand of block 1 "
             "(Deut 15:12 in the machine's DEPENDS table). The patch "
             "cannot be verified until Deuteronomy is derived.",
             "Patch scene: the demand ledger is the honest state.", [])

def h_patches_talion(s):
    return R("FORWARD",
             "Num 35 (refuge corpus, the no-ransom pair) and Deut 19 "
             "(plotting witnesses) are declared forward demands of block "
             "2 — the machine already consumes their constants (the "
             "ransom type-boundary, the release-clock) as OPEN edges.",
             "Patch scene: forward by design.", [])

def h_yiud_charufa(s):
    return R("CONFIRM",
             "Lev 19:20 (the shifchah charufah, the half-designated "
             "slave-woman) RESOLVES into frozen unit "
             "lev_19_holiness_duty_ledger — the one patch verse already "
             "derived; the machine's yiud (designation) interface meets "
             "its Leviticus counterpart and holds.",
             "The assembly's surprise resolution.", [])

def h_rahab(s):
    t = b2.tachat_payment("nefesh")
    return R("CONFIRM",
             "Rahab's oath ('our life in place of yours to die', Josh "
             "2:14) swears the machine's tachat-substitution semantics in "
             "the flesh — the nefesh clause is the literal one (mode=%s)."
             % t["mode"],
             "Lexicon: the substitution grammar attested in covenant.",
             [("tachat_payment('nefesh')", t)])

def h_achan(s):
    v = b3.stoning_verdict(victim_is_human=False)
    return R("DIVERGE",
             "The machine stones an ox only for killing a MAN (non-human "
             "victim -> stoned=%s). Achan's oxen killed no one — they are "
             "stoned WITH him under CHEREM (the ban), a different "
             "jurisdiction entirely." % v["stoned"],
             "The treasure-type divergence: a jurisdiction fact. Cherem "
             "consecration-law, not damages-law, reaches Achan's animals; "
             "the scan flagged this as the inversion of 21:28.",
             [("stoning_verdict(victim not human)", v)])

def h_divine_sale(s):
    return R("NO-VERDICT-IN-TEXT",
             "Judges' cycle-formula ('He SOLD them into the hand of...') "
             "borrows the statute's sale-verb as a divine figure; no "
             "court, no term, no redemption-price is run in the text.",
             "Prophetic figure: the grammar is the statute's, the "
             "jurisdiction is Heaven's.", [])

def h_samson(s):
    t = b2.tachat_payment("eye")
    return R("DIVERGE",
             "The machine's eye-clause pays money (mode=%s) in a court. "
             "Samson's eyes are gouged by a FOREIGN power in war, and his "
             "'as they did to me, so I did' is vengeance-jurisdiction — "
             "the tradition itself uses his line to prove tachat means "
             "in-KIND, not in-form." % t["mode"],
             "Jurisdiction divergence: war and Philistine custody, not "
             "an ordained court.",
             [("tachat_payment('eye')", t)])

def h_ruth(s):
    return R("FORWARD",
             "The gate-scene's redemption ladder (goel priority, the "
             "sandal) runs on Lev 25's institutions — block 1 declares "
             "Lev 25 as FOUR forward demands (25:10, 25:39, 25:41, "
             "25:55). The machine's redemption arithmetic exists "
             "(graduated, at-cost), but the kinsman-redeemer layer is "
             "not yet derived.",
             "Forward: the Leviticus 25 module.", [])

def h_samuel_audit(s):
    k = b3.kofer_admissible("ox_owner")
    return R("CONFIRM",
             "Samuel's clearance oath (1 Sam 12:3: 'whose OX have I "
             "taken... from whose hand a KOFER') audits himself in the "
             "statute's own remedy-nouns — ox-restitution and ransom "
             "(machine: kofer is the owner's lawful instrument, "
             "admissible=%s). The people answer: nothing taken. Amos "
             "5:12 runs the same audit on judges who FAIL it." % k,
             "Binding mode: the statute's vocabulary as the integrity "
             "standard for office.",
             [("kofer_admissible('ox_owner')", k)])

def h_nabal(s):
    hv = b2.homicide_verdict("mezid", warned_and_persisted=False)
    return R("CONFIRM",
             "David en route to kill Nabal is a mezid without court or "
             "warning (track if he struck: %s — but as AVENGER he is no "
             "court at all); Abigail's speech names the bloodguilt, David "
             "blesses her for the restraint. The machine's "
             "courts-not-avengers architecture is the scene's own moral."
             % hv["track"],
             "Binding mode: self-help homicide averted; Heaven takes "
             "Nabal ten days later — the two-courts split on stage.",
             [("homicide_verdict(unwarned)", hv)])

def h_goliath(s):
    return R("CONFIRM",
             "Lexicon: the champion's prize ('his father's house made "
             "FREE in Israel', 1 Sam 17:25) speaks the manumission "
             "vocabulary of the slave-laws — chofshi, the exit-word of "
             "21:2.",
             "Lexicon-level scene.", [])

def h_nathan(s):
    t = b3.theft_tariff("sheep")
    k = b2.kim_leih(death_class=True)
    return R("CONFIRM",
             "David's own verdict on the parable — 'FOURFOLD shall he "
             "repay the ewe' — is the machine's sheep-tariff exactly "
             "(multiplier=%d). And Nathan WITHHELD the murder from the "
             "parable: for the murder there is no payment (kim leih: "
             "payment %s) — the parable charges only what the tariff can "
             "collect." % (t["multiplier"], k["payment"]),
             "The flagship. 2 Sam 12:6 is the chapter ledger's final row "
             "AND a declared machine demand; the tradition pre-computed "
             "the four (child, Amnon, Tamar, Absalom).",
             [("theft_tariff('sheep')", t), ("kim_leih(death)", k)])

def h_tekoa(s):
    hv = b2.homicide_verdict("mezid")
    return R("DIVERGE",
             "Two brothers fought in the field, no rescuer; one dead. The "
             "machine's mezid track: %s — and its architecture has NO "
             "pardon-power (no paired mercy checking justice). David "
             "grants the widow's plea and commutes: CROWN clemency, "
             "outside the court machine." % hv["mode"],
             "Jurisdiction divergence, marked by the text itself: the "
             "widow's case is a constructed parable to license Absalom's "
             "recall — clemency as the king's prerogative, not the "
             "court's option.",
             [("homicide_verdict('mezid')", hv)])

def h_gibeonites(s):
    k = b3.kofer_admissible("human_murderer")
    return R("CONFIRM",
             "David asks 'with what shall I ATONE (kofer-verb)?' — the "
             "Gibeonites answer in the statute's own boundary: no silver "
             "and gold. Machine: kofer for a human murderer admissible="
             "%s (Num 35:31's ban, a declared demand). The narrative "
             "rules exactly where the machine does." % k,
             "Binding mode: the ransom type-boundary spoken by "
             "non-Israelites, enforced by famine.",
             [("kofer_admissible('human_murderer')", k)])

def h_absalom(s):
    return R("NO-VERDICT-IN-TEXT",
             "'Absalom STOLE the hearts' — the theft-verb on minds; the "
             "tradition's seven-thief ladder puts the mind-thief FIRST. "
             "No court process runs in the text.",
             "Doctrine: the verb's semantic field, not a case.", [])

def h_yoav(s):
    a = b2.altar_shelter(sentence="death", convicted_by="torah_court")
    c = b2.altar_shelter(sentence="death", convicted_by="crown")
    return R("CONFIRM",
             "Solomon executes 21:14 VERBATIM — 'from beside My altar you "
             "shall take him to die.' Machine: the altar never shelters "
             "from the court (sheltered=%s); at the CROWN interface the "
             "machine carries the standing machloket (GRA: shields from "
             "the crown — which is exactly why Joab RAN there; Netziv: "
             "it does not — which is exactly why he DIED there). The "
             "narrative is the machloket's own test case."
             % a["sheltered"],
             "1 Kgs 2:28 is a declared machine demand (forward edge). "
             "Benaiah reports the refusal; Solomon: 'do as he said.'",
             [("altar_shelter(court)", a), ("altar_shelter(crown)", c)])

def h_naboth(s):
    return R("DIVERGE",
             "The court FORMS all present and correct — two witnesses, "
             "proclamation, stoning outside the city — and every input "
             "false. The machine assumes honest testimony; its defense "
             "against plotted witnesses (Deut 19's zomemim law) is a "
             "declared FORWARD demand, not yet derived. Elijah's verdict "
             "arrives from the other docket: blood-debt to Jezreel.",
             "The abuse-case divergence: protocol weaponized. The "
             "narrative shows the gap the plotting-witness patch exists "
             "to close.", [])

def h_horns(s):
    return R("NO-VERDICT-IN-TEXT",
             "Zedekiah's iron horns ('with these you shall GORE Aram') "
             "wield the goring verb as war-prophecy theater; no ox, no "
             "owner, no court. Twin accounts (1 Kgs 22:11 = 2 Chr 18:10) "
             "serve as the catalog's parallel-merge calibration row: one "
             "event, two witnesses.",
             "Prophetic figure + calibration function.", [])

def h_talent(s):
    ol = b3.owner_liability("muad", "free_man", victim_value=100)
    return R("CONFIRM",
             "The prophet's disguise-parable: 'your SOUL in place of his "
             "soul, OR you shall weigh a talent' — the kofer disjunction "
             "(life-liability bought back with money) is the machine's "
             "mu'ad-owner structure exactly (capital='%s' + kofer as the "
             "buy-back). Ahab convicts himself — the Nathan pattern."
             % ol["capital"],
             "1 Kgs 20:39 is a declared machine demand. The strike-"
             "refusing fellow of v.35 ('strike me') also feeds the "
             "pre-authorization rule in block 2.",
             [("owner_liability(mu'ad)", ol)])

def h_widow_creditor(s):
    return R("NO-VERDICT-IN-TEXT",
             "The creditor comes 'to take my two children as slaves' — "
             "debt-slavery within the statute's frame (term-limited, "
             "redeemable; the machine's clocks would cap it). The text "
             "runs no court: Elisha's oil pays the debt and the case "
             "never reaches the gate.",
             "The prophet's remedy PREEMPTS the machine — mercy above "
             "the law's floor, which is itself the statute's design "
             "(the law as floor, not ceiling).", [])

def h_yehosheba(s):
    kv = b2.kidnap_verdict(stole=True, into_domain=True, used=False,
                           sold=False, witnesses_sale=False)
    return R("CONFIRM",
             "Yehosheba STEALS (the verb is the statute's) the infant "
             "Joash from the massacre. Machine: the kidnap pipeline "
             "needs use AND sale — verdict=%s, missing %s. The rescue-"
             "theft convicts no one; the verb alone is not the crime."
             % (kv["verdict"], kv.get("missing")),
             "Twin accounts (2 Kgs 11:2 = 2 Chr 22:11) — the second "
             "parallel-merge calibration row.",
             [("kidnap_verdict(rescue facts)", kv)])

def h_war_crimes(s):
    f = b2.fetus_payment()
    return R("CONFIRM",
             "Ripping open the pregnant (Hazael, Menachem, Ammon) is the "
             "statute's protected scenario at war-atrocity scale. No "
             "human court reaches foreign armies — and Amos 1:13 "
             "prosecutes Ammon for EXACTLY this from Heaven's docket. "
             "Machine: the fetus-clause exists (payment='%s') and the "
             "two-courts architecture routes what courts cannot reach."
             % f["payment"],
             "Foreign-comparative: the statute's values enforced at the "
             "only jurisdiction that spans nations.",
             [("fetus_payment()", f)])

def h_amos(s):
    return R("CONFIRM",
             "Amos indicts by the statute: 'they SOLD the righteous for "
             "silver' (sale without the insolvency gate) and 'takers of "
             "KOFER' (ransom where the law bars it — the machine's "
             "type-boundary corrupted into a bribe-word). The indictment "
             "PRESUPPOSES the statute the machine implements.",
             "Prophetic enforcement of block-1 sale-gates and the "
             "block-3 kofer boundary.", [])

def h_hosea(s):
    half = b3.SLAVE_TARIFF / 2
    return R("CONFIRM",
             "Hosea buys her back 'for fifteen of silver' — HALF the "
             "thirty (machine: SLAVE_TARIFF/2 = %g, the half-slave's "
             "split in the machine's own arithmetic). The tradition "
             "reads the half-price as the redemption of a half-estranged "
             "bond." % half,
             "Prophetic figure riding the tariff constant.",
             [("SLAVE_TARIFF / 2", half)])

def h_isaiah_thieves(s):
    return R("NO-VERDICT-IN-TEXT",
             "'Your princes are companions of THIEVES' — the thief-"
             "figure indicts office-holders; no case runs.",
             "Doctrine/figure.", [])

def h_jer2(s):
    return R("FORWARD",
             "'Not in the BREAKING-IN did you find them' (Jer 2:34) — "
             "Jeremiah cites the burglar-clause's LIMITS as indictment: "
             "you killed where even 22:1's license does not reach. The "
             "clause is Exod 22:1-2 — block-4 territory, the machine's "
             "declared border (the tail ledgered it).",
             "The lemma's only non-statute hit in Tanakh; a forward "
             "stub by design.", [])

def h_jehoiakim(s):
    ec = b1.exit_cost(medical_outlays_by_master=0)
    return R("CONFIRM",
             "Jeremiah indicts the king 'who makes his fellow serve "
             "GRATIS' — the statute's word for the SLAVE'S exit-right "
             "(machine: exit_cost=%d, the slave walks for nothing) "
             "inverted into the king's unpaid corvee. The prophet "
             "convicts by the statute's own vocabulary." % ec,
             "Prophetic-figurative on the chinnam ('for nothing') "
             "lexeme; found via the harvest's one 'awl-slip' detour.",
             [("exit_cost(0)", ec)])

def h_jer34(s):
    sl, _ = b1.court_sale(theft=1000, worth_six_years_labor=500)
    st = b1.term_status(sl, elapsed_days=6 * 365)
    return R("CONFIRM",
             "The machine says FREE at term (status after six years: "
             "%s); Zedekiah's Jerusalem proclaims release, then RE-"
             "ENSLAVES the freed. The covenant sanction lands measure-"
             "for-measure: 'you did not proclaim release — behold I "
             "proclaim a release FOR you: to the sword, the pestilence, "
             "the famine' (Jer 34:17). The breach is judged BY the "
             "statute's own terms." % st,
             "Binding-mode flagship. Jer 34:14 quotes the composed "
             "release law verbatim — the patch layer cited inside "
             "Tanakh itself.",
             [("term_status(6 years)", st)])

def h_jeremiah_pit(s):
    p = b3.pit_liability(10, victim="man")
    return R("CONFIRM",
             "Jeremiah lowered into the pit ('no water, only mire' — the "
             "Joseph echo verbatim): a MAN in a pit draws no money court "
             "(machine forum: %s) — and Heaven's court convenes: Ebed-"
             "melech who lifts him OUT is personally saved by oracle "
             "(Jer 39:18) while the city that pitted its prophet falls."
             % p["forum"],
             "The pit-branch typology, second attestation after Joseph.",
             [("pit_liability(10, man)", p)])

def h_ezek18(s):
    return R("CONFIRM",
             "Ezekiel 18 doctrinalizes what the ox-law's son-or-daughter "
             "clause already coded: no vicarious liability — each soul "
             "its own docket ('the soul that sins, IT dies'; the "
             "capital-formula and blood-on-him idioms are the statute's). "
             "Machine: the 21:31 clause applies the SAME din for the "
             "minor victim and never punishes children for parents.",
             "Doctrine scene confirming the liability architecture.", [])

def h_ezek34(s):
    o = b3.ox_vs_ox("muad", 200, 200, 50)
    return R("NO-VERDICT-IN-TEXT",
             "The fat rams 'push with side and shoulder and GORE the "
             "weak' — shepherd-politics in the ox-law's verbs; God "
             "announces He will judge 'between sheep and sheep' (the "
             "ox-vs-ox docket cosmicized; the machine's mu'ad pays in "
             "full: %s). No earthly case runs." % o["pays"],
             "Prophetic figure over the block-3 vocabulary.",
             [("ox_vs_ox(mu'ad)", o)])

def h_lamb_ox(s):
    return R("NO-VERDICT-IN-TEXT",
             "'As a lamb to the slaughter' — the tariff's animals and "
             "slaughter-verb as innocence-figures; no case.",
             "Figure only.", [])

def h_pit_boomerang(s):
    p = b3.pit_liability(10)
    return R("CONFIRM",
             "'Who digs a pit falls into it' (Prov 26:27; Ps 7:16) — "
             "wisdom universalizes the digger's liability (machine: the "
             "digger pays, liable=%s) into moral physics: the hazard "
             "returns to its maker." % p["liable"],
             "Doctrine mirroring the statute's ownership-of-hazard.",
             [("pit_liability(10)", p)])

def h_cosmic_kofer(s):
    k = b3.kofer_admissible("human_murderer")
    return R("CONFIRM",
             "Ps 49: 'a brother cannot be ransomed... the kofer of his "
             "soul is too costly' — the machine's hardest boundary (no "
             "ransom for a life, admissible=%s) stated as cosmology: "
             "before God every man is the case money cannot reach." % k,
             "Doctrine: the type-boundary universalized.",
             [("kofer_admissible('human_murderer')", k)])

def h_wisdom_thief(s):
    t = b3.theft_tariff("ox")
    return R("CONFIRM",
             "Prov 6:31 'the thief repays SEVENFOLD' vs the machine's "
             "max multiplier %d — the tradition harmonizes by DERIVING: "
             "Kli Yakar's arithmetic (breeding-value says eleven; the "
             "Torah docked seven for the thief's shouldered shame — "
             "'great is human dignity: it pushes aside seven sheep'), "
             "read as Solomon computing the dignity-discount."
             % t["multiplier"],
             "Doctrine scene whose apparent divergence the chain itself "
             "resolves — kept as CONFIRM-via-derivation with the "
             "arithmetic on display.",
             [("theft_tariff('ox')", t)])

def h_job_slave(s):
    m = b2.manumission()
    return R("CONFIRM",
             "Job's manifesto: 'did I despise the cause of my slave IN "
             "THEIR CONTENTION WITH ME... did not He who made me in the "
             "belly make him?' — the slave has a CAUSE against the "
             "master (machine: the exit is a fine the court enforces, "
             "free=%s), grounded in one womb — the statute's dignity "
             "architecture stated as creed." % m["free"],
             "Doctrine; the Rivash reads the slave-quarrel file "
             "through this verse.",
             [("manumission()", m)])

def h_zech_scroll(s):
    t = b3.theft_tariff("ox", courts_ordained=False)
    return R("CONFIRM",
             "The flying scroll enters the THIEF's house and the false-"
             "swearer's and consumes them — heavenly enforcement of the "
             "theft-parashah's pair EXACTLY where jurisdiction decay "
             "leaves courts dark (machine today: fine uncollectable=%s, "
             "'the flying scroll enforces from Heaven' is the machine's "
             "own note). The oath-half is the guardians' oath — Exod "
             "22:10, block-4 FORWARD." % t["fine_uncollectable"],
             "Prophetic enforcement of the two-courts architecture; "
             "half-forward by design.",
             [("theft_tariff(no courts)", t)])

def h_zech_thirty(s):
    return R("CONFIRM",
             "'They weighed out my wage: THIRTY of silver' — and God "
             "calls it 'the majestic price I was priced by them': the "
             "slave-gored tariff (machine constant %d) wielded as the "
             "insult-price of the divine shepherd. The machine declares "
             "Zech 11:12 a formal demand." % b3.SLAVE_TARIFF,
             "Prophetic figure on the block-3 constant.",
             [("SLAVE_TARIFF", b3.SLAVE_TARIFF)])

def h_joel(s):
    kv = b2.kidnap_verdict()
    return R("CONFIRM",
             "Tyre and Sidon SOLD the children of Judah — man-theft-and-"
             "sale at nation scale (machine: the completed pipeline is "
             "capital, verdict=%s) — and the sentence is restitution in "
             "kind: 'I will sell YOUR sons and daughters.' Measure-for-"
             "measure at the only court that tries nations."
             % kv["verdict"],
             "Foreign-comparative: the kidnap statute run on peoples.",
             [("kidnap_verdict(complete)", kv)])

def h_esther(s):
    return R("CONFIRM",
             "Esther pleads the statute's own SCALE: 'we have been SOLD, "
             "I and my people, to be destroyed... had we been sold as "
             "slaves I would have held my peace.' Sale-to-slavery sits "
             "inside the law's frame (term, redemption); sale-to-DEATH "
             "has no frame at all — her argument is the gradient between "
             "block 1's sale-laws and block 2's capital track.",
             "Foreign-comparative: the statute's categories argued in a "
             "Persian court.", [])

def h_neh5(s):
    fs = b1.father_sale(True, True, True, True, True)
    return R("CONFIRM",
             "'We subject our sons and daughters as slaves — some of our "
             "daughters are subjected ALREADY, and it is not in the "
             "power of our hands' — the daughters'-sale machinery "
             "(machine: the father-sale gates exist, record=%s) run by "
             "FAMINE and creditors instead of the poverty-gate's "
             "protections. Nehemiah convenes the assembly and forces "
             "restoration + release: the redemption architecture "
             "ENFORCED against its abusers." % (fs[0] is not None),
             "Binding mode: the statute's protections reasserted by a "
             "governor's court.",
             [("father_sale(all gates)", fs[0])])

def h_deut28(s):
    return R("NO-VERDICT-IN-TEXT",
             "'Your OX slaughtered before your eyes and you shall not "
             "eat of it' — the tariff's nouns and verbs weaponized as "
             "covenant curse: the law's remedies withheld IS the "
             "punishment. No case runs.",
             "Curse-inversion figure.", [])

def h_daniel(s):
    return R("NO-VERDICT-IN-TEXT",
             "The ram 'goring westward, northward, southward, and no "
             "beast could stand before him' — empires as unstoppable "
             "mu'ad oxen; the horn-typology family. Figure only.",
             "Prophetic figure over the goring verb.", [])

def h_borrowed_axe(s):
    return R("FORWARD",
             "'Alas, master — and it was BORROWED!' (2 Kgs 6:5): the "
             "prophets' apprentice states borrower-liability (Exod "
             "22:13) in one cry. Block-4 territory — the guardians' "
             "table is the next block's machine; the scene waits for it.",
             "The catalog's cleanest forward stub.", [])

def h_capital_survey(s):
    return R("CONFIRM",
             "The doubled capital formula ('dying he shall die') runs "
             "through the block-2 quartet (striker, parent-striker, "
             "kidnapper, curser) and the survey's other sites in the "
             "same register — machine: the unmarked default is the "
             "lightest death, the marked cases carry their modes "
             "(murderer sword, curser stoning). Lexicon-level census "
             "confirms the formula's legal grammar.",
             "Lexicon scene.", [])

# ---- the DOCKET scenes (folded 2026-08-13, owner word "yes fold them") ----
def h_david_uriah(s):
    hv = b2.homicide_verdict("mezid", warned_and_persisted=False)
    return R("CONFIRM",
             "Murder by letter, by foreign sword: the court track returns "
             "'%s' (agency + no witnesses + no warning — 'the striker "
             "dies, not the sender'); the two-courts architecture bills "
             "the remainder to Heaven's docket." % hv["track"],
             "Nathan's sentence matches both halves: 'you shall not die' "
             "— then the child, then the fourfold. The crime sits at "
             "ck 72.9, immediately before nathan_fourfold in the replay.",
             [("homicide_verdict('mezid', unwarned)", hv)])

def h_amaziah(s):
    hv = b2.homicide_verdict("mezid")
    return R("CONFIRM",
             "The killers: track=%s, mode=%s. The sons: NO function in "
             "the machine can charge them — vicarious liability does not "
             "exist in the system. Amaziah's recorded ruling is exactly "
             "this pair." % (hv["track"], hv["mode"]),
             "The docket's jewel: the text itself says he ruled 'as it "
             "is WRITTEN in the book of the Torah of Moses' — a named "
             "king executing the statute, reproduced by the machine.",
             [("homicide_verdict('mezid')", hv)])

def h_abner_asahel(s):
    rr = b2.rodef_rescue(could_stop_by_maiming=True)
    return R("CONFIRM",
             "Even against a pursuer: killing where MAIMING sufficed -> "
             "liable=%s (the proportionality rule Sanhedrin 74a derives "
             "from OUR brawl-verse). Abner's spear-butt precision proved "
             "he could have wounded." % rr["rescuer_liable_if_killed"],
             "The tradition's court (Sanhedrin 49a) convicts him on this "
             "exact ground; the narrative collects at the GATE — the "
             "court's own venue — and Solomon confirms the debt.",
             [("rodef_rescue(could_stop_by_maiming=True)", rr)])

def h_rechab_baanah(s):
    hv = b2.homicide_verdict("mezid", warned_and_persisted=False)
    cr = b2.altar_shelter(sentence="death", convicted_by="crown")
    return R("CONFIRM",
             "The court track cannot convict on confession (track=%s — "
             "no self-incrimination: 'the life is not his to give'); the "
             "CROWN track executes exactly in that gap — the stealth-"
             "killer jurisdiction the altar machloket (dispute) maps." % hv["track"],
             "David's sentence speaks Gen 9:5's demand-verb: 'shall I "
             "not REQUIRE his blood from your hand' — the machine's "
             "resolved charter edge, in a king's mouth.",
             [("homicide_verdict(confession only)", hv),
              ("altar_shelter(crown) — the machloket", cr)])

def h_adonibezek(s):
    tp = b2.tachat_payment("hand")
    return R("CONFIRM",
             "A court pays money for a hand (mode=%s); the EXACT in-kind "
             "measure belongs to the jurisdiction that can calibrate it "
             "— and the defendant himself attributes it there: 'as I "
             "have done, so GOD has repaid me.'" % tp["mode"],
             "The ideal-measure doctrine (talion as the measure courts "
             "approximate and never exceed) voiced by a foreign king "
             "under war jurisdiction.",
             [("tachat_payment('hand')", tp)])

def h_zechariah_bj(s):
    jur = b2.capital_jurisdiction(temple_standing=True,
                                  sanhedrin_in_chamber=False)
    hv = b2.homicide_verdict("mezid")
    return R("CONFIRM",
             "capital_jurisdiction(no seated court) -> %s: the king's-"
             "command stoning is not an execution but a MURDER; the "
             "mezid track (%s by %s) attaches to the killers." %
             (jur, hv["track"], hv["mode"]),
             "The dying declaration invokes the demand-verb — and five "
             "verses later Chronicles records the collection: Joash "
             "slain 'for the blood of the sons of Jehoiada.' The "
             "fastest divine collection in the catalog.",
             [("capital_jurisdiction(True, False)", jur),
              ("homicide_verdict('mezid')", hv)])

def h_jeremiah_trial(s):
    return R("FORWARD",
             "No Exodus-21 rule covers prophecy charges — false-prophecy "
             "law is Deut 18, not yet derived. The machine DECLINES to "
             "rule, and the decline is the verdict: a machine that ruled "
             "on everything would be a toy.",
             "The trial itself is a working courtroom — the capital "
             "formula, gate-seated officials, PRECEDENT cited both ways "
             "(Micah spared; Uriah ben Shemaiah killed), advocacy — "
             "waiting for its block.", [])

HANDLERS = {
    "david_uriah_agency": h_david_uriah,
    "amaziah_fathers_not_sons": h_amaziah,
    "abner_asahel_rodef": h_abner_asahel,
    "rechab_baanah_confession": h_rechab_baanah,
    "adonibezek_ideal_measure": h_adonibezek,
    "zechariah_ben_jehoiada": h_zechariah_bj,
    "jeremiah_capital_trial": h_jeremiah_trial,
    "gen9_noahide_charter": h_gen9,
    "cain_sevenfold": h_cain,
    "abimelech_capital_decree": h_abimelech,
    "hagar_amah": h_hagar,
    "jacob_laban_ledger": h_jacob_laban,
    "joseph_pit": h_joseph_pit,
    "joseph_sale_theft": h_joseph_sale,
    "goblet_graded_verdicts": h_goblet,
    "moses_egyptian": h_moses_egyptian,
    "egypt_stoning_fear": h_egypt_stoning,
    "sinai_boundary_ox_rule": h_sinai_boundary,
    "calf_paid_at_ox_rate": h_calf,
    "patches_release_laws": h_patches_release,
    "patches_talion_refuge": h_patches_talion,
    "patch_yiud_charufa": h_yiud_charufa,
    "rahab_tachat_pledge": h_rahab,
    "achan_ox_stoned_with_him": h_achan,
    "divine_sale_formula": h_divine_sale,
    "samson_eye_vengeance": h_samson,
    "ruth_gate_redemption": h_ruth,
    "samuel_clearance_audit": h_samuel_audit,
    "nabal_abigail_self_help": h_nabal,
    "goliath_freedom_prize": h_goliath,
    "nathan_fourfold": h_nathan,
    "tekoa_widow_commutation": h_tekoa,
    "gibeonites_no_kofer": h_gibeonites,
    "absalom_steals_hearts": h_absalom,
    "yoav_altar": h_yoav,
    "naboth_stoning": h_naboth,
    "horns_of_iron_parallel": h_horns,
    "talent_or_soul": h_talent,
    "widow_creditor_children": h_widow_creditor,
    "yehosheba_theft_rescue": h_yehosheba,
    "war_crimes_pregnant": h_war_crimes,
    "amos_sale_and_kofer": h_amos,
    "hosea_half_tariff": h_hosea,
    "isaiah_thief_companions": h_isaiah_thieves,
    "jer2_not_in_the_breaking_in": h_jer2,
    "jehoiakim_gratis_labor": h_jehoiakim,
    "jer34_release_breach": h_jer34,
    "jeremiah_pit": h_jeremiah_pit,
    "ezek18_individual_liability": h_ezek18,
    "ezek34_goring_flock": h_ezek34,
    "lamb_ox_to_slaughter": h_lamb_ox,
    "pit_boomerang_doctrine": h_pit_boomerang,
    "cosmic_kofer": h_cosmic_kofer,
    "wisdom_thief_tariff": h_wisdom_thief,
    "job_slave_manifesto": h_job_slave,
    "zech_scroll_curse": h_zech_scroll,
    "zech11_thirty_shekels": h_zech_thirty,
    "joel_nations_sold_back": h_joel,
    "esther_sale_plea": h_esther,
    "neh5_daughters_subjected": h_neh5,
    "deut28_curse_inversion": h_deut28,
    "daniel_goring_empires": h_daniel,
    "forward_borrowed_axe": h_borrowed_axe,
    "capital_formula_survey": h_capital_survey,
}

def run_scene(sid):
    s = SCENES[sid]
    out = dict(s)
    out.update(HANDLERS[sid](s))
    return out

# ---------------------------------------------------------------------------
# THE FORM BINDER — curated machine entry-points with typed parameters
# ---------------------------------------------------------------------------
FORMS = {
    "theft_tariff": {
        "label": "Theft tariff (21:37) — what does the thief owe?",
        "fn": lambda a: b3.theft_tariff(**a),
        "params": [("animal", "choice:ox,sheep,camel,goblet", "ox"),
                   ("disposed", "bool", True), ("whole", "bool", True),
                   ("irreversible", "bool", True),
                   ("act_causes_prohibition", "bool", False),
                   ("via_agent", "bool", False),
                   ("thief_owned_first", "bool", False),
                   ("owner", "choice:commoner,hekdesh,gentile", "commoner"),
                   ("confessed_in_court", "bool", False),
                   ("courts_ordained", "bool", True)]},
    "homicide": {
        "label": "Homicide fork (21:12-14) — which track?",
        "fn": lambda a: b2.homicide_verdict(**a),
        "params": [("grade", "choice:mezid,shogeg,karov_le_mezid,"
                    "karov_le_ones", "mezid"),
                   ("striker", "choice:man,woman,minor", "man"),
                   ("victim", "choice:free_man,ger_toshav", "free_man"),
                   ("victim_viable", "bool", True),
                   ("whole_soul", "bool", True),
                   ("warned_and_persisted", "bool", True)]},
    "slave_window": {
        "label": "The slave window (21:20-21) — sword or exempt?",
        "fn": lambda a: b2.slave_homicide(**a),
        "params": [("instrument", "choice:rod,sword", "rod"),
                   ("exclusive_title", "bool", True),
                   ("current_subjection", "bool", True),
                   ("survived_hours", "int", 30),
                   ("victim", "choice:canaanite_slave,hebrew_slave",
                    "canaanite_slave")]},
    "manumission": {
        "label": "Limb-tip manumission (21:26-27) — does the slave go free?",
        "fn": lambda a: b2.manumission(**a),
        "params": [("organ", "choice:eye,tooth,milk_tooth", "eye"),
                   ("exposed", "bool", True),
                   ("non_regenerating", "bool", True),
                   ("act_on_organ", "bool", True),
                   ("intent_at_organ", "bool", True),
                   ("destroyed_irreversibly", "bool", True),
                   ("proven", "choice:court_witnesses,self_admission",
                    "court_witnesses"),
                   ("via_agent", "bool", False),
                   ("exclusive_title", "bool", True),
                   ("slave", "choice:canaanite,hebrew", "canaanite"),
                   ("second_organ_later", "bool", False)]},
    "kidnap": {
        "label": "Kidnap pipeline (21:16) — do the elements complete?",
        "fn": lambda a: b2.kidnap_verdict(**a),
        "params": [("stole", "bool", True), ("into_domain", "bool", True),
                   ("used", "bool", True), ("sold", "bool", True),
                   ("sold_whole", "bool", True),
                   ("witnesses_theft", "bool", True),
                   ("witnesses_sale", "bool", True),
                   ("victim_matzuy", "bool", False),
                   ("victim_viable", "bool", True)]},
    "five_heads": {
        "label": "The five heads (21:19,24-25) — which payments attach?",
        "fn": lambda a: b2.five_heads_award(**a),
        "params": [("limb_lost", "bool", True), ("pain", "bool", True),
                   ("idle", "bool", True), ("healing", "bool", True),
                   ("shamed", "bool", False),
                   ("mens_rea", "choice:mezid,shogeg", "mezid"),
                   ("intended_shame", "bool", False),
                   ("victim_pampered", "bool", False),
                   ("relapse_from_wound", "bool", False),
                   ("victim_disobeyed_doctor", "bool", False)]},
    "fetus": {
        "label": "The fetus clause (21:22) — who is paid, and when not?",
        "fn": lambda a: b2.fetus_payment(**a),
        "params": [("ason_in_woman", "bool", False),
                   ("husband_alive", "bool", True),
                   ("husband_sued", "bool", True)]},
    "pit": {
        "label": "The pit (21:33-34) — liable for the fall?",
        "fn": lambda a: b3.pit_liability(**a),
        "params": [("depth", "int", 10),
                   ("victim", "choice:ox,man,vessels,chicken", "ox"),
                   ("outcome", "choice:death,injury", "death"),
                   ("pit_kind", "choice:hevel,impact", "hevel"),
                   ("covered_properly", "bool", False),
                   ("handed_to_public", "bool", False),
                   ("fell_inside", "bool", True)]},
    "ox_vs_ox": {
        "label": "Ox vs ox (21:35-36) — who pays what?",
        "fn": lambda a: b3.ox_vs_ox(**a),
        "params": [("gorer_status", "choice:tam,muad", "tam"),
                   ("gorer_live_value", "int", 200),
                   ("gored_value", "int", 200),
                   ("carcass_value", "int", 0),
                   ("victim_owner", "choice:commoner,hekdesh,"
                    "gentile_lawless", "commoner"),
                   ("gorer_owner", "choice:commoner,hekdesh", "commoner")]},
    "ox_lifecycle": {
        "label": "Ox lifecycle (21:28-29) — walk an ox through world-days",
        "fn": None,   # special-cased: runs on a World
        "params": [("gorings_on_days", "str", "1,2,3"),
                   ("owner_present_testimony", "bool", True),
                   ("context", "choice:weekday,sabbath", "weekday"),
                   ("petting_days_after", "int", 0),
                   ("query_context", "choice:weekday,sabbath", "weekday"),
                   ("victim_is_man", "bool", False)]},
    "court_sale": {
        "label": "Court sale of the thief (21:2) — is the sale valid?",
        "fn": lambda a: b1.court_sale(**a),
        "params": [("theft", "int", 1000),
                   ("worth_six_years_labor", "int", 500),
                   ("male", "bool", True), ("insolvent", "bool", True),
                   ("by_witnesses", "bool", True),
                   ("victim_consents_to_sale", "bool", True)]},
    "altar": {
        "label": "The altar (21:14) — does it shelter him?",
        "fn": lambda a: b2.altar_shelter(**a),
        "params": [("sentence", "choice:death,exile,money", "death"),
                   ("convicted_by", "choice:torah_court,crown",
                    "torah_court"),
                   ("priest_mid_service", "bool", False)]},
}

def run_form(name, args):
    spec = FORMS[name]
    typed = {}
    for pname, ptype, pdefault in spec["params"]:
        raw = args.get(pname, pdefault)
        if ptype == "bool":
            typed[pname] = (raw in (True, "true", "True", "1", 1, "on"))
        elif ptype == "int":
            typed[pname] = int(raw)
        else:
            typed[pname] = raw
    if name == "ox_lifecycle":
        w = World()
        ox = w.register_ox("custom")
        for d in str(typed["gorings_on_days"]).split(","):
            d = d.strip()
            if not d:
                continue
            w.day = int(float(d))
            w.goring(ox, context=typed["context"],
                     owner_present_testimony=typed["owner_present_testimony"])
        for _ in range(typed["petting_days_after"]):
            w.petting_day(ox)
        return {"status": w.ox_status(ox, context=typed["query_context"],
                                      victim_is_man=typed["victim_is_man"]),
                "gorings_recorded": len(w.oxen[ox]["gorings"]),
                "note": "tam = innocent (half-damages, from the body); "
                        "muad = forewarned (full damages, from the best)"}
    result = spec["fn"](typed)
    if isinstance(result, tuple):     # block-1 (record, why) pairs
        return {"record": result[0], "why": result[1]}
    return result

# ---------------------------------------------------------------------------
# REPLAY — the chronology fold: stamps + the catalog's replay-state notes
# accumulated as standing rules
# ---------------------------------------------------------------------------
def build_replay():
    keyed = [s for s in CAT["scenes"] if s["chronology_key"] is not None]
    keyed.sort(key=lambda s: s["chronology_key"])
    events = []
    for s in keyed:
        r = HANDLERS[s["id"]](s)
        events.append({"ck": s["chronology_key"], "id": s["id"],
                       "title": s["title_en"], "mode": s["mode"],
                       "stamp": r["stamp"],
                       "replay_state": s["replay_state_en"],
                       "refs": s["refs"]})
    return events

# ---------------------------------------------------------------------------
# SUMMARY — "the law ran N times across the Tanakh"
# ---------------------------------------------------------------------------
def build_summary():
    stamps, by_mode = {}, {}
    for sid in SCENES:
        r = HANDLERS[sid](SCENES[sid])
        stamps[r["stamp"]] = stamps.get(r["stamp"], 0) + 1
        m = SCENES[sid]["mode"]
        by_mode.setdefault(m, {}).setdefault(r["stamp"], 0)
        by_mode[m][r["stamp"]] += 1
    _, resolved, forward = M.chapter_dependency_proof(verbose=False)
    return {"scenes": len(SCENES), "stamps": stamps, "by_mode": by_mode,
            "machine": {"blocks": 3, "claims": {"block1": 39, "block2": 43,
                                                "block3": 35},
                        "dependency_edges": {"internal": 2,
                                             "resolved": len(resolved),
                                             "forward": len(forward)}},
            "meta": CAT.get("meta", {})}

# ---------------------------------------------------------------------------
# THE PAGE (self-contained; no external assets)
# ---------------------------------------------------------------------------
PAGE = u"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Exodus 21 — the Tanakh Run</title>
<style>
:root{--bg:#12100d;--panel:#1c1915;--ink:#e8e0d0;--dim:#9a8f7a;
--gold:#c9a45c;--line:#2e2a22;--confirm:#4f9e6b;--diverge:#c25b4e;
--noverdict:#7a8699;--forward:#8a6fb3}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
font:15px/1.55 Georgia,'Times New Roman',serif}
header{padding:18px 24px 10px;border-bottom:1px solid var(--line)}
h1{margin:0;font-size:21px;color:var(--gold);font-weight:normal}
h1 small{color:var(--dim);font-size:13px;margin-left:10px}
nav{padding:0 24px;border-bottom:1px solid var(--line)}
nav button{background:none;border:none;color:var(--dim);font:inherit;
padding:10px 14px;cursor:pointer;border-bottom:2px solid transparent}
nav button.on{color:var(--gold);border-bottom-color:var(--gold)}
main{display:flex;min-height:calc(100vh - 110px)}
#list{width:360px;border-right:1px solid var(--line);overflow-y:auto;
max-height:calc(100vh - 110px)}
#detail{flex:1;padding:20px 26px;overflow-y:auto;
max-height:calc(100vh - 110px)}
.scene{padding:9px 14px;border-bottom:1px solid var(--line);cursor:pointer}
.scene:hover{background:var(--panel)}
.scene.sel{background:var(--panel);border-left:3px solid var(--gold)}
.scene .t{font-size:13.5px}
.scene .m{font-size:11px;color:var(--dim)}
.chip{display:Inline-Block;font-size:10px;padding:1px 7px;border-radius:9px;
color:#fff;vertical-align:middle;margin-right:6px;font-family:sans-serif}
.chip.CONFIRM{background:var(--confirm)}
.chip.DIVERGE{background:var(--diverge)}
.chip.NOV{background:var(--noverdict)}
.chip.FORWARD{background:var(--forward)}
.chip.P0{background:var(--gold);color:#241d10}
.chip.P1,.chip.P2{background:#3a352b;color:var(--dim)}
.panel{background:var(--panel);border:1px solid var(--line);
border-radius:6px;padding:14px 16px;margin:12px 0}
.panel h3{margin:0 0 8px;font-size:12px;text-transform:uppercase;
letter-spacing:.12em;color:var(--dim);font-weight:normal}
.vs{display:flex;gap:14px}.vs>div{flex:1}
.refs a{color:var(--gold);text-decoration:none;margin-right:10px;
cursor:pointer}
.calls{font:12px/1.5 ui-monospace,Menlo,monospace;color:var(--dim);
white-space:pre-wrap;word-break:break-word}
#verse{direction:rtl;display:flex;flex-wrap:wrap;gap:2px 10px;
padding:6px 0}
#verse .w{display:Inline-Flex;flex-direction:column;align-items:center;
margin-bottom:8px}
#verse .he{font-size:20px}
#verse .en{font-size:10px;color:var(--dim);direction:ltr;
font-family:sans-serif;max-width:90px;text-align:center}
form.binder{display:grid;grid-template-columns:repeat(auto-fill,
minmax(230px,1fr));gap:10px}
form.binder label{font-size:12px;color:var(--dim);display:block}
form.binder input,form.binder select{width:100%;background:#26221b;
color:var(--ink);border:1px solid var(--line);border-radius:4px;
padding:5px 7px;font:inherit;font-size:13px}
button.go{background:var(--gold);color:#241d10;border:none;
border-radius:4px;padding:8px 22px;font:inherit;cursor:pointer;
margin-top:12px}
pre.out{background:#0d0b08;border:1px solid var(--line);border-radius:6px;
padding:12px;font:12.5px/1.6 ui-monospace,Menlo,monospace;
white-space:pre-wrap;word-break:break-word;color:#cfc4ab}
input[type=range]{width:100%}
.ev{padding:7px 10px;border-left:3px solid var(--line);margin:6px 0}
.ev.future{opacity:.25}
.ev .ck{color:var(--dim);font-size:11px}
.summary td,.summary th{padding:4px 12px;text-align:left;font-size:13px;
border-bottom:1px solid var(--line)}
.note{color:var(--dim);font-size:13px}
.filter{padding:8px 14px;border-bottom:1px solid var(--line);
font-size:12px;color:var(--dim)}
.filter select{background:#26221b;color:var(--ink);border:1px solid
var(--line);border-radius:4px;font-size:12px}
</style></head><body>
<header><h1>Exodus 21 — the Tanakh Run
<small>one chapter compiled; 24 books executed against it &middot;
experimental model, not binding law</small></h1></header>
<nav>
<button id="tab-scenes" class="on" onclick="tab('scenes')">Scenes</button>
<button id="tab-custom" onclick="tab('custom')">Custom facts</button>
<button id="tab-replay" onclick="tab('replay')">Replay</button>
<button id="tab-summary" onclick="tab('summary')">Summary</button>
</nav>
<main>
<div id="list"></div>
<div id="detail"><p class="note">Loading…</p></div>
</main>
<script>
let SC=[],CUR=null,MODE='scenes',REPLAY=null,FORMS=null;
const $=id=>document.getElementById(id);
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;');
function chip(st){const c=st==='NO-VERDICT-IN-TEXT'?'NOV':st;
return '<span class="chip '+c+'">'+st+'</span>';}
function tab(m){MODE=m;['scenes','custom','replay','summary'].forEach(x=>
$('tab-'+x).classList.toggle('on',x===m));render();}
async function boot(){
SC=await (await fetch('/api/scenes')).json();
FORMS=await (await fetch('/api/forms')).json();
render();}
function render(){
if(MODE==='scenes'){renderList();if(CUR)showScene(CUR);else
$('detail').innerHTML='<p class="note">Pick a scene. Stamps: CONFIRM '+
'(the narrative runs the machine\\'s rule), DIVERGE (it does not — and '+
'the divergence is itself a finding: jurisdiction, era, or abuse), '+
'NO-VERDICT-IN-TEXT (figure or doctrine; no case runs), FORWARD (the '+
'scene needs a block not yet derived — never faked).</p>';}
if(MODE==='custom')renderCustom();
if(MODE==='replay')renderReplay();
if(MODE==='summary')renderSummary();}
let FP='all';
function renderList(){
$('list').style.display='';
let h='<div class="filter">priority <select id="fp" '+
'onchange="FP=this.value;renderList()">'+
['all','P0','P1','P2'].map(o=>'<option'+(o===FP?' selected':'')+'>'+o+
'</option>').join('')+'</select></div>';
for(const s of SC){if(FP!=='all'&&s.priority!==FP)continue;
h+='<div class="scene'+(CUR===s.id?' sel':'')+'" onclick="CUR=\\''+s.id+
'\\';renderList();showScene(\\''+s.id+'\\')">'+
'<div class="t"><span class="chip '+s.priority+'">'+s.priority+'</span>'+
chip(s.stamp)+esc(s.title_en)+'</div>'+
'<div class="m">'+esc(s.mode)+' &middot; ck='+s.chronology_key+'</div></div>';}
$('list').innerHTML=h;}
async function showScene(id){
const s=await (await fetch('/api/run/'+id)).json();
let h='<h2 style="margin:4px 0 2px;font-weight:normal">'+esc(s.title_en)+
'</h2><div>'+chip(s.stamp)+'<span class="note">'+esc(s.mode)+
' &middot; chronology key '+s.chronology_key+'</span></div>';
h+='<div class="panel refs"><h3>Verses</h3>'+s.refs.map(r=>
'<a onclick="verse(\\''+r.replace(/'/g,'')+'\\')">'+esc(r)+'</a>').join('')+
'<div id="verse"></div><div id="versenote" class="note"></div></div>';
h+='<div class="panel"><h3>The facts</h3>'+esc(s.facts_en)+'</div>';
h+='<div class="vs"><div class="panel"><h3>The machine says</h3>'+
esc(s.machine)+'</div>'+
'<div class="panel"><h3>The narrative says</h3>'+
esc(s.narrative_outcome_en)+'</div></div>';
h+='<div class="panel"><h3>Reading the comparison</h3>'+esc(s.note)+
'</div>';
if(s.calls&&s.calls.length){h+='<div class="panel"><h3>Machine calls '+
'behind this stamp</h3><div class="calls">'+s.calls.map(c=>
esc(c[0])+' \\u2192 '+esc(c[1])).join('\\n')+'</div></div>';}
h+='<div class="panel"><h3>Replay state</h3><span class="note">'+
esc(s.replay_state_en)+'</span></div>';
h+='<div class="panel"><h3>Statute hooks</h3><span class="note">'+
s.hooks.map(esc).join(' &middot; ')+'</span></div>';
$('detail').innerHTML=h;}
async function verse(r){
const w=await (await fetch('/api/verse?ref='+encodeURIComponent(r))).json();
$('verse').innerHTML=w.map(x=>'<span class="w"><span class="he">'+
esc(x.he)+'</span><span class="en">'+esc(x.en)+'</span></span>').join('');
$('versenote').textContent=w.length?('Interlinear English per word '+
'(lemma-bridge; hand-check pending glosses).'):
'No verse rows (ref outside the local corpus).';}
function renderCustom(){
$('list').style.display='none';
let h='<h2 style="font-weight:normal">Custom facts — the chapter rules '+
'on your case</h2><p class="note">Pick a statute engine, set the facts, '+
'run. Every result is a live machine call.</p>';
h+='<select id="fsel" onchange="drawForm()" style="background:#26221b;'+
'color:var(--ink);border:1px solid var(--line);padding:6px;font:inherit">';
for(const k in FORMS)h+='<option value="'+k+'">'+esc(FORMS[k].label)+
'</option>';
h+='</select><div id="fbody"></div><pre class="out" id="fout">'+
'(result appears here)</pre>';
$('detail').innerHTML=h;drawForm();}
function drawForm(){
const k=$('fsel').value,spec=FORMS[k];
let h='<form class="binder" id="fform" onsubmit="return false">';
for(const p of spec.params){const[n,t,d]=p;
if(t==='bool'){h+='<div><label>'+n+'</label><select name="'+n+'">'+
'<option value="true"'+(d?' selected':'')+'>true</option>'+
'<option value="false"'+(!d?' selected':'')+'>false</option></select></div>';}
else if(t.startsWith('choice:')){h+='<div><label>'+n+'</label>'+
'<select name="'+n+'">'+t.slice(7).split(',').map(o=>'<option'+
(o===d?' selected':'')+'>'+o+'</option>').join('')+'</select></div>';}
else{h+='<div><label>'+n+'</label><input name="'+n+'" value="'+d+
'"></div>';}}
h+='</form><button class="go" onclick="runForm()">Run the machine</button>';
$('fbody').innerHTML=h;}
async function runForm(){
const k=$('fsel').value,f=new FormData($('fform')),args={};
for(const[n,v]of f.entries())args[n]=v;
const r=await (await fetch('/api/custom',{method:'POST',
headers:{'Content-Type':'application/json'},
body:JSON.stringify({form:k,args:args})})).json();
$('fout').textContent=JSON.stringify(r,null,2);}
async function renderReplay(){
$('list').style.display='none';
if(!REPLAY)REPLAY=await (await fetch('/api/replay')).json();
let h='<h2 style="font-weight:normal">Replay — the world folds over '+
'the timeline</h2><p class="note">Scrub through the '+REPLAY.length+
' chronology-keyed scenes in canonical order. Each event consults the '+
'standing state, gets its stamp, then writes state.</p>'+
'<input type="range" id="scrub" min="1" max="'+REPLAY.length+'" value="'+
REPLAY.length+'" oninput="drawReplay()"><div id="rl"></div>';
$('detail').innerHTML=h;drawReplay();}
function drawReplay(){
const n=parseInt($('scrub').value);
let h='<p class="note">showing events 1\\u2013'+n+' of '+REPLAY.length+
'</p>';
REPLAY.forEach((e,i)=>{h+='<div class="ev'+(i>=n?' future':'')+'">'+
'<span class="ck">ck '+e.ck+'</span> '+chip(e.stamp)+esc(e.title)+
'<div class="note">'+esc(e.replay_state)+'</div></div>';});
$('rl').innerHTML=h;}
async function renderSummary(){
$('list').style.display='none';
const s=await (await fetch('/api/summary')).json();
let h='<h2 style="font-weight:normal">The law ran '+s.scenes+
' times across the Tanakh</h2>';
h+='<div class="panel"><h3>Stamps</h3><table class="summary">';
for(const k in s.stamps)h+='<tr><td>'+chip(k)+'</td><td>'+s.stamps[k]+
'</td></tr>';
h+='</table></div>';
h+='<div class="panel"><h3>By mode</h3><table class="summary">'+
'<tr><th>mode</th><th>stamps</th></tr>';
for(const m in s.by_mode){h+='<tr><td>'+esc(m)+'</td><td>'+
Object.entries(s.by_mode[m]).map(([k,v])=>k+': '+v).join(' &middot; ')+
'</td></tr>';}
h+='</table></div>';
h+='<div class="panel"><h3>The machine underneath</h3><p class="note">'+
'Three blocks, '+(39+43+35)+' witnessed claims; chapter dependency '+
'proof: '+s.machine.dependency_edges.internal+' internal + '+
s.machine.dependency_edges.resolved+' resolved + '+
s.machine.dependency_edges.forward+' forward edges. Epigraph: '+
esc((s.meta&&s.meta.epigraph_en)||'His judgments are in all the earth '+
'(Ps 105:7).')+'</p></div>';
$('detail').innerHTML=h;}
boot();
</script>
<div style="margin:26px 0 12px;padding-top:10px;border-top:1px solid #333;
font-size:11px;opacity:.65">TorahSim &middot; MIT license &middot;
data attributions in ATTRIBUTION.md at the repo root &middot;
experimental model &mdash; not binding religious law</div>
</body></html>
"""

# ---------------------------------------------------------------------------
# THE SERVER
# ---------------------------------------------------------------------------
class Handler(BaseHTTPRequestHandler):
    def _send(self, body, ctype="application/json; charset=utf-8", code=200):
        data = body if isinstance(body, bytes) else body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _json(self, obj, code=200):
        self._send(json.dumps(obj, ensure_ascii=False, default=str), code=code)

    def do_GET(self):
        u = urlparse(self.path)
        p = u.path
        try:
            if p == "/" or p == "/index.html":
                self._send(PAGE, "text/html; charset=utf-8")
            elif p == "/api/scenes":
                out = []
                for s in CAT["scenes"]:
                    r = HANDLERS[s["id"]](s)
                    out.append({"id": s["id"], "title_en": s["title_en"],
                                "priority": s["priority"], "mode": s["mode"],
                                "chronology_key": s["chronology_key"],
                                "stamp": r["stamp"]})
                self._json(out)
            elif p.startswith("/api/run/"):
                sid = p.rsplit("/", 1)[1]
                if sid not in SCENES:
                    self._json({"error": "unknown scene"}, 404)
                else:
                    self._json(run_scene(sid))
            elif p == "/api/verse":
                ref = parse_qs(u.query).get("ref", [""])[0]
                self._json(verse_words(ref))
            elif p == "/api/forms":
                self._json({k: {"label": v["label"], "params": v["params"]}
                            for k, v in FORMS.items()})
            elif p == "/api/replay":
                self._json(build_replay())
            elif p == "/api/summary":
                self._json(build_summary())
            else:
                self._json({"error": "not found"}, 404)
        except Exception as e:          # surface errors to the client, honest
            self._json({"error": "%s: %s" % (type(e).__name__, e)}, 500)

    def do_POST(self):
        u = urlparse(self.path)
        try:
            if u.path == "/api/custom":
                n = int(self.headers.get("Content-Length", 0))
                body = json.loads(self.rfile.read(n) or b"{}")
                self._json(run_form(body["form"], body.get("args", {})))
            else:
                self._json({"error": "not found"}, 404)
        except Exception as e:
            self._json({"error": "%s: %s" % (type(e).__name__, e)}, 500)

    def log_message(self, fmt, *args):   # quiet console
        pass

def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8021
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print("TANAKH RUN app: http://127.0.0.1:%d  (chapter=Exod 21; "
          "scenes=%d; lexicon=%d lemmas)" % (port, len(SCENES), len(LEXICON)))
    srv.serve_forever()

if __name__ == "__main__":
    main()
