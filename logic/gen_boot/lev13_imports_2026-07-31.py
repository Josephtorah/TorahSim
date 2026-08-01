#!/usr/bin/env python3
"""lev13_imports_2026-07-31.py — filling the gaps between the seven days
and Leviticus 13: every declaration Lev 13 reads, installed in canonical
order, with comments.

LEARNING EXERCISE (owner order, 2026-07-31), companion to
seven_days_2026-07-31.py. Same contract: this is a RENDERING, not the
logic. The seven-days reads cite FROZEN units (gen_01..gen_07). The gap
installs below are UNDERIVED — no unit exists for them yet — so their
operator readings are provisional sketches; what IS hard is the letter
data: every "first occurrence" claim in this file was verified against
our own DB (torah_grok.sqlite, checked 2026-07-31) before being written.
Every Hebrew term carries its English gloss inline — absolute rule.

The question this file answers: when the Lev 13 machine boots and starts
reading symbols, where was each symbol installed? The seven days supplied
four of its devices; everything else arrives in the gap — and the gap
turns out to be a single coherent supply chain.

Run:  python3 logic/gen_boot/lev13_imports_2026-07-31.py
"""

BOOT = []      # the import trace
MANIFEST = []  # symbol -> (installed at, status, what Lev 13 does with it)


def install(ref, status, symbol, gloss, note):
    BOOT.append((ref, status, symbol, gloss, note))
    print("  %-11s %-12s %-14s %s" % (ref, status, symbol, gloss))
    for line in note.split("\n"):
        print("      %s" % line)


def imports(symbol, source, status, use):
    MANIFEST.append((symbol, source, status, use))


# ---------------------------------------------------------------------------
# 0. What the FROZEN week already supplied (recap — full detail in
#    seven_days_2026-07-31.py and the frozen units)
# ---------------------------------------------------------------------------

def week_recap():
    print("\n### ALREADY INSTALLED BY THE FROZEN WEEK (gen_01..gen_07):")
    print("      adam (day 6)          — Lev 13:2's subject parameter")
    print("      ra'ah+hineh verdict   — the inspection instrument (1:31 syntax;")
    print("                              Lev 13 runs ra'ah x32, hineh x20)")
    print("      seven-day clock       — quarantine timer; re-inspection lands on")
    print("                              yom ha-shevi'i (THE seventh day) x6")
    print("      status-write device   — day 7's kadosh (holy) declaration; Lev 13")
    print("                              runs 20 declare-impure/declare-pure writes")
    imports("adam ('human')", "Gen 1:26-27", "[FROZEN gen_06]", "the law's subject: adam ki yihyeh... (13:2)")
    imports("ra'ah+hineh ('see...behold') verdict", "Gen 1:31", "[FROZEN gen_06]", "the priest's exam syntax, polarity inverted")
    imports("shivat yamim ('seven days') clock", "Gen 1:5-2:3", "[FROZEN week]", "quarantine periods; re-check on THE seventh")
    imports("status-write (declaration confers state)", "Gen 2:3", "[FROZEN gen_07]", "ve-timme'o / ve-tiharo ('declare impure/pure')")


# ---------------------------------------------------------------------------
# 1. EDEN (Gen 2:4-3:24) — the biggest single supplier
# ---------------------------------------------------------------------------

def gap_eden():
    print("\n### GAP 1 — EDEN (Gen 2:4-3:24): substrate, parties, genre, garments")

    install("Gen 2:7", "[UNDERIVED]", "adam-instance", "the species becomes an individual",
            "va-yitzer... afar min ha-ADAMAH ('dust from the GROUND') — the day-6\n"
            "species term instantiated; the adamah wordplay day 6 seeded at 1:25\n"
            "(first 'ground', one verse before adam was proposed) pays off here.")
    imports("the adam/adamah bond", "Gen 2:7", "[UNDERIVED]", "the patient under every skin exam")

    install("Gen 2:16-17", "[UNDERIVED]", "first-rule", "permission + prohibition + penalty",
            "The corpus's FIRST installed rule: a grant ('of every tree you MAY\n"
            "eat') + LET-NOT(eat(etz ha-da'at)) + penalty clause MOT TAMUT ('you\n"
            "shall surely DIE' — infinitive absolute doubling, DB: Vqa + Vqi2ms).\n"
            "This is the TRIGGER/HANDLER GENRE itself being installed — the code\n"
            "shape Lev 13 is written in descends from this verse pair.")
    imports("trigger/handler rule shape", "Gen 2:16-17", "[UNDERIVED]", "the genre of every ki- ('when/if') clause in Lev 13")

    install("Gen 2:21", "[UNDERIVED]", "basar + SAGAR", "flesh — and the shut-verb's first firing",
            "va-yisgor BASAR tachtenah ('and He CLOSED the FLESH beneath it') —\n"
            "TWO Lev 13 imports in one clause, DB-verified first occurrences:\n"
            "basar ('flesh', the exam substrate: be-or BESARO, 13:2ff) and\n"
            "sagar ('shut') — the verb whose hiphil HISGIR ('confine') is Lev\n"
            "13's quarantine operator. Its first use is SURGICAL CLOSURE OF\n"
            "FLESH. The quarantine verb is born on skin.")
    imports("basar ('flesh')", "Gen 2:21", "[UNDERIVED]", "the exam substrate: 'in the skin of his FLESH'")
    imports("sagar ('shut') -> hisgir ('confine')", "Gen 2:21", "[UNDERIVED]", "the quarantine operator (13:4,5,11,21,26,31...)")

    install("Gen 2:22-23", "[UNDERIVED]", "ishah / ish", "the party vocabulary",
            "le-ISHAH ('into a woman', 2:22 — first token, DB) and ISH ('man',\n"
            "2:23's wordplay). Lev 13 dispatches cases on exactly these: ve-ISH\n"
            "O ISHAH ki yihyeh... ('a man OR a woman, when there is...' —\n"
            "13:29, 13:38) and closes its verdict on ish tzarua hu (13:44).")
    imports("ish / ishah ('man / woman')", "Gen 2:22-23", "[UNDERIVED]", "case dispatch parameters (13:29, 13:38)")

    install("Gen 3:21", "[UNDERIVED]", "or + begged", "skin — and the garment domain",
            "kotnot OR ('garments of SKIN') — the word or ('skin', ayin-vav-resh;\n"
            "NOT day 1's or 'light', aleph-vav-resh — different first letters,\n"
            "the chain's famous garments-of-light wordplay lives on that pair)\n"
            "enters the corpus HERE, DB-verified. Lev 13's opening substrate\n"
            "(be-OR besaro, 'in the SKIN of his flesh') and its clothing section\n"
            "(13:47-59, the garment infection) both read this verse's install:\n"
            "skin and garment enter the corpus TOGETHER, as the same object —\n"
            "and Lev 13 legislates them as parallel infection domains.")
    imports("or ('skin')", "Gen 3:21", "[UNDERIVED]", "the exam surface (13:2 and throughout)")
    imports("garment as second skin", "Gen 3:7, 3:21", "[UNDERIVED]", "the begged ('garment') infection domain, 13:47-59")

    install("Gen 3:14-19", "[UNDERIVED]", "sentencing", "the handler fires — and discharges strangely",
            "The first violation trace: interrogation, then sentences per party\n"
            "(serpent, woman, man). The 2:17 penalty ('ON THE DAY you eat you\n"
            "shall surely die') does NOT discharge literally — Adam lives 930\n"
            "years. A spec-delta the chain has worked for two millennia (the\n"
            "divine-day reading, Ps 90:4; the mortality reading). The machine\n"
            "lesson Lev 13 inherits: penalty clauses have executors and TIMING.")
    imports("death (sentenced)", "Gen 3:19", "[UNDERIVED]", "the stakes behind the tamei ('impure') verdict")


# ---------------------------------------------------------------------------
# 2. FIRST BLOOD (Gen 4) — sin and death become real
# ---------------------------------------------------------------------------

def gap_first_blood():
    print("\n### GAP 2 — FIRST BLOOD (Gen 4): the negative register opens")
    install("Gen 4:7", "[UNDERIVED]", "chatat", "sin — crouching at the door",
            "la-petach CHATAT rovetz ('at the door SIN crouches') — first token\n"
            "of the sin-word (DB: lemma 2403b, Gen 4:7), arriving as a POSITIONED\n"
            "entity (at an opening, waiting). Lev 13's world — where a condition\n"
            "sits ON a person and an officer must examine the boundary — speaks\n"
            "this verse's spatial grammar.")
    install("Gen 4:8", "[UNDERIVED]", "first-death", "the penalty clause's world is now real",
            "Abel: the first actual death. From here, mot yumat ('he shall\n"
            "surely die') formulas have a referent.")
    imports("chatat ('sin')", "Gen 4:7", "[UNDERIVED]", "background register of the impurity system")


# ---------------------------------------------------------------------------
# 3. THE ARK (Gen 7) — the proto-quarantine: all three devices co-fire
# ---------------------------------------------------------------------------

def gap_ark():
    print("\n### GAP 3 — THE ARK (Gen 7): purity axis + timer + enclosure, together")
    install("Gen 7:2", "[UNDERIVED]", "tahor", "the pure/impure axis — first token",
            "ha-behemah ha-TEHORAH ('the CLEAN cattle') — the pure-word's first\n"
            "occurrence in the corpus (DB-verified; the learning pass flagged\n"
            "this forward reference to Lev 11 months ago). NOTE what it\n"
            "partitions: behemah — day 6's install. The new axis cuts the old\n"
            "taxonomy. Its negative pole arrives much later (tamei 'impure',\n"
            "first at Gen 34:5 — Dinah): the axis is born positive-only.")
    install("Gen 7:4", "[UNDERIVED]", "seven-day-wait", "the week as countdown",
            "'For in SEVEN MORE DAYS I will cause it to rain' — the creation\n"
            "week's cycle used as a WAITING PERIOD before a decreed event: the\n"
            "exact device of Lev 13's ve-hisgiro shivat yamim ('he shall\n"
            "confine him seven days').")
    install("Gen 7:16", "[UNDERIVED]", "enclosure", "the shut-verb's second firing — protective",
            "va-yisgor YHWH ba'ado ('and the LORD SHUT him in') — sagar again\n"
            "(2:21 closed flesh; 7:16 closes the ark). And the same verse\n"
            "carries, DB-verified: zakhar u-nekevah ('male and female' — day\n"
            "6's pair), mi-kol BASAR ('of all flesh' — Eden's substrate), and\n"
            "ka'asher tzivah oto Elohim ('as God COMMANDED him' — the\n"
            "compliance receipt of the law genre). One verse: the pair, the\n"
            "flesh, the receipt, the enclosure.\n"
            "THE ARK IS THE PROTO-QUARANTINE: enclosure (sagar) + purity\n"
            "partition (tahor) + seven-day timers (7:4,10) co-fire here first —\n"
            "the three devices Lev 13 will run as one procedure.")
    imports("tahor ('pure')", "Gen 7:2", "[UNDERIVED]", "the verdict register's positive pole")
    imports("tamei ('impure')", "Gen 34:5", "[UNDERIVED]", "the verdict register's negative pole")
    imports("enclosure + timer + purity, combined", "Gen 7", "[UNDERIVED]", "the quarantine procedure's prototype")


# ---------------------------------------------------------------------------
# 4. THE AFFLICTION WORD (Gen 12 / 26 / 34) — nega debuts, three times guarded
# ---------------------------------------------------------------------------

def gap_nega_debut():
    print("\n### GAP 4 — NEGA (Gen 12:17; 26:11; 34:5): the affliction register")
    install("Gen 12:17", "[UNDERIVED]", "nega", "the law's subject noun — first firing",
            "va-yenaga... NEGA'IM gedolim ('struck with great AFFLICTIONS') —\n"
            "Pharaoh, 'over the matter of Sarai'. Lev 13's own noun (nega, the\n"
            "mark/affliction) debuts as a ruler's skin affliction over a taken\n"
            "wife — the chain reads it as tzara'at outright (Bereshit Rabbah\n"
            "41:2, triage queue). DB-verified first occurrence.")
    install("Gen 26:11", "[UNDERIVED]", "mot-yumat", "the death formula enters LAW form",
            "Avimelekh's edict: ha-NOGEA ba-ish ha-zeh... MOT YUMAT ('whoever\n"
            "TOUCHES this man or his wife shall surely be put to death') — the\n"
            "first mot-yumat LEGAL formula in the corpus (DB-verified), decreed\n"
            "by a Gentile king, and phrased with the SAME root as nega (naga,\n"
            "'touch'). Touch and affliction are one root; the first statute\n"
            "guards a boundary of touch.\n"
            "Observation, dual-track: the negative register's three debuts —\n"
            "nega (Sarai, 12:17), mot yumat (Rebekah's protection, 26:11),\n"
            "tamei (Dinah, 34:5) — are ALL marriage-boundary narratives. The\n"
            "machine notes the pattern and stops; significance is chain work.")
    imports("nega ('mark/affliction')", "Gen 12:17", "[UNDERIVED]", "the thing Lev 13 examines (its own title noun)")
    imports("mot yumat ('surely die') as statute", "Gen 26:11", "[UNDERIVED]", "the penalty-formula genre of the law corpus")


# ---------------------------------------------------------------------------
# 5. OFFICES AND CLOCK-NAMES (Gen 14 / 32; Exod 16 / 20 / 28-29)
# ---------------------------------------------------------------------------

def gap_offices():
    print("\n### GAP 5 — OFFICES + THE CLOCK'S NAME (Gen 14, 32; Exod 16, 20, 28-29)")
    install("Gen 14:18", "[UNDERIVED]", "kohen", "the priest-word — before the priesthood",
            "Malki-tzedek... KOHEN le-El Elyon ('priest to God Most High') —\n"
            "the office word exists in the corpus long before Israel's office\n"
            "is created (DB-verified first token).")
    install("Gen 32:3", "[UNDERIVED]", "machaneh", "the camp-word",
            "MACHANEH ('camp') debuts at Jacob's Machanayim ('two camps') —\n"
            "the topology term of Lev 13:46's sentence: michutz la-machaneh\n"
            "moshavo ('OUTSIDE THE CAMP is his dwelling').")
    install("Exod 16:23", "[UNDERIVED]", "shabbat", "the seventh day gets its NAME",
            "SHABBAT ('cessation') as a noun — first token, at the MANNA (DB) —\n"
            "on the trail our detector graded A for ha-shishi ('the sixth'):\n"
            "Exod 16:5,22,29, the double portion on THE sixth day. Day 7 of the\n"
            "week was never named in Genesis; the name arrives with bread.")
    install("Exod 20:8-11", "[UNDERIVED]", "clock-in-law", "the week becomes a commandment",
            "zakhor et yom ha-SHABBAT le-KADSHO ('remember the Sabbath day to\n"
            "SANCTIFY it') — and the reason clause re-runs Gen 2:2-3's exact\n"
            "vocabulary (rested / blessed / THE seventh / sanctified): the law\n"
            "CITES the frozen unit. Day 7's open transaction becomes a weekly\n"
            "re-entered obligation — and Lev 13's quarantine clock ticks on a\n"
            "cycle the law now owns.")
    install("Exod 28:1; 29:44", "[UNDERIVED]", "kohen-office", "Israel's priesthood installed",
            "ve-yikhahen li ('that he may serve Me as priest') — Aaron and his\n"
            "sons take the office; Lev 8 executes the investiture spec with\n"
            "SEVEN ka'asher tzivah ('as He commanded') receipts (measured in\n"
            "the learning pass). Lev 13:2 hands the nega exam to exactly them:\n"
            "'to Aaron the priest or to one of his sons the priests'.")
    imports("kohen ('priest') — word", "Gen 14:18", "[UNDERIVED]", "the inspector's title")
    imports("kohen — OFFICE", "Exod 28:1", "[UNDERIVED]", "the delegated oracle who sees and declares")
    imports("machaneh ('camp')", "Gen 32:3", "[UNDERIVED]", "the exile topology (13:46)")
    imports("shabbat (the clock, named + legislated)", "Exod 16:23; 20:8-11", "[UNDERIVED]", "the calendar the quarantine runs on")


# ---------------------------------------------------------------------------
# 6. THE BRIDGE (Lev 10:10; 11:47) — the creation operator handed over
# ---------------------------------------------------------------------------

def gap_bridge():
    print("\n### GAP 6 — THE BRIDGE (Lev 10:10): the divide-operator changes hands")
    install("Lev 10:10", "[UNDERIVED]", "havdil-office", "the priests inherit the partition operator",
            "u-LE-HAVDIL bein ha-kodesh u-vein ha-chol u-vein ha-tamei u-vein\n"
            "ha-tahor ('and TO DIVIDE between the holy and the profane, and\n"
            "between the impure and the pure') — DB text verbatim. HAVDIL\n"
            "('divide') is the creation week's own partition operator: day 1\n"
            "God divides light|darkness; day 2 the raqia ('firmament') is BUILT\n"
            "to divide waters|waters (the machine's viyhi-mavdil LET? flag);\n"
            "day 4 the luminaries are APPOINTED to divide (operator delegated\n"
            "to fixtures). Lev 10:10 is the third migration: the operator is\n"
            "delegated to OFFICERS, as a standing job over the two status axes\n"
            "(day 7's kadosh axis; the ark's tahor axis). The learning pass\n"
            "called this 'operator migration' — here is its cleanest chain.")
    install("Lev 11:47", "[UNDERIVED]", "havdil-run", "the operator runs over day 5-6's taxonomy",
            "lehavdil bein ha-tamei u-vein ha-tahor — the diet law closes by\n"
            "running the division over the creature classes the week installed\n"
            "(fins/wings/creepers — day 5-6 kind-keys as the type system).")
    imports("havdil ('divide') as priestly office", "Lev 10:10", "[UNDERIVED]",
            "THE operator Lev 13 executes case-by-case on skin")


# ---------------------------------------------------------------------------
# the manifest
# ---------------------------------------------------------------------------

def manifest():
    print("\n" + "=" * 76)
    print("LEV 13 IMPORT MANIFEST — what its machine reads, and where it was installed")
    print("=" * 76)
    print("Opening verse check — Lev 13:2 'adam ki yihyeh ve-OR BESARO NEGA...'")
    print("('a human, when there is in the SKIN of his FLESH a MARK'):")
    print("    adam(day 6, FROZEN) + or(Gen 3:21) + basar(Gen 2:21) + nega(Gen 12:17)")
    print("    — four imports in five words; none of them local.\n")
    w = max(len(s) for s, _, _, _ in MANIFEST)
    for sym, src, status, use in MANIFEST:
        print("  %-*s  %-16s %-18s %s" % (w, sym, src, status, use))
    print("\nStill missing after all gaps: NOTHING structural — Lev 13's every")
    print("symbol traces to an earlier install. What has no earlier source is")
    print("only the DIAGNOSTIC CONTENT itself (the mark taxonomy: se'et/sapachat/")
    print("baheret 'swelling/scab/bright-spot', hair-color predicates, spread")
    print("tests) — i.e., exactly the new law being legislated. The runtime is")
    print("fully supplied; only the program text is new. That is the")
    print("declared-once-used-forever architecture, seen from the consumer side.")


def main():
    print("LEV 13 RUNTIME IMPORTS — the gap declarations between the frozen week")
    print("and the skin-exam law, in canonical order (letter-data DB-verified;")
    print("gap operator readings provisional until each unit is derived)")
    week_recap()
    gap_eden()
    gap_first_blood()
    gap_ark()
    gap_nega_debut()
    gap_offices()
    gap_bridge()
    manifest()


if __name__ == "__main__":
    main()
