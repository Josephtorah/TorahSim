#!/usr/bin/env python3
"""torah_runtime_demo_2026-07-31.py — ONE demo: everything required to run
Leviticus 13, from Genesis 1:1 to executed verdicts.

LEARNING DEMO (owner order, 2026-07-31): the three gen_boot renderings
(seven_days / lev13_imports / lev13_decision_tree) combined into one
program that actually CONNECTS them:

    PART 1  BOOT        — the seven days run and EXPORT symbols
    PART 2  IMPORTS     — the Gen 2 -> Lev 10 gap declarations fill the table
    PART 3  INSTALL     — Lev 13:1-8's case + handlers LINK against the table
                          (a missing import is a hard stop — that is the demo)
    PART 4  EXECUTE     — four cases run through the installed procedure
    PART 5  AUDIT       — the whole arc on one screen

Contract, unchanged: this is a RENDERING, not the logic. The truth lives in
the frozen YAML units (gen_01..gen_07 FROZEN; lev_13_intake_quarantine
DRAFT at the freeze gate); gap declarations are UNDERIVED sketches whose
letter-facts (first occurrences) are DB-verified. Every Hebrew term is
glossed in English inline — absolute rule.

Run:  python3 logic/gen_boot/torah_runtime_demo_2026-07-31.py
"""

# ===========================================================================
# the shared symbol table — declared once, used forever
# ===========================================================================

SYMBOLS = {}   # name -> (source, status)


def export(name, source, status):
    SYMBOLS[name] = (source, status)


def resolve(name, needed_by):
    """The linker: Lev 13 may only use what an earlier install exported."""
    if name not in SYMBOLS:
        raise SystemExit("LINK ERROR: %s needs '%s' and nothing installed it"
                         % (needed_by, name))
    src, status = SYMBOLS[name]
    print("      import %-28s <- %-12s %s" % (name, src, status))


# ===========================================================================
# PART 1 — BOOT: the seven days (frozen units gen_01..gen_07, condensed)
# ===========================================================================

class Week:
    def __init__(self):
        self.WORLD, self.FACTS, self.NAMES, self.ROLES = [], [], {}, {}
        self.SPECS, self.TESTS, self.LEDGER, self.FLAGS = [], [], {}, []

    def say(self, msg):
        print("    " + msg)

    def declare(self, demand, mood):
        self.SPECS.append([demand, mood, False])
        self.say("DECLARE %s(%s)" % (mood, demand))

    def receipt(self, demand, how):
        for s in self.SPECS:
            if s[0] == demand and not s[2]:
                s[2] = True
                self.say("RESULT  %s  [%s; mood stays %s]" % (demand, how, s[1]))
                return

    def install(self, *names):
        self.WORLD.extend(names)
        self.say("WORLD += {%s}" % ", ".join(names))

    def name(self, e, n):
        self.NAMES[e] = n
        self.say("NAME    %s := %s" % (e, n))

    def assign(self, e, r):
        self.ROLES[e] = r
        self.say("ASSIGN  %s -> %s" % (e, r))

    def bless(self, who, mandate=()):
        for it in mandate:
            self.FACTS.append("mandate: " + it)
        self.say("BLESS   %s%s" % (who, " MANDATE {%s}" % ", ".join(mandate)
                                   if mandate else " (no mandate)"))

    def test(self, oracle, theme):
        self.TESTS.append((oracle, theme))
        self.say("TEST    PASS(%s, %s)" % (oracle, theme))

    def commit(self, day, label):
        assert all(s[2] for s in self.SPECS), "open demand at commit"
        if not [t for t in self.TESTS if t[2:] == ()][len(self.LEDGER):]:
            pass
        self.LEDGER[day] = label
        self.say("COMMIT  LEDGER[day %d] := %s" % (day, label))


def boot_week(m):
    print("\n" + "=" * 74)
    print("PART 1 — BOOT: the seven days (FROZEN units gen_01..gen_07)")
    print("=" * 74)

    print("\n--- day 1 (Gen 1:1-5): or (light)")
    m.say("EVENT   bara (created): shamayim (heavens), aretz (earth); t0 := reshit ('beginning')")
    m.install("shamayim", "aretz")
    m.declare("exists(or)", "LET")
    m.receipt("exists(or)", "va-yehi or — same verse")
    m.install("or_light")
    m.test("tov", "or")                      # tov = "good"
    m.name("or_light", "yom")                # day
    m.name("choshekh", "layla")              # night
    m.commit(1, "yom echad (CARDINAL 'one')")

    print("\n--- day 2 (Gen 1:6-8): raqia (firmament)")
    m.declare("exists(raqia)", "LET")
    m.declare("mavdil(raqia, mayim|mayim)", "LET?")   # the first mandatory ?
    m.receipt("exists(raqia)", "va-yehi khen ('and it was so')")
    m.receipt("mavdil(raqia, mayim|mayim)", "the divide event")
    m.install("raqia")
    m.name("raqia", "shamayim")
    m.say("FLAG    commit_without_test — day 2 has no tov; flags never block")
    m.commit(2, "yom sheni")

    print("\n--- day 3 (Gen 1:9-13): land + vegetation (first delegation)")
    m.declare("gathered(mayim)", "LET")
    m.declare("exists(yabasha)", "LET?")
    m.receipt("gathered(mayim)", "va-yehi khen — BEFORE delivery")
    m.receipt("exists(yabasha)", "the dry appears")
    m.install("yabasha", "deshe")
    m.name("yabasha", "eretz")
    m.name("miqveh_ha_mayim", "yamim")       # seas — naming series ENDS here
    m.test("tov", "gathering")
    m.test("tov", "vegetation")
    m.commit(3, "yom shlishi")

    print("\n--- day 4 (Gen 1:14-19): the luminaries (first offices)")
    m.declare("exists(meorot)", "LET")
    m.receipt("exists(meorot)", "va-yehi khen")
    m.install("maor_gadol", "maor_qaton", "kokhavim")
    m.assign("maor_gadol", "memshelet_yom")   # office of day
    m.assign("maor_qaton", "memshelet_lailah")
    m.test("tov", "meorot")
    m.commit(4, "yom revi'i")

    print("\n--- day 5 (Gen 1:20-23): first life, first blessing — NO receipt token")
    m.declare("swarm(mayim)", "LET?")
    m.declare("fly(of)", "LET?")
    m.receipt("swarm(mayim)", "asher SHARTZU ha-mayim — receipt inside a relative clause")
    m.receipt("fly(of)", "delivery alone")
    m.install("taninim", "nefesh_chaya", "of_kanaf")
    m.test("tov", "nefesh_chaya")
    m.bless("the creatures", ["CMD!(peru)", "CMD!(revu)", "CMD!(milu ha-mayim)",
                              "LET(yirev ha-of)"])
    m.commit(5, "yom chamishi")

    print("\n--- day 6 (Gen 1:24-31): land classes + the adam — receipts RETURN")
    m.declare("totze(aretz)", "LET")
    m.receipt("totze(aretz)", "va-yehi khen — same-verse position restored")
    m.install("chayat_ha_aretz", "behemah", "remes")
    m.test("tov", "nefesh_chaya")
    m.declare("make(adam)", "CMD-US?")        # na'aseh — first 1cp of the corpus
    m.receipt("make(adam)", "bara x3 — the beriah triad needs no token")
    m.install("ha_adam")
    m.bless("the humans (addressed directly)",
            ["CMD!(peru)", "CMD!(revu)", "CMD!(milu ha-aretz)",
             "CMD!(kivshuha)", "CMD!(redu)"])
    m.declare("yihyeh(zera, le_okhlah)", "LET?")
    m.assign("kol_zorea_zera", "okhlah_la_adam")       # food office 1
    m.assign("kol_yerek_esev", "okhlah_le_chol_chai")  # food office 2
    m.receipt("yihyeh(zera, le_okhlah)", "va-yehi khen — the week's LAST receipt")
    m.test("tov_meod", "kol_asher_asah")
    m.commit(6, "yom HA-shishi (DEFINITE — heh yeterah)")

    print("\n--- day 7 (Gen 2:1-3): completion + sanctity — the OPEN TRANSACTION")
    m.say("EVENT   va-yekhulu ('they WERE finished' — agentless passive)")
    m.say("EVENT   va-yekhal / va-yishbot ('finished' / 'ceased' — ON the seventh)")
    m.bless("yom_ha_shevii (a TIME object)")
    m.assign("yom_ha_shevii", "kadosh")       # the Torah's first holiness write
    m.say("(no COMMIT — LEDGER[7] stays absent forever)")

    # ---- what the frozen week EXPORTS to everything downstream -------------
    export("adam (human)",              "Gen 1:26-27", "[FROZEN gen_06]")
    export("inspection (see+behold+verdict)", "Gen 1:31", "[FROZEN gen_06]")
    export("seven-day clock",           "Gen 1:5-2:3", "[FROZEN week]")
    export("yom ha-shevi'i (THE 7th day label)", "Gen 2:2-3", "[FROZEN gen_07]")
    export("status-write by declaration", "Gen 2:3 (kadosh)", "[FROZEN gen_07]")
    export("open-transaction pattern",  "Gen 2:1-3", "[FROZEN gen_07]")


# ===========================================================================
# PART 2 — IMPORTS: the Gen 2 -> Lev 10 supply chain (UNDERIVED gap sketches;
#          every first-occurrence claim DB-verified 2026-07-31)
# ===========================================================================

def import_chain():
    print("\n" + "=" * 74)
    print("PART 2 — THE IMPORT CHAIN (gap declarations, canonical order)")
    print("=" * 74)
    gaps = [
        ("Gen 2:16-17", "rule genre (ki/if + penalty)",
         "the FIRST installed rule: permission + LET-NOT + mot tamut penalty"),
        ("Gen 2:21",    "basar (flesh)",
         "va-yisgor BASAR — flesh AND the shut-verb born in one clause"),
        ("Gen 2:21",    "sagar->hisgir (shut->confine)",
         "the quarantine verb's first firing is surgical flesh-closure"),
        ("Gen 2:22-23", "ish/ishah (man/woman)",
         "the party vocabulary (Lev 13:29,38 dispatches on it)"),
        ("Gen 3:21",    "or (skin) + begged (garment)",
         "kotnot OR: skin and garment enter together — both become exam domains"),
        ("Gen 4:7",     "chatat (sin)",
         "sin crouching at the door — the negative register opens"),
        ("Gen 7:2",     "tahor (pure)",
         "the axis's positive pole — Noah's clean animals cut day 6's classes"),
        ("Gen 7:4,16",  "quarantine prototype",
         "enclosure (va-yisgor) + purity + seven-day timers co-fire at the ark"),
        ("Gen 12:17",   "nega (mark/affliction)",
         "the law's title noun debuts on Pharaoh, over Sarai"),
        ("Gen 14:18",   "kohen (priest) — the word",
         "Malki-tzedek: the office word before the office"),
        ("Gen 34:5",    "tamei (impure)",
         "the axis's negative pole (Dinah)"),
        ("Exod 20:8-11","clock legislated",
         "the Sabbath command CITES Gen 2:2-3 verbatim as its reason clause"),
        ("Exod 28:1",   "kohen — the OFFICE",
         "Aaron and his sons installed; Lev 8 executes with 7 compliance receipts"),
        ("Lev 10:10",   "havdil (divide) as priestly office",
         "the creation partition operator handed to officers over kodesh|chol, tamei|tahor"),
    ]
    for src, sym, note in gaps:
        print("  %-12s %-34s %s" % (src, sym, "[UNDERIVED]"))
        print("      %s" % note)
        export(sym, src, "[UNDERIVED]")


# ===========================================================================
# PART 3 — INSTALL: Lev 13:1-8 links and loads (draft unit
#          lev_13_intake_quarantine — CASE + six HANDLERs)
# ===========================================================================

def install_law():
    print("\n" + "=" * 74)
    print("PART 3 — LEV 13:1-8 INSTALLS (the LINK step: every symbol must resolve)")
    print("=" * 74)
    print("  [Lev 13:2] 'adam ki yihyeh ve-OR BESARO NEGA...' — the opening")
    print("  five words are four imports. Resolving them (a miss = hard stop):\n")
    resolve("adam (human)",                        "Lev 13:2 (the case subject)")
    resolve("or (skin) + begged (garment)",        "Lev 13:2 (the exam surface)")
    resolve("basar (flesh)",                       "Lev 13:2 (the substrate)")
    resolve("nega (mark/affliction)",              "Lev 13:2 (the examined thing)")
    resolve("kohen — the OFFICE",                  "Lev 13:2 (the inspector)")
    resolve("rule genre (ki/if + penalty)",        "Lev 13:2 (the ki-case shape)")
    resolve("inspection (see+behold+verdict)",     "Lev 13:3 (ve-ra'ah...ve-hineh)")
    resolve("sagar->hisgir (shut->confine)",       "Lev 13:4 (the quarantine call)")
    resolve("seven-day clock",                     "Lev 13:4-6 (the timer)")
    resolve("yom ha-shevi'i (THE 7th day label)",  "Lev 13:5-6 (the re-entry date)")
    resolve("tahor (pure)",                        "Lev 13:6 (the release verdict)")
    resolve("tamei (impure)",                      "Lev 13:3,8 (the impure verdict)")
    resolve("status-write by declaration",         "Lev 13:3,6,8 (timme/tiharo)")
    print("\n  ALL IMPORTS RESOLVED — the runtime Genesis built is sufficient.")
    print("  Installing the procedure (standing handlers; nothing executes yet):")
    print("    CASE(adam, se'et|sapachat|baheret in skin-of-flesh) ROUTE(-> priest)")
    print("    HANDLER IF(hair white AND deeper)        THEN(tzara'at — declare TAMEI)")
    print("    HANDLER IF(white, NOT deeper, NOT turned) THEN(confine 7 days)")
    print("    HANDLER IF(day 7: stood, no spread)       THEN(confine 7 SHENIT)")
    print("    HANDLER IF(day 7 II: faded, no spread)    THEN(declare TAHOR; wash; is-pure)")
    print("    HANDLER IF(spreads AFTER release)         THEN(be seen again)")
    print("    HANDLER IF(spread confirmed)              THEN(declare TAMEI — tzara'at)")


# ===========================================================================
# PART 4 — EXECUTE: cases run through the installed procedure
#          (Lev 13:1-8 as branching code; branches cite their verses)
# ===========================================================================

class Obs:
    def __init__(self, hair_white=False, deeper=False, stood=False,
                 faded=False, spread=False):
        self.hair_white, self.deeper = hair_white, deeper
        self.stood, self.faded, self.spread = stood, faded, spread


def run_case(name, observations, spreads_after_release=False):
    print("\nCASE: %s" % name)
    day, obs = 0, list(observations)
    o = obs.pop(0)
    print("    day %2d [13:2] ki (when): mark on skin-of-flesh -> brought to the priest" % day)
    if o.hair_white and o.deeper:
        print("    day %2d [13:3] hair WHITE + DEEPER -> tzara'at: declare TAMEI (impure)" % day)
        return "TAMEI"
    if not o.hair_white and not o.deeper:
        print("    day %2d [13:4] im (if): white, NOT deeper, NOT turned -> CONFINE 7 days" % day)
        day += 7
        o = obs.pop(0)
        if o.spread:
            print("    day %2d [13:5/8] ve-hineh: SPREAD in confinement -> declare TAMEI" % day)
            return "TAMEI"
        if o.stood:
            print("    day %2d [13:5] ve-hineh: STOOD, no spread -> CONFINE 7 SHENIT (2nd)" % day)
            day += 7
            o = obs.pop(0)
            if o.faded and not o.spread:
                print("    day %2d [13:6] ve-hineh: FADED -> declare TAHOR (pure); wash; is-pure" % day)
                if spreads_after_release:
                    print("    day %2d [13:7] im (if): spreads AFTER release -> be seen again" % (day + 1))
                    print("    day %2d [13:8] ve-hineh: confirmed -> declare TAMEI: tzara'at hi" % (day + 1))
                    return "TAHOR, reopened -> TAMEI"
                return "TAHOR"
            if o.spread:
                print("    day %2d [13:8] ve-hineh: SPREAD -> declare TAMEI: tzara'at hi" % day)
                return "TAMEI"
    print("    day %2d [13:9ff] mixed predicates -> the chapter's next ki-paragraph" % day)
    return "HANDED OFF"


def execute_cases():
    print("\n" + "=" * 74)
    print("PART 4 — CASES EXECUTE (the handlers fire; verdicts are status writes)")
    print("=" * 74)
    print("  HONESTY NOTE: these four cases are SYNTHETIC — invented inputs, one")
    print("  per branch (path coverage). Lev 13:1-8 itself narrates zero cases.")
    print("  The corpus's own executed test case is MIRIAM (Num 12:10-15): the")
    print("  quarantine actually runs on a person — and Deut 24:8-9 pairs the")
    print("  statute with that case by name ('remember Miriam'). See below.")
    verdicts = [
        run_case("A — white hair, deeper at intake", [Obs(hair_white=True, deeper=True)]),
        run_case("B — shallow; stands week 1; fades week 2", [Obs(), Obs(stood=True), Obs(faded=True)]),
        run_case("C — as B, then spreads after release", [Obs(), Obs(stood=True), Obs(faded=True)], True),
        run_case("D — spread caught at first day-7 check", [Obs(), Obs(spread=True)]),
    ]
    return verdicts


# ===========================================================================
# PART 5 — AUDIT
# ===========================================================================

def audit(m, verdicts):
    print("\n" + "=" * 74)
    print("PART 5 — AUDIT: Genesis 1:1 to executed verdicts, one arc")
    print("=" * 74)
    print("BOOT     WORLD x%d entities; %d names (series ended day 3); %d offices;"
          % (len(m.WORLD), len(m.NAMES), len(m.ROLES)))
    print("         %d demands all satisfied (?-moods held forever); ledger rows 1-6;"
          % len(m.SPECS))
    print("         day 7 uncommitted — the open transaction the Sabbath law re-enters.")
    print("IMPORTS  %d symbols exported (week + gap chain), every one DB-anchored."
          % len(SYMBOLS))
    print("INSTALL  1 case + 6 handlers standing — installed code, armed;")
    print("         13 imports resolved, 0 missing: Lev 13 runs ENTIRELY on")
    print("         inherited symbols — only its diagnostic content is new.")
    print("EXECUTE  verdicts: %s" % " | ".join(verdicts))
    print("\nThe demo's one sentence: Genesis is the boot log, the gap is the")
    print("import chain, the law is installed code, and a case is a function")
    print("call — declared once, used forever, letter-verified at every step.")


def main():
    print("TORAH RUNTIME DEMO — everything required to run Leviticus 13,")
    print("from Genesis 1:1 to executed verdicts")
    print("(learning rendering; the YAML units are the logic: gen_01..07 FROZEN,")
    print(" lev_13_intake_quarantine DRAFT, gap installs UNDERIVED)")
    m = Week()
    boot_week(m)
    import_chain()
    install_law()
    verdicts = execute_cases()
    audit(m, verdicts)


if __name__ == "__main__":
    main()
