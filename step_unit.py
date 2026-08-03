#!/usr/bin/env python3
"""
step_unit.py — the verse STEPPER: run_unit.py's machine, one verse at a time.

Owner order 2026-08-01: "I want to see each verse execute one at a time in
our system. when I click space it will go to the next verse."

Contract: identical to run_unit.py — this tool INTERPRETS frozen units only
(Pre-Code: code never invents logic). It imports run_unit's Machine and
HANDLERS and simply pauses between boot steps, showing what each verse DID
to the six registers.

Keys:  SPACE / ENTER = next verse   ·   q = quit
(If stdin is not a terminal, falls back to line input — Enter advances.)

Usage:
  python3 step_unit.py gen_01_creation_boot
  python3 step_unit.py gen_01_creation_boot gen_02_raqia_day   # units in sequence
"""

import sys

import run_unit as ru

BOLD, DIM, GREEN, YELLOW, CYAN, RESET = (
    "\033[1m", "\033[2m", "\033[32m", "\033[33m", "\033[36m", "\033[0m")

# ---------------------------------------------------------------------------
# Glossing (owner order 2026-08-01: "add english translations") — the
# ABSOLUTE rule applied to machine tokens: nothing Hebrew-derived on screen
# without English. Display-only; the machine's tokens are untouched.
# ---------------------------------------------------------------------------

# whole-token glosses checked FIRST (compounds with their own sense)
GLOSS_EXACT = {
    "YHWH_Elohim": "the-LORD-God", "Elohim": "God", "YHWH": "the-LORD",
    "etz_ha_chayim": "tree-of-life",
    "etz_ha_daat_tov_va_ra": "tree-of-knowledge-of-good-and-evil",
    "ezer_kenegdo": "helper-corresponding-to-him",
    "yom_ha_shevii": "the-seventh-day",
    "be_yom_asot": "in-the-day-of-[His]-making",
    "heyot_ha_adam_levado": "the-human-being-alone",
    "mi_kol_etz_ha_gan": "from-every-tree-of-the-garden",
    "me_etz_ha_daat_tov_va_ra": "from-the-tree-of-knowledge-of-good-and-evil",
    "mot_tamut": "dying-you-shall-die",
    "oved_ve_shomer": "worker-and-keeper",
    "chayat_ha_sadeh": "beast-of-the-field",
    "of_ha_shamayim": "fowl-of-the-sky",
    "basar_echad": "one-flesh", "lo_yitboshashu": "were-not-ashamed",
    "hu_shemo": "that-is-its-name", "lo_matza": "did-not-find",
    "lo_himtir": "had-not-caused-rain", "adam_ayin": "no-human-existed",
    "nefesh_chaya": "living-being", "nishmat_chayim": "breath-of-life",
    "or_basar": "skin-of-flesh", "nega_tzaraat": "the-disease-mark",
    "b_tzelem_k_demut": "in-image-after-likeness",
    "kol_zorea_zera": "every-seed-bearing-plant", "le_okhlah": "for-food",
    "tov_meod": "very-good", "kol_asher_asah": "all-that-He-made",
}

# single-part glosses (machine-token cores across the frozen units)
GLOSS_CORE = {
    "shamayim": "heavens", "aretz": "earth", "eretz": "earth", "or": "light",
    "choshekh": "darkness", "tehom": "deep", "mayim": "waters",
    "ruach": "spirit-wind", "tohu": "unformed", "vohu": "void",
    "reshit": "beginning", "yom": "day", "layla": "night", "erev": "evening",
    "boqer": "morning", "raqia": "expanse", "yabasha": "dry-land",
    "yamim": "seas", "deshe": "vegetation", "esev": "herb", "etz": "tree",
    "pri": "fruit", "zera": "seed", "tov": "good", "ra": "evil",
    "meorot": "lights", "kokhavim": "stars", "moadim": "appointed-times",
    "otot": "signs", "taninim": "sea-monsters", "sheretz": "swarmers",
    "of": "fowl", "behemah": "livestock", "remes": "creepers",
    "chayah": "beast", "chaya": "living", "adam": "human",
    "adamah": "ground", "tzelem": "image", "demut": "likeness",
    "zakhar": "male", "nekevah": "female", "kadosh": "holy",
    "melakhah": "work", "tzevaam": "their-host", "gan": "garden",
    "eden": "Eden", "nahar": "river", "daat": "knowledge",
    "akhal": "eat", "akhol": "eating", "tokhal": "you-shall-eat",
    "mot": "dying", "tamut": "you-shall-die", "ezer": "helper",
    "ishah": "woman", "ish": "man", "av": "father", "em": "mother",
    "basar": "flesh", "tzela": "side-rib", "tardemah": "deep-sleep",
    "sagar": "shut", "banah": "build", "shemot": "names",
    "kohen": "priest", "tamei": "impure", "tahor": "pure",
    "seet": "swelling", "sapachat": "scab", "baheret": "bright-spot",
    "pisyon": "spreading", "make": "make", "exists": "exists",
    "arumim": "naked", "terem": "not-yet", "ed": "mist",
    "zahav": "gold", "bedolach": "bdellium", "shoham": "onyx-stone",
    "chavilah": "Havilah", "kush": "Cush", "ashur": "Asshur",
    "pishon": "Pishon", "gichon": "Gihon", "chidekel": "Tigris",
    "perat": "Euphrates", "ferat": "Euphrates", "rashim": "heads",
    "shivat": "seven", "shenit": "second-time", "swarm": "swarm",
    "sheva": "seven", "kol": "all", "khol": "all", "asah": "make",
    "bara": "create", "yatzar": "form", "asot": "making",
}

GLOSS_FUNC = {
    "ha": "the", "ve": "and", "va": "and", "u": "and", "be": "in",
    "le": "to", "la": "to", "mi": "from", "me": "from", "ke": "like",
    "el": "to", "al": "upon", "lo": "not", "hu": "that", "et": "",
    "min": "from", "bein": "between", "im": "if", "ki": "when",
    "mimenu": "from-it", "mimena": "from-it", "bo": "in-it",
    "oto": "it", "otah": "her", "lakh": "to-you", "lekha": "to-you",
    "elekha": "to-you", "beinkha": "between-you", "imah": "with-her",
    "imadi": "with-me", "akholkha": "your-eating",
    "akholkhem": "your-eating", "shuvkha": "your-return",
    "kol": "all", "khol": "all", "gam": "also", "pen": "lest",
    "ad": "until", "asher": "which", "sham": "there", "zot": "this",
}

# Supplement 2026-08-02 (owner order: every machine token translated in the
# Python renderings) — display glosses for token pieces the core set missed.
GLOSS_CORE.update({
    "elohim": "God", "noach": "Noach", "tevah": "ark", "laylah": "night",
    "mizbeach": "altar", "olah": "burnt-offering", "reiach": "odor",
    "nichoach": "pleasing-savor", "libo": "His-heart", "manoach": "resting-place",
    "mikhseh": "covering", "yonah": "dove", "tzippor": "bird",
    "hotze": "bring-out", "itakh": "with-you", "ito": "with-him",
    "elav": "to-him", "lahem": "to-them", "oti": "me", "atah": "you",
    "bakh": "in-you", "fiha": "her-mouth", "piha": "her-mouth",
    "apav": "his-nostrils", "apekha": "your-nostrils", "panekha": "your-face",
    "yado": "his-hand", "yadenu": "our-hands", "raglah": "her-foot",
    "achi": "my-brother", "achikha": "your-brother", "achiv": "his-brother",
    "eshet": "wife-of", "ishto": "his-wife", "ishekh": "your-husband",
    "emekh": "your-mother", "bnei": "sons-of", "bnot": "daughters-of",
    "banot": "daughters", "neshei": "wives-of", "vanekha": "your-sons",
    "anshei": "men-of", "shte": "two-of", "shneihem": "both-of-them",
    "adah": "Adah", "tzilah": "Tzillah", "naamah": "Naamah",
    "kayin": "Cain", "chavah": "Chavah-Eve", "hanokh": "Chanokh",
    "moshe": "Moses", "aharon": "Aaron", "harei": "mountains-of",
    "harim": "mountains", "rashei": "tops-of", "mayenot": "fountains-of",
    "mei": "waters-of", "meah": "hundred", "esreh": "-teen",
    "shanah": "year", "shnat": "year-of", "yemei": "days-of",
    "yamav": "his-days", "shivah": "seven", "shevii": "seventh",
    "shnayim": "two", "arbaah": "four", "meod": "very",
    "pnei": "face-of", "hinneh": "behold", "hineni": "behold-I",
    "eleh": "these", "zeh": "this", "chai": "living", "dam": "blood",
    "demei": "bloods-of", "amah": "cubit", "aleh": "leaf",
    "akev": "heel", "kotz": "thorn", "siach": "shrub",
    "sadeh": "field", "toledot": "generations", "tzaddik": "righteous",
    "tehorah": "clean", "rabbah": "great", "machah": "wipe",
    "charavah": "dry-land", "yavshah": "was-dry", "matzah": "found",
    "yasfah": "did-again", "reot": "see", "lemalah": "upward",
    "hakimoti": "I-will-establish", "briti": "My-covenant",
    "lefanai": "before-Me", "mashchitam": "destroying-them",
    "nishchatah": "was-corrupted", "darko": "its-way",
    "dorotav": "his-generations", "kofer": "pitch",
    "qomatah": "its-height", "rochbah": "its-width", "tzidah": "its-side",
    "shlishim": "third-decks", "shniyim": "second-decks",
    "minah": "its-kind", "minehu": "its-kind", "mikneh": "livestock",
    "minchah": "offering", "minchato": "his-offering", "shaah": "gaze",
    "chattat": "sin", "petach": "door-opening", "teshukatekh": "your-desire",
    "timshol": "you-shall-rule", "teitiv": "you-do-well",
    "yukam": "shall-be-avenged", "yahargeni": "will-kill-me",
    "harago": "slew-him", "horeg": "slayer", "motzi": "finder",
    "levilti": "so-as-not", "kochah": "its-strength",
    "patztah": "opened-wide", "tzoakim": "crying-out", "roeh": "shepherd",
    "qol": "voice", "shema": "hear", "likro": "to-call",
    "chaburati": "my-wound", "yenachamenu": "will-comfort-us",
    "maasenu": "our-work", "ererah": "cursed", "arurah": "cursed",
    "baavurekha": "for-your-sake", "itzvonekh": "your-toil",
    "heronekh": "your-pregnancy", "yimshol": "shall-rule",
    "yeshufkha": "shall-bruise-you", "teshufenu": "shall-bruise-him",
    "gechonkha": "your-belly", "eivah": "enmity", "kotnot": "garments-of",
    "tokhalenah": "you-shall-eat", "tokhel": "eat", "temutun": "you-shall-die",
    "chayekha": "your-life", "einei": "eyes-of", "eineikhem": "your-eyes",
    "nifqechu": "were-opened", "eirummim": "naked", "ayeka": "where-are-you",
    "kenegdo": "corresponding-to-him", "levado": "alone", "heyot": "being",
    "azav": "leave", "davak": "cleave", "eseh": "I-will-make",
    "aseh": "make", "hayah": "was", "hibaram": "their-being-created",
    "beraam": "when-created", "bidmut": "in-likeness-of",
    "dmutenu": "our-likeness", "dmuteNU": "our-likeness",
    "dmuto": "his-likeness", "tzalmo": "his-image", "tzalmO": "His-image",
    "tzalmenu": "our-image", "hithalekh": "walked-about",
    "einenu": "he-is-not", "einenah": "is-not", "hishqah": "watered",
    "yaaleh": "went-up", "mazria": "seeding", "okhlah": "food",
    "akhlah": "food", "atzei": "wood-of", "orot": "lights",
    "kivshuha": "subdue-it", "kavash": "subdue", "radah": "rule",
    "dagah": "fish", "dagat": "fish-of", "khen": "so",
    "lakach": "take", "lakachat": "taken", "baado": "about-him",
    "ruchi": "My-spirit", "machshevot": "thoughts", "hidekel": "Tigris",
    "oved": "worker", "shomer": "keeper", "kidmat": "east-of",
    "tzivah": "commanded", "tzivahu": "commanded-him", "ktiv": "written-form",
    "tihyeh": "shall-be", "arbeh": "I-will-multiply", "harbah": "greatly",
    "tzaraat": "the-disease", "timmeo": "pronounce-impure",
    "kibbes": "wash", "sear": "hair", "mareh": "appearance",
    "mareha": "its-appearance", "nirah": "seen", "heraoto": "its-appearing",
})
GLOSS_FUNC.update({"ba": "in-the", "ka": "like", "li": "to-me"})

GLOSS_UNIT = {}   # filled per unit from its own tree_coverage table


def build_unit_gloss(unit):
    """translit-core -> en-core, from the unit's own coverage rows."""
    g = {}
    tr_pre = ("va-", "ve-", "ha-", "la-", "le-", "be-", "mi-", "me-", "u-", "ke-")
    en_pre = ("and-", "the-", "to-", "in-", "from-", "for-", "like-")
    for verse in (unit.get("tree_coverage") or {}).get("verses", []):
        for w in verse.get("words", []):
            tr, en = str(w.get("he_translit", "")), str(w.get("en", ""))
            changed = True
            while changed:
                changed = False
                for p in tr_pre:
                    if tr.startswith(p):
                        tr, changed = tr[len(p):], True
                for p in en_pre:
                    if en.startswith(p):
                        en, changed = en[len(p):], True
            tr = tr.replace("-", "_").strip("_")
            if tr and en and tr not in g:
                g[tr] = en
    return g


def gloss_token(tok):
    """'aretz' -> 'earth'; 'mi_kol_etz_ha_gan' -> 'from-all-tree-the-garden'."""
    if tok in GLOSS_EXACT:
        return GLOSS_EXACT[tok]
    if tok in GLOSS_UNIT:
        return GLOSS_UNIT[tok]
    if tok in GLOSS_CORE:
        return GLOSS_CORE[tok]
    parts = tok.split("_")
    if len(parts) == 1:
        return GLOSS_FUNC.get(tok, "")
    out = []
    for p in parts:
        out.append(GLOSS_EXACT.get(p) or GLOSS_UNIT.get(p)
                   or GLOSS_CORE.get(p) or GLOSS_FUNC.get(p, p))
    return "-".join(x for x in out if x)


def with_gloss(tok):
    g = gloss_token(tok)
    return "%s %s(%s)%s" % (tok, DIM, g, RESET) if g and g != tok else tok


import re as _re


def gloss_expr(s):
    """English twin of a machine expression: every identifier glossed."""
    def repl(mt):
        tok = mt.group(0)
        g = gloss_token(tok)
        return g if g and g != tok else tok
    return _re.sub(r"[A-Za-z][A-Za-z_0-9]+", repl, s)


def wait_key():
    """One raw keypress (space/enter = advance, q = quit)."""
    if not sys.stdin.isatty():
        try:
            input()
            return " "
        except EOFError:
            return "q"
    import termios
    import tty
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    if ch in ("\x03", "q", "Q"):          # Ctrl-C / q
        return "q"
    return ch


def snapshot(m):
    return {
        "world": set(m.created_set()),
        "presup": set(m.presupposed_set()),
        "facts": len(m.WORLD["facts"]),
        "queue": [e["demand"] for e in m.SPECS["queue"]],
        "tests": [(t["verdict"], t["oracle"]) for t in m.TESTS],
        "names": dict(m.REGISTRY["names"]),
        "ledger": set(m.LEDGER),
        "flags": [(f["kind"], f["detail"]) for f in m.FLAGS],
        "triples": [(t["q"], t["discharged"]) for t in m.TRIPLES],
        "log_len": len(m.SPECS["log"]),
        "triple_len": len(m.TRIPLES),
        "partitions": list(m.WORLD["partitions"]),
        "invariants": list(m.WORLD["invariants"]),
    }


def show_changes(before, after, m):
    """What THIS verse did — only the deltas."""
    out = []

    def twin(prefix, expr):
        g = gloss_expr(expr)
        if g != expr:
            out.append(DIM + "  %s= %s" % (" " * len(prefix), g) + RESET)

    for e in sorted(after["world"] - before["world"]):
        out.append(GREEN + "  + WORLD install: %s" % with_gloss(e) + RESET)
    for e in sorted(after["presup"] - before["presup"]):
        out.append(YELLOW + "  ~ presupposed (read-before-install): %s"
                   % with_gloss(e) + RESET)
    if after["facts"] > before["facts"]:
        for f in m.WORLD["facts"][before["facts"]:]:
            out.append(GREEN + "  + standing fact: %s" % f + RESET)
            twin("+ standing fact: ", f)
    for entry in m.SPECS["log"][before["log_len"]:]:
        if entry["demand"] not in after["queue"]:
            out.append(GREEN + "  >< SPECS push+pop SAME VERSE [%s]: %s   (latency 0)"
                       % (entry["mood"], entry["demand"]) + RESET)
            twin(">< SPECS push+pop SAME VERSE [%s]: " % entry["mood"], entry["demand"])
    for d in after["queue"]:
        if d not in before["queue"]:
            mood = next((e["mood"] for e in m.SPECS["log"] if e["demand"] == d), "?")
            out.append(CYAN + "  > SPECS push [%s]: %s   (OPEN — a demand now waits)"
                       % (mood, d) + RESET)
            twin("> SPECS push [%s]: " % mood, d)
    for d in before["queue"]:
        if d not in after["queue"]:
            out.append(GREEN + "  < SPECS pop: %s   (demand SATISFIED)" % d + RESET)
            twin("< SPECS pop: ", d)
    for t in after["tests"]:
        if t not in before["tests"]:
            color = GREEN if t[0] == "PASS" else YELLOW
            out.append(color + "  * TEST %s(%s)" % (t[0], with_gloss(t[1])) + RESET)
    for k, v in after["names"].items():
        if before["names"].get(k) != v:
            out.append(GREEN + "  + REGISTRY write: %s -> %s"
                       % (with_gloss(k), with_gloss(v)) + RESET)
    for p in after["partitions"]:
        if p not in before["partitions"]:
            out.append(GREEN + "  | PARTITION: %s ∩ %s = ∅   (%s and %s no longer mix)"
                       % (p[0], p[1], gloss_token(p[0]) or p[0],
                          gloss_token(p[1]) or p[1]) + RESET)
    for inv in after["invariants"]:
        if inv not in before["invariants"]:
            out.append(CYAN + "  ~ INVARIANT active: %s" % inv + RESET)
            twin("~ INVARIANT active: ", inv)
    for day in sorted(after["ledger"] - before["ledger"]):
        out.append(BOLD + GREEN + "  # LEDGER COMMIT: day %s closed" % day + RESET)
    for f in after["flags"]:
        if f not in before["flags"]:
            out.append(YELLOW + "  ! FLAG %s: %s" % f + RESET)
    for q, disch in after["triples"][before["triple_len"]:]:
        if disch:
            out.append(GREEN + "  ?= TRIPLE posted and discharged SAME VERSE: {%s}" % q + RESET)
        else:
            out.append(CYAN + "  ? TRIPLE posted: {%s}   (stands undischarged)" % q + RESET)
        twin("? TRIPLE: ", q)
    for q, disch in after["triples"][:before["triple_len"]]:
        if (q, False) in before["triples"] and disch:
            out.append(GREEN + "  = TRIPLE discharged: {%s}" % q + RESET)
    if not out:
        out.append(DIM + "  (no register changes — state/description only)" + RESET)
    return out


def registers_line(m):
    return (DIM + "  registers: WORLD=%d installed, %d presupposed | facts=%d | "
            "SPECS open=%d | TESTS=%d | REGISTRY writes=%d | LEDGER=%s | flags=%d" % (
                len(m.created_set()), len(m.presupposed_set()),
                len(m.WORLD["facts"]), len(m.SPECS["queue"]), len(m.TESTS),
                m.REGISTRY["writes"], sorted(m.LEDGER) or "[]",
                len(m.FLAGS)) + RESET)


def step_through(unit_id):
    unit = ru.load_unit(unit_id)          # frozen gate stays in force
    ru.validate_unit(unit)
    GLOSS_UNIT.clear()
    GLOSS_UNIT.update(build_unit_gloss(unit))
    meta = unit["meta"]
    steps = sorted(unit.get("boot_steps", []), key=lambda s: s.get("order", 0))

    print("\n" + BOLD + "=" * 72 + RESET)
    print(BOLD + "%s — %s" % (meta["id"], meta.get("title_en", "")) + RESET)
    print(DIM + "%d verse-steps · SPACE = next verse · q = quit" % len(steps) + RESET)
    print(BOLD + "=" * 72 + RESET)

    m = ru.Machine()
    for i, step in enumerate(steps, 1):
        if wait_key() == "q":
            print(DIM + "\n(stopped at owner's request — %d of %d steps run)"
                  % (i - 1, len(steps)) + RESET)
            return m, False

        before = snapshot(m)
        m._step_ref = step["ref"]

        print("\n" + BOLD + "[%d/%d] %s  %s  %s" % (
            i, len(steps), step["id"], step["ref"],
            CYAN + "[%s]" % step.get("op", "") + RESET) + RESET)
        print("  " + step.get("he", ""))
        print(DIM + "  %s" % step.get("he_translit", "") + RESET)
        print("  %s" % step.get("en", "").replace("[EN-AID/JPS] ", "").replace("[EN-AID] ", ""))
        print()
        for op in step.get("operators", []):
            ru.HANDLERS[op["op"]](m, op, step)
            cites = ",".join(op.get("cites") or []) or "-"
            print("   %s%-18s%s %s  %s[%s]%s" % (
                BOLD, op["op"], RESET, op.get("expr_en", ""), DIM, cites, RESET))
        print()
        for line in show_changes(before, snapshot(m), m):
            print(line)
        print(registers_line(m))

    print("\n" + BOLD + "-- unit complete --" + RESET)
    open_d = [e["demand"] for e in m.SPECS["queue"]]
    print("final WORLD:    %s" % ", ".join(with_gloss(e) for e in sorted(m.created_set())))
    print("final REGISTRY: %s" % (", ".join("%s -> %s" % (with_gloss(k), with_gloss(v))
          for k, v in m.REGISTRY["names"].items()) or "(no writes)"))
    print("final TESTS:    %s | LEDGER: %s" % (
        [(t["verdict"], t["oracle"]) for t in m.TESTS] or "(none)",
        sorted(m.LEDGER) or "[]"))
    if open_d:
        print(YELLOW + BOLD + "STILL OPEN at unit end: — the unit ends owing." + RESET)
        for d in open_d:
            print(YELLOW + "    %s" % d + RESET)
            print(DIM + "    = %s" % gloss_expr(d) + RESET)
    return m, True


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    for unit_id in args:
        try:
            _, done = step_through(unit_id)
            if not done:
                break
        except ru.ContractError as e:
            print("CONTRACT: %s" % e, file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
