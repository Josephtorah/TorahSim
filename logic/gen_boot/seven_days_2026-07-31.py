#!/usr/bin/env python3
"""seven_days_2026-07-31.py — the seven days of creation as a running program.

LEARNING EXERCISE (owner order, 2026-07-31). This file is a RENDERING of the
seven logic-derived units — it is NOT the logic. Under the Pre-Code rule the
logic lives hand-authored in the frozen YAML units and the interpreter only
reads them; this file re-states what those derivations found, as one
continuous runnable program, so the week can be watched booting end to end.

Sources (the truth this file is drawn from):
    logic/units/gen_01_creation_boot.yaml        day 1  (frozen)
    logic/units/gen_02_raqia_day.yaml            day 2  (frozen)
    logic/units/gen_03_double_build.yaml         day 3  (frozen)
    logic/units/gen_04_lights_calendar.yaml      day 4  (frozen)
    logic/units/gen_05_swarms_blessing.yaml      day 5  (frozen)
    logic/units/gen_06_land_adam_dominion.yaml   day 6  (draft, pre-flight green)
    logic/units/gen_07_completion_sanctity.yaml  day 7  (draft, pre-flight green)

The machine model: six registers + a flag list.
    TIME      — anchors and marks (t0 = reshit, "beginning")
    WORLD     — entities that exist, and standing facts about them
    REGISTRY  — names and offices (written only by NAME and ASSIGN)
    SPECS     — demands issued by speech, waiting for receipts
    TESTS     — the tov ("good") inspections
    LEDGER    — committed days (the evening-morning close-outs)
    FLAGS     — machine observations; flags NEVER block (dual-track rule)

Contracts carried over from the interpreter, unchanged:
  * A demand coded jussive ("let-there-be" form) is a clean LET.
  * A demand coded IMPERFECT in command position is LET? — and the question
    mark NEVER auto-upgrades (TIR-028). Same for the first-person-plural
    volitive CMD-US? ("let US make", TIR-033, coded imperfect at Gen 1:26).
  * A receipt (va-yehi khen, "and it was so" — or delivery itself) pops the
    matching demand; the recorded mood stays exactly as issued, forever.
  * A blessing's mandate is standing WORLD fact, never a SPECS push: the
    text closes each day clean, and the machine must not falsify that.
  * Flags ride the ledger; they never stop a commit.

Every Hebrew term is glossed in English inline — absolute project rule.

Run:  python3 logic/gen_boot/seven_days_2026-07-31.py
"""

# ---------------------------------------------------------------------------
# the machine
# ---------------------------------------------------------------------------

class Week:
    def __init__(self):
        self.TIME = {"t0": None, "marks": []}
        self.WORLD = {"entities": {}, "facts": [], "invariants": [], "partitions": []}
        self.REGISTRY = {"names": {}, "roles": {}}
        self.SPECS = []          # each: {demand, mood, satisfied}
        self.TESTS = []          # each: (oracle, theme)
        self.LEDGER = {}         # day -> {label, form, clean}
        self.FLAGS = []          # each: (kind, detail)
        self.TRIPLES = []        # design contracts: {q, discharged}
        self._tests_at_last_commit = 0   # the real units are standalone; in this
        # continuous rendering, commit must judge only the CURRENT day's tests

    # -- helpers ------------------------------------------------------------
    def say(self, msg):
        print("    " + msg)

    def flag(self, kind, detail):
        self.FLAGS.append((kind, detail))
        self.say("FLAG  %s: %s" % (kind, detail))

    # -- operators ----------------------------------------------------------
    def time_anchor(self, t0):
        self.TIME["t0"] = t0
        self.say("TIME  t0 := %s" % t0)

    def presupposed(self, *names):
        # read-before-install: the text USES these without ever creating them
        for n in names:
            self.WORLD["entities"].setdefault(n, "presupposed")
            self.flag("read_before_install", n)

    def install(self, *names):
        for n in names:
            self.WORLD["entities"][n] = "created"
        self.say("WORLD += {%s}" % ", ".join(names))

    def declare(self, demand, mood):
        assert mood in ("LET", "LET?", "LET-NOT", "CMD-US?")
        self.SPECS.append({"demand": demand, "mood": mood, "satisfied": False})
        self.say("DECLARE %s(%s)" % (mood, demand))

    def receipt(self, demand, how):
        # va-yehi khen ("and it was so"), or receipt by the delivery itself
        for s in self.SPECS:
            if s["demand"] == demand and not s["satisfied"]:
                s["satisfied"] = True
                self.say("RESULT  HOLDS(%s)  [%s; mood stays %s]"
                         % (demand, how, s["mood"]))
                return
        # a receipt with no matching demand is itself worth seeing
        self.say("RESULT  HOLDS(%s)  [%s; no matching demand]" % (demand, how))

    def design(self, q):
        # a purpose clause: a contract with no receipt anywhere in the span
        self.TRIPLES.append({"q": q, "discharged": False})
        self.say("TRIPLE  design { Q: %s }  (no receipt scheduled)" % q)

    def event(self, desc):
        self.say("EVENT   %s" % desc)

    def partition(self, a, b):
        self.WORLD["partitions"].append((a, b))
        self.say("PARTITION  %s ∩ %s = ∅" % (a, b))

    def invariant(self, p):
        self.WORLD["invariants"].append(p)
        self.say("INVARIANT  %s" % p)

    def name(self, entity, given):
        # the va-yiqra ("and He called") naming formula — days 1-3 only
        self.REGISTRY["names"][entity] = given
        self.say("NAME    %s := %s" % (entity, given))

    def assign(self, entity, role):
        # dative role/office binding (day 4 precedent) — no naming formula
        if self.WORLD["entities"].get(entity) is None:
            self.flag("assigned_before_any_presence", entity)
        self.REGISTRY["roles"][entity] = role
        self.say("ASSIGN  %s -> %s" % (entity, role))

    def bless(self, recipient, mandate=()):
        # mandate items become STANDING WORLD FACTS — never SPECS pushes
        for item in mandate:
            self.WORLD["facts"].append("mandate: " + item)
        self.say("BLESS   %s%s" % (recipient,
                 "  MANDATE {%s}" % ", ".join(mandate) if mandate else
                 "  (no mandate — standing conferred, nothing commissioned)"))

    def spec_delta(self, spec, delivered):
        self.flag("spec_delta", "spec '%s' -> delivered '%s'" % (spec, delivered))

    def test(self, oracle, theme):
        self.TESTS.append((oracle, theme))
        self.say("TEST    PASS(%s, %s)" % (oracle, theme))

    def commit(self, day, label, form):
        open_specs = [s for s in self.SPECS if not s["satisfied"]]
        assert not open_specs, "commit with open demands: %r" % open_specs
        if len(self.TESTS) == self._tests_at_last_commit:
            # S6 policy: a missing test is a FLAG (pattern deviation), never a block
            self.flag("commit_without_test", "day %d closes with no test of its own" % day)
        self._tests_at_last_commit = len(self.TESTS)
        self.LEDGER[day] = {"label": label, "form": form, "clean": True}
        self.say("COMMIT  cycle(erev -> boqer); LEDGER[day %d] := %s (%s)"
                 % (day, label, form))


# ---------------------------------------------------------------------------
# the seven days, as derived
# ---------------------------------------------------------------------------

def day1(m):
    """Gen 1:1-5 — boot. The verse pair {precondition block} + {first fiat}."""
    print("\n=== DAY 1 — or (light): the boot (Gen 1:1-5)")
    m.time_anchor("reshit")                       # reshit = "beginning"
    m.event("bara (created): Elohim -> shamayim (heavens), aretz (earth)")
    m.install("shamayim", "aretz")                # installed by narration, not naming
    # 1:2 is pure precondition: no narrative verb fires in it
    m.say("STATE   tohu va-vohu (unformed-and-void) over aretz;"
          " choshekh (darkness) over tehom (deep)")
    m.invariant("ruach Elohim (breath/wind of God) hovering over mayim (waters)")
    m.presupposed("choshekh", "tehom", "mayim", "ruach")   # read uninitialized
    m.declare("exists(or)", "LET")                # yehi or — "let there be light"
    m.receipt("exists(or)", "va-yehi or, same verse — latency zero")
    m.install("or")
    m.test("tov", "or")                           # tov = "good"
    m.partition("or", "choshekh")
    m.name("or", "yom")                           # yom = "day"
    m.name("choshekh", "layla")                   # layla = "night"
    m.commit(1, "yom echad", "CARDINAL")          # echad = "one" — not "first":
    # the only cardinal day label of the week; days 2-6 are ordinals.


def day2(m):
    """Gen 1:6-8 — raqia (firmament). The first LET? and the first missing test."""
    print("\n=== DAY 2 — raqia (firmament): the divider (Gen 1:6-8)")
    m.declare("exists(raqia)", "LET")             # yehi raqia — jussive, clean
    m.declare("mavdil(raqia, mayim|mayim)", "LET?")
    # ^ vi-yhi MAVDIL ("and let it be DIVIDING") — imperfect-coded job demand:
    #   the corpus's first mandatory question mark (TIR-028).
    m.invariant("mavdil (dividing) waters-below | waters-above, standing")
    m.presupposed("mayim")                        # gen_01 installed; standalone read
    m.event("asah (made): Elohim -> raqia")
    m.install("raqia")
    m.partition("mayim_under", "mayim_over")
    m.receipt("exists(raqia)", "va-yehi khen ('and it was so')")
    m.receipt("mavdil(raqia, mayim|mayim)", "the divide event discharges the job")
    m.name("raqia", "shamayim")                   # the firmament NAMED "heavens"
    m.commit(2, "yom sheni", "ORDINAL")           # sheni = "second"
    # No tov ("good") anywhere on day 2 — the famous missing test.
    # The machine FLAGS it and commits anyway: flags never block.


def day3(m):
    """Gen 1:9-13 — the double build: gathering + the first delegation."""
    print("\n=== DAY 3 — yabasha + deshe (dry land + vegetation): double build (Gen 1:9-13)")
    m.declare("gathered(mayim, to=maqom_echad)", "LET")   # maqom echad = "one place"
    m.declare("exists(yabasha)", "LET?")          # yabasha = "dry land"; imperfect
    m.receipt("gathered(mayim, to=maqom_echad)", "va-yehi khen — receipt BEFORE the delivery narrative")
    m.receipt("exists(yabasha)", "the dry appears")
    m.install("yabasha")
    m.name("yabasha", "eretz")                    # eretz = "earth/land"
    m.name("miqveh_ha_mayim", "yamim")            # yamim = "seas"
    # ^ the NAMING SERIES ENDS HERE — no va-yiqra ("and He called") ever again.
    m.test("tov", "gathering")
    m.declare("sprout(aretz, vegetation)", "LET") # tadshe ha-aretz — DELEGATION:
    m.invariant("esev mazria zera (herb seed-causing seed); etz oseh pri"
                " (tree making fruit); le-mino (by its kind)")
    m.receipt("sprout(aretz, vegetation)", "va-yehi khen — again before execution")
    m.event("va-totze ha-aretz (and the earth BROUGHT FORTH) — the delegate performs")
    m.install("deshe")                            # deshe = "grass/vegetation"
    m.spec_delta("etz pri oseh pri (fruit-tree making fruit)",
                 "etz oseh pri (tree making fruit) — one word short")
    m.spec_delta("esev mazria zera", "esev mazria zera LE-MINEHU — kind-key added")
    m.test("tov", "vegetation")
    m.commit(3, "yom shlishi", "ORDINAL")         # shlishi = "third"


def day4(m):
    """Gen 1:14-19 — the luminaries: offices, over-delivery, first ASSIGN."""
    print("\n=== DAY 4 — me'orot (luminaries): the calendar machine (Gen 1:14-19)")
    m.declare("exists(meorot, loc=raqia_ha_shamayim)", "LET")
    m.presupposed("raqia_ha_shamayim")            # day-2 product, standalone read
    m.receipt("exists(meorot, loc=raqia_ha_shamayim)", "va-yehi khen pops the job-list")
    m.event("asah (made): maor_gadol (greater light), maor_qaton (lesser light)"
            " — and the kokhavim (stars), unordered")
    m.install("maor_gadol", "maor_qaton", "kokhavim")
    m.assign("maor_gadol", "memshelet_yom")       # memshelet = "dominion/office of day"
    m.assign("maor_qaton", "memshelet_lailah")    # office of night — FIRST ASSIGN
    m.spec_delta("me'orot (one undifferentiated plural)",
                 "shnei ha-me'orot ha-GEDOLIM (the two GREAT lights), then gadol/qaton")
    m.spec_delta("no stars in the job order", "ve-et ha-kokhavim — appended, office-less")
    m.spec_delta("jobs: divide, signs, festivals, days+years, shine",
                 "le-memshelet (for dominion) ADDED at delivery")
    m.test("tov", "meorot")
    m.commit(4, "yom revi'i", "ORDINAL")          # revi'i = "fourth"


def day5(m):
    """Gen 1:20-23 — swarms and the first blessing. The deviation day."""
    print("\n=== DAY 5 — sheretz + of (swarms + fliers): first life, first blessing (Gen 1:20-23)")
    m.declare("swarm(mayim, product=sheretz_nefesh_chaya)", "LET?")
    # ^ yishretzu — QAL IMPERFECT, not jussive-coded: mandatory ? forever.
    m.declare("fly(of, loc=pnei_raqia_ha_shamayim)", "LET?")
    # ^ ye'ofef — second imperfect. And NO va-yehi khen follows — the ONLY
    #   work-day fiat of the week with no receipt token anywhere in its span.
    m.presupposed("pnei_raqia_ha_shamayim")
    m.event("BARA returns (first since 1:1): et-ha-taninim ha-gedolim"
            " (the great sea-monsters) lead the inventory, unordered")
    m.install("taninim", "nefesh_chaya_romeset", "of_kanaf")
    m.receipt("swarm(mayim, product=sheretz_nefesh_chaya)",
              "asher SHARTZU ha-mayim — receipt relocated into a relative clause:"
              " the demand verb returns as a PERFECT, crediting the delegate")
    m.receipt("fly(of, loc=pnei_raqia_ha_shamayim)", "receipt by delivered inventory alone")
    m.spec_delta("yishretzu HA-MAYIM (waters delegated)",
                 "va-yivra ELOHIM — God executes; delegate credited in the clause")
    m.spec_delta("no taninim in the order", "taninim LEAD the delivery, adjective-bearing")
    m.spec_delta("bare classes", "kol- totality x2, kind-keys, of differentiated as of KANAF (winged)")
    m.test("tov", "nefesh_chaya")                 # test BEFORE the blessing
    m.bless("otam (them — the new creatures)",
            ["CMD!(peru — be fruitful)", "CMD!(revu — multiply)",
             "CMD!(milu et-ha-mayim ba-yamim — fill the waters in the seas)",
             "LET(yirev ha-of ba-aretz — let the fowl multiply on land)"])
    # ^ the corpus's FIRST imperatives — and a mood SPLIT: the fowl gets a
    #   third-person jussive, and only one verb of the three (rationed mandate).
    m.commit(5, "yom chamishi", "ORDINAL")        # chamishi = "fifth"
    # zero REGISTRY writes today: naming ended day 3, offices unused.


def day6(m):
    """Gen 1:24-31 — land classes, the adam, dominion, grants, THE sixth day."""
    print("\n=== DAY 6 — chayah + adam (land animals + the human): the pivot (Gen 1:24-31)")
    # -- block 1: land classes (1:24-25)
    m.declare("totze(aretz, product=nefesh_chaya_le_minah)", "LET")
    # ^ totze — day 3's DELIVERY verb re-used as a spec verb; hiphil jussive.
    m.presupposed("aretz_registry")
    m.receipt("totze(aretz, product=nefesh_chaya_le_minah)",
              "va-yehi khen — the receipt token RETURNS, same-verse (days 1-4 position)")
    m.event("asah (made): chayat ha-aretz (wild beast), behemah (cattle),"
            " remes ha-adamah (creeper of the ground)")
    m.install("chayat_ha_aretz", "behemah", "remes_ha_adamah")
    m.spec_delta("totze HA-ARETZ (earth delegated)",
                 "va-ya'as ELOHIM — God executes; delegate SILENT (no credit clause)")
    m.spec_delta("behemah, remes, chayto-eretz (archaic construct, last)",
                 "chayat ha-aretz FIRST (normalized + article) — order permuted")
    m.spec_delta("remes (bare)", "KOL-remes HA-ADAMAH — first 'ground' of the corpus,"
                 " one verse before adam is proposed")
    m.test("tov", "nefesh_chaya")
    # -- block 2: the adam (1:26-28)
    m.declare("make(adam, spec=b_tzelem_k_demut)", "CMD-US?")
    # ^ na'aseh ("let US make") — first 1st-person-plural form in the corpus;
    #   coded imperfect, so the ? is mandatory. The plural stays [OPEN].
    m.design("rule(adam, over: dagah/of/behemah/kol-ha-aretz/remes)")
    # ^ ve-yirdu ("and let them rule") — jussive purpose clause; no receipt
    #   for dominion exists anywhere in the span: contract left undischarged.
    m.presupposed("dagat_ha_yam", "of_ha_shamayim")
    m.event("BARA TRIPLED: va-yivra... bara oto... bara otam — one verse, three tokens")
    m.install("ha_adam")
    m.receipt("make(adam, spec=b_tzelem_k_demut)",
              "receipt by delivery alone — NO va-yehi khen: the beriah-triad rule"
              " (heavens/taninim/adam need no token; bara itself receipts)")
    m.spec_delta("na'aseh (asah — making verb, 1cp)", "bara x3 — verb ESCALATION at delivery")
    m.spec_delta("be-tzalmeNU ki-dmuteNU (OUR image, OUR likeness)",
                 "be-tzalmO (HIS image) + be-tzelem ELOHIM — plural resolved to singular")
    m.spec_delta("tzelem AND demut", "tzelem only x3 — demut (likeness) DROPPED (returns 5:1)")
    m.spec_delta("adam (unsexed)", "zakhar u-nekevah (male and female) + oto->otam number shift")
    m.bless("otam (the humans, addressed DIRECTLY: va-yomer LAHEM)",
            ["CMD!(peru — be fruitful)", "CMD!(revu — multiply)",
             "CMD!(milu et-ha-aretz — fill the EARTH, not the waters)",
             "CMD!(kivshuha — subdue it: a verb no spec announced)",
             "CMD!(redu — rule the fish, the fowl, every creeping living thing)"])
    # ^ five imperatives, NO mood split — day 5's ration has no parallel here.
    m.spec_delta("design: yirdu over 5 domains incl. ALL THE EARTH",
                 "mandate: redu over 3 — the earth MOVED to fill-and-subdue OBJECT")
    m.spec_delta("design verbs: radah only", "kavash (subdue) ADDED — Torah-rare, grade A")
    # -- block 3: the food grants (1:29-30)
    m.event("hineh NATATI ('behold, I HAVE GIVEN') — the corpus's first"
            " first-person perfect: a grant completed by speech")
    m.presupposed("kol_zorea_zera")               # day-3 plants under shifted terms
    m.assign("kol_zorea_zera", "okhlah_la_adam")  # okhlah = "food": office 1
    m.declare("yihyeh(kol_zorea_zera, le_okhlah)", "LET?")
    # ^ "for you it SHALL BE for food" — imperfect standing-state demand.
    m.presupposed("kol_yerek_esev")
    m.assign("kol_yerek_esev", "okhlah_le_chol_nefesh_chaya")   # office 2: animals
    m.receipt("yihyeh(kol_zorea_zera, le_okhlah)",
              "va-yehi khen — the WEEK'S LAST receipt answers yihyeh ('shall be')"
              " with its own verb root: va-yehi ('and it was')")
    # -- close (1:31)
    m.test("tov_meod", "kol_asher_asah")
    # ^ the GLOBAL test: explicit everything-object, hineh (behold), me'od (very);
    #   Onkelos reads it as an arrangement check: takin lachada ("well-ordered").
    m.commit(6, "yom HA-shishi", "DEFINITE ORDINAL")
    # ^ THE sixth day — the week's only definite article on a day label
    #   (heh yeterah, "extra letter heh"; the chain hangs a condition on it:
    #   creation conditional on Torah-acceptance, Shabbat 88a).


def day7(m):
    """Gen 2:1-3 — completion and sanctity. The OPEN TRANSACTION."""
    print("\n=== DAY 7 — shevi'i (the seventh): completion and sanctity (Gen 2:1-3)")
    m.event("va-yekhulu ('and they WERE FINISHED') — PASSIVE, agentless:"
            " heavens, earth, and all their tzava (host/array)")
    m.presupposed("shamayim_registry", "aretz_registry_2")
    m.event("va-yekhal ('and He FINISHED') — ACTIVE, dated ON the seventh day [OPEN]")
    m.event("va-yishbot ('and He CEASED') — the verb that will name the Sabbath;"
            " Onkelos glosses it 'rested' (ve-nach)")
    m.bless("yom_ha_shevii (the seventh day — a TIME object, not a creature)")
    # ^ third blessing of the corpus: NO le-mor, NO mandate, NO speech at all —
    #   this is the only day with zero utterances.
    m.assign("yom_ha_shevii", "kadosh")
    # ^ va-yekadesh ("and He sanctified") — the Torah's FIRST holiness token;
    #   written to a day: the machine flags a status write to a non-entity.
    m.say("NOTE    asher bara Elohim LA'ASOT ('which God created TO MAKE') —")
    m.say("        the closing purpose infinitive: creation handed forward [OPEN]")
    # -- and then: NOTHING. No test. No receipt. No evening-morning. No label.
    m.say("(no COMMIT operator exists for day 7 — the transaction stays open)")


# ---------------------------------------------------------------------------
# run the week
# ---------------------------------------------------------------------------

def audit(m):
    print("\n" + "=" * 74)
    print("WEEK AUDIT — machine state after Gen 2:3")
    print("=" * 74)
    created = sorted(k for k, v in m.WORLD["entities"].items() if v == "created")
    presup = sorted(k for k, v in m.WORLD["entities"].items() if v == "presupposed")
    print("WORLD    created x%d: %s" % (len(created), ", ".join(created)))
    print("         presupposed (read-before-install) x%d: %s" % (len(presup), ", ".join(presup)))
    print("         standing mandate facts x%d (days 5-6 blessings — receipts never owed)"
          % sum(1 for f in m.WORLD["facts"] if f.startswith("mandate")))
    print("REGISTRY names x%d (series ENDED day 3): %s"
          % (len(m.REGISTRY["names"]),
             ", ".join("%s:=%s" % kv for kv in m.REGISTRY["names"].items())))
    print("         roles x%d (day-4 offices; day-6 food offices; day-7 kadosh):"
          % len(m.REGISTRY["roles"]))
    for e, r in m.REGISTRY["roles"].items():
        print("             %s -> %s" % (e, r))
    open_moods = [(s["demand"], s["mood"]) for s in m.SPECS if s["mood"].endswith("?")]
    print("SPECS    demands issued x%d, all satisfied; question-mark moods held"
          " forever x%d:" % (len(m.SPECS), len(open_moods)))
    for d, mo in open_moods:
        print("             %-8s %s" % (mo, d))
    print("TESTS    x%d local tov ('good') + 1 global tov me'od ('very good')"
          % (len(m.TESTS) - 1))
    print("LEDGER   %d closed rows: %s" % (len(m.LEDGER),
          ", ".join("day %d = %s" % (d, v["label"]) for d, v in sorted(m.LEDGER.items()))))
    print("         day 7: ABSENT — blessed and sanctified, never committed:")
    print("         the week ends holding an OPEN TRANSACTION (the Sabbath's")
    print("         halakhic afterlife: a standing day, re-entered weekly).")
    undis = [t for t in m.TRIPLES if not t["discharged"]]
    for t in undis:
        print("OPEN     design contract undischarged: %s" % t["q"])
    kinds = {}
    for k, _ in m.FLAGS:
        kinds[k] = kinds.get(k, 0) + 1
    print("FLAGS    %s — none blocking (dual-track: flags ride, chain answers"
          % ", ".join("%s x%d" % kv for kv in sorted(kinds.items())))
    print("         recorded beside them, never merged).")
    print("\nRECEIPT CENSUS  va-yehi khen ('and it was so'):")
    print("    day 1 (light: same-verse) · day 2 · day 3 x2 · day 4 · day 5 NONE")
    print("    (relocated into the crediting clause) · day 6 x2 (restored; the")
    print("    last answers yihyeh 'shall be' with va-yehi 'and it was') · day 7 —")
    print("    nothing demanded, nothing owed.")
    print("\nBARA CENSUS  bara ('created', the strong verb): 1:1 (heavens+earth),")
    print("    1:21 (first life), 1:27 x3 (the adam) — and the beriah blocks are")
    print("    exactly the receipt-less ones (the chain's triad, verified day 5).")


def main():
    print("SEVEN DAYS OF CREATION — the derived machine, run end to end")
    print("(learning rendering of gen_01..gen_07; the YAML units are the logic)")
    m = Week()
    for day in (day1, day2, day3, day4, day5, day6, day7):
        day(m)
    audit(m)


if __name__ == "__main__":
    main()
