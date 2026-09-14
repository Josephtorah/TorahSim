#!/usr/bin/env python3
"""build_diagrams.py — draws the ARCHITECTURE folder's SVG diagrams.

Pure Python, no dependencies. Writes only into ARCHITECTURE/diagrams/.
Touches nothing else in the repository. Re-run after any change to the
markdown so the pictures and the prose stay in step:

    python3 ARCHITECTURE/tools/build_diagrams.py

Every box and arrow here restates something the markdown cites; the
diagrams add no facts of their own.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "diagrams")
os.makedirs(OUT, exist_ok=True)

GOLD, RED, BLUE, SOFT, INK, CARD, LINE = (
    "#6e5417", "#a33b1f", "#2f5d8a", "#57503f", "#1e1b14", "#fffdf6", "#cdb56a")
FONT = 'font-family="Georgia,serif"'


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


class SVG:
    def __init__(self, w, h):
        self.w, self.h, self.parts = w, h, []
        self.parts.append(
            '<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" '
            'markerWidth="7" markerHeight="7" orient="auto">'
            '<path d="M0 0L10 5L0 10z" fill="%s"/></marker>'
            '<marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" '
            'markerWidth="7" markerHeight="7" orient="auto">'
            '<path d="M0 0L10 5L0 10z" fill="%s"/></marker>'
            '<marker id="arb" viewBox="0 0 10 10" refX="9" refY="5" '
            'markerWidth="7" markerHeight="7" orient="auto">'
            '<path d="M0 0L10 5L0 10z" fill="%s"/></marker></defs>'
            % (GOLD, RED, BLUE))
        self.parts.append('<rect x="0" y="0" width="%d" height="%d" fill="#fbf8f0"/>'
                          % (w, h))

    def box(self, x, y, w, h, title, lines=(), stroke=GOLD, fill=CARD,
            title_size=13, line_size=11, dashed=False):
        dash = ' stroke-dasharray="6 4"' if dashed else ''
        self.parts.append(
            '<rect x="%d" y="%d" width="%d" height="%d" rx="9" fill="%s" '
            'stroke="%s" stroke-width="2"%s/>' % (x, y, w, h, fill, stroke, dash))
        cx = x + w / 2
        self.parts.append(
            '<text x="%.1f" y="%d" text-anchor="middle" font-size="%d" '
            'font-weight="bold" fill="%s">%s</text>'
            % (cx, y + 20, title_size, stroke, esc(title)))
        for i, ln in enumerate(lines):
            self.parts.append(
                '<text x="%.1f" y="%d" text-anchor="middle" font-size="%d" '
                'fill="%s">%s</text>'
                % (cx, y + 38 + i * (line_size + 4), line_size, SOFT, esc(ln)))

    def arrow(self, x1, y1, x2, y2, label="", color=GOLD, dashed=False,
              curve=0, label_dy=-6, size=10.5, label_t=0.5):
        marker = {GOLD: "ar", RED: "arr", BLUE: "arb"}.get(color, "ar")
        dash = ' stroke-dasharray="6 4"' if dashed else ''
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        t = label_t
        if curve:
            # perpendicular offset for the control point
            dx, dy = x2 - x1, y2 - y1
            n = (dx * dx + dy * dy) ** 0.5 or 1
            cx, cy = mx - dy / n * curve, my + dx / n * curve
            self.parts.append(
                '<path d="M %.1f %.1f Q %.1f %.1f %.1f %.1f" fill="none" '
                'stroke="%s" stroke-width="2" marker-end="url(#%s)"%s/>'
                % (x1, y1, cx, cy, x2, y2, color, marker, dash))
            # point on the quadratic curve at parameter t
            lx = (1 - t) ** 2 * x1 + 2 * (1 - t) * t * cx + t * t * x2
            ly = (1 - t) ** 2 * y1 + 2 * (1 - t) * t * cy + t * t * y2
        else:
            self.parts.append(
                '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                'stroke-width="2" marker-end="url(#%s)"%s/>'
                % (x1, y1, x2, y2, color, marker, dash))
            lx, ly = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
        if label:
            self.parts.append(
                '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%s" '
                'fill="%s">%s</text>' % (lx, ly + label_dy, size, color, esc(label)))

    def text(self, x, y, s, size=12, color=SOFT, anchor="middle", italic=False,
             bold=False):
        st = (' font-style="italic"' if italic else '') + \
             (' font-weight="bold"' if bold else '')
        self.parts.append(
            '<text x="%.1f" y="%.1f" text-anchor="%s" font-size="%d" fill="%s"%s>%s'
            '</text>' % (x, y, anchor, size, color, st, esc(s)))

    def write(self, name):
        body = "\n".join(self.parts)
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
               'width="%d" height="%d" %s>\n%s\n</svg>\n'
               % (self.w, self.h, self.w, self.h, FONT, body))
        path = os.path.join(OUT, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        print("wrote", os.path.relpath(path, os.path.dirname(HERE)))


# ---------------------------------------------------------------- 1. layers
def layers():
    s = SVG(980, 560)
    s.text(490, 30, "The six layers of the compiled code, and how data moves between them (counts of 2026-09-13)",
           14, INK, bold=True)
    # row 1
    s.box(30, 60, 260, 120, "0  INK", [
        "tanakh.sqlite: words, lemmas,", "cantillation marks, scribal dots",
        "the whole Hebrew Bible, read-only"], GOLD)
    s.box(360, 60, 260, 120, "1  SPEC  (frozen units)", [
        "logic/units/*.yaml, one claim set per span",
        "210 frozen: Genesis 73, Exodus 41, Leviticus 49, Numbers 47",
        "rendered as assert-backed logic/py_units/*.py"], GOLD)
    s.box(690, 60, 260, 120, "2  WORLD  (the fold)", [
        "corpus_world.py + entity_registry.yaml",
        "210 units -> 1,809 facts,",
        "341 demands (191 open), standing 2,163",
        "hash 8b8fff1fa28953af"], GOLD)
    # row 2
    s.box(30, 300, 260, 130, "3  CODE  (cold runs)", [
        "World/step9/cold_run_*.py",
        "57 runners, 427 compiled functions",
        "6,378 graded cells, 57/57 on the sweep",
        "every verdict carries registry effects"], RED)
    s.box(360, 300, 260, 130, "4  TEST  (the exam)", [
        "*_rules.py + cases_*.yaml + vocabulary.yaml",
        "47 rounds, 1,595/1,595; the union-rule dockets",
        "43 rules modules, 47 case files",
        "158 dimensions, 1,501 values"], BLUE)
    s.box(690, 300, 260, 130, "5  RUNTIME  (the engine)", [
        "World/step9/world_engine.py",
        "entities with ledgers, laws as daemons,",
        "timers, the calendar, the journal, the diff engine",
        "62 daemons; one tape, 1,279 events, 157 dates"], BLUE)
    # registries strip
    s.box(30, 480, 920, 60, "cross-cutting registries", [
        "effect_vocabulary.yaml (1,012 effects, 8 ledger ops)  ·  MOVE_CATALOG.md (M-01..M-30)  ·  "
        "MIDDOT.md  ·  findings F-001..  ·  entity_registry.yaml"], SOFT, title_size=12)
    # arrows
    s.arrow(290, 120, 360, 120, "derive (Step 2-3)")
    s.arrow(620, 120, 690, 120, "fold, in canonical order")
    s.arrow(160, 180, 160, 300, "compile from the ink alone (motion 1)", RED, label_dy=-4)
    s.arrow(360, 350, 290, 350, "grade (motions 3-5)", BLUE, label_dy=-8)
    s.arrow(290, 390, 360, 390, "misses -> Talmud -> labeled move", RED, label_dy=14)
    s.arrow(620, 365, 690, 365, "declared checkpoints", BLUE, label_dy=-6)
    s.arrow(290, 320, 690, 320, "wrapped as daemons", RED, curve=-40, label_dy=-30)
    s.arrow(820, 180, 820, 300, "population: entities, events, closers", GOLD, label_dy=-4)
    s.arrow(440, 180, 240, 300, "findings auto-seat back into the units", RED, dashed=True,
            curve=30, label_dy=26)
    s.arrow(490, 480, 490, 430, "", SOFT, dashed=True)
    s.arrow(160, 480, 160, 430, "", SOFT, dashed=True)
    s.text(490, 555, "Layers 1 and 2 are the proof machine (one execution, replayed to the hash). "
           "Layers 3 to 5 are the simulation machine.", 11, SOFT, italic=True)
    s.write("01_layers.svg")


# ------------------------------------------------------ 2. span dependencies
def dependencies():
    s = SVG(1210, 880)
    s.text(605, 28, "The 14 compiled spans of 2026-09-05 and every cross-span edge named then (the 57 of 2026-09-13: DEPENDENCIES.md)",
           14, INK, bold=True)
    s.text(130, 70, "BOOKS REACHED, NOT COMPILED", 12, SOFT, bold=True)
    s.text(450, 62, "EXODUS", 13, GOLD, bold=True)
    s.text(810, 62, "LEVITICUS", 13, GOLD, bold=True)
    s.text(1080, 70, "OTHER TARGETS", 12, SOFT, bold=True)
    ex = [("decalogue", "Exod 20 law layer", 12),
          ("mishpatim", "Exod 21:2-22:3, 5 fns", 23),
          ("mishpatim_2", "Exod 21-22, 3 more fns", 9),
          ("guardians", "Exod 22:6-14", 12),
          ("pesach", "Exod 12-13", 24),
          ("calendar", "Exod 23:10-19", 14)]
    lv = [("vayikra5", "Lev 5", 27), ("tzav", "Lev 6-8", 33),
          ("offerings", "Lev 1-8 dispatcher", 40), ("shemini", "Lev 11", 19),
          ("negaim", "Lev 13-14", 16), ("yoma", "Lev 16", 18),
          ("moadim", "Lev 23", 24), ("lev24", "Lev 24:10-23", 23)]
    pos = {}
    for i, (k, sub, n) in enumerate(ex):
        y = 80 + i * 100
        s.box(350, y, 200, 62, "cold_run_%s" % k, [sub, "%d/%d cells" % (n, n)], GOLD, title_size=12)
        pos[k] = (350, y, 200, 62)
    for i, (k, sub, n) in enumerate(lv):
        y = 80 + i * 84
        s.box(710, y, 200, 62, "cold_run_%s" % k, [sub, "%d/%d cells" % (n, n)], GOLD, title_size=12)
        pos[k] = (710, y, 200, 62)
    left = [("deut25", "Deuteronomy 25:11-12", ["humiliation's source"]),
            ("lev25", "Leviticus 25:9-10", ["the Jubilee; units still drafts",
                                            "reached twice: release (mishpatim),",
                                            "shofar (moadim)"]),
            ("deut22", "Deuteronomy 22:29", ["the fifty-shekel constant"]),
            ("deut14", "Deuteronomy 14:21", ["kid-in-milk, the third seat"])]
    for i, (k, t, sub) in enumerate(left):
        y = 90 + i * 118
        h = 44 + 15 * len(sub)
        s.box(30, y, 200, h, t, sub, SOFT, title_size=11.5, dashed=True, line_size=10)
        pos[k] = (30, y, 200, h)
    right = [("noah", 140, "Sanhedrin 56a, Noahide block", ["the epithet arm"]),
             ("sam", 300, "1 Samuel 2:15-17", ["the sons of Eli, a run log"])]
    for k, y, t, sub in right:
        s.box(980, y, 200, 58, t, sub, SOFT, title_size=11.5, dashed=True)
        pos[k] = (980, y, 200, 58)
    s.box(480, 790, 260, 58, "world_engine.py", ["5 daemons wrapped, 6 recorded scenes"], BLUE, title_size=12)
    pos["engine"] = (480, 790, 260, 58)

    def c(k, side):
        x, y, w, h = pos[k]
        return {"r": (x + w, y + h / 2), "l": (x, y + h / 2),
                "t": (x + w / 2, y), "b": (x + w / 2, y + h),
                "tl": (x + 40, y), "tr": (x + w - 40, y)}[side]

    def edge(a, sa, b, sb, label, color=RED, curve=0, dashed=False, dy=-6, t=0.5, size=10):
        (x1, y1), (x2, y2) = c(a, sa), c(b, sb)
        s.arrow(x1, y1, x2, y2, label, color, dashed, curve, dy, size, label_t=t)

    # inside the compiled set
    edge("decalogue", "b", "mishpatim", "t", "ROUTES theft + capital laws", GOLD, dy=-4)
    edge("mishpatim", "r", "lev24", "l", "CALLS talion()", RED, curve=80, dy=14, t=0.5)
    edge("offerings", "l", "pesach", "r", "ROUTES the Passover row", RED, curve=20, dy=-6, t=0.5)
    edge("vayikra5", "b", "offerings", "t", "", GOLD, curve=-70)
    edge("tzav", "b", "offerings", "t", "case-law layer", GOLD, dy=12, t=0.35)
    edge("moadim", "l", "pesach", "r", "shares Pesachim 5:3", BLUE, dashed=True, curve=-20, dy=14, t=0.5)
    # into books not compiled (left column)
    edge("mishpatim", "l", "deut25", "r", "IMPORT: humiliation", RED, dy=-6, size=9.5)
    edge("mishpatim", "l", "lev25", "r", "IMPORT: Jubilee release", RED, dy=-6, size=9.5)
    edge("mishpatim_2", "l", "deut22", "r", "FETCH: fifty shekels", RED, dy=-6, size=9.5)
    edge("calendar", "l", "deut14", "r", "census: third seat", GOLD, dy=-6, size=9.5)
    # other targets (right column)
    edge("tzav", "r", "sam", "l", "run-log check", BLUE, dy=-6, t=0.5)
    edge("lev24", "r", "noah", "l", "ROUTES epithet arm", GOLD, dy=-6, t=0.5)
    # into the engine (bottom row)
    edge("mishpatim", "r", "engine", "tl", "daemons: slave clock, ox", BLUE, curve=-70, dy=-6, t=0.86)
    edge("guardians", "b", "engine", "tl", "daemon: guardians", BLUE, curve=-80, dy=14, t=0.8)
    edge("vayikra5", "l", "engine", "tr", "daemon: deposit oath", BLUE, curve=70, dy=-6, t=0.66)
    edge("tzav", "l", "engine", "tr", "daemon: installation", BLUE, curve=60, dy=14, t=0.72)
    s.text(605, 868, "Solid red: a compiled span reaching into another span or book. Gold: routing and census edges. "
           "Blue: wrapped into the engine or checked against a run log. Dashed boxes are not compiled yet.",
           10.5, SOFT, italic=True)
    s.write("02_dependencies.svg")


# ----------------------------------------------------------- 3. goring ox
def ox():
    s = SVG(900, 380)
    s.text(450, 28, "The goring ox: a two-state machine with a counted transition (Exodus 21:28-36)",
           14, INK, bold=True)
    s.box(60, 90, 260, 110, "INNOCUOUS  (tam)", [
        "damage to an ox: pays HALF,", "out of the ox's own body", "ink 21:35: 'they divide'"], GOLD)
    s.box(580, 90, 260, 110, "FOREWARNED  (muad)", [
        "damage to an ox: pays FULL", "ink 21:36: 'ox for ox'",
        "human victim: ransom may be imposed (21:30)"], RED)
    s.arrow(320, 130, 580, 130, "third goring -> flips  [Bava Kamma 23b: yesterday + day-before = three]", RED, label_dy=-8)
    s.arrow(580, 170, 320, 170, "reverts: three days restrained, or children handle it and it does not gore  [Mishnah Bava Kamma 2:4]",
            GOLD, dashed=True, label_dy=16, size=10)
    s.box(330, 250, 240, 90, "either state, human victim", [
        "the ox is STONED (21:28-29)", "slave victim: thirty shekels fixed (21:32)"], BLUE)
    s.arrow(190, 200, 370, 250, "", BLUE)
    s.arrow(710, 200, 530, 250, "", BLUE)
    s.text(450, 365, "Effects written: pays (half or full), forewarned (status), stoned, ransom_imposed, gives_fixed_sum. "
           "Daemon: world_engine.law_goring_ox.", 10.5, SOFT, italic=True)
    s.write("03_goring_ox.svg")


# ------------------------------------------------------------ 4. slave clock
def slave():
    s = SVG(960, 400)
    s.text(480, 28, "The Hebrew slave's clock, and the interrupt that crosses books (Exodus 21:2-6 with Leviticus 25:10)",
           14, INK, bold=True)
    s.box(40, 80, 200, 90, "ACQUIRED", ["ink 21:2: 'when you acquire'", "term_clock set: six years"], GOLD)
    s.box(330, 80, 220, 90, "SERVING", ["timer runs; deduction of money", "is a computed early exit [Kiddushin 16a]"], GOLD)
    s.box(660, 80, 240, 90, "FREE  (year seven)", ["ink 21:2: 'in the seventh he goes out free'", "effect goes_free, timer fires"], BLUE)
    s.arrow(240, 125, 330, 125, "")
    s.arrow(550, 125, 660, 125, "timer fires at year 6", BLUE)
    s.box(330, 240, 220, 100, "PIERCED  'forever'", ["ink 21:5-6: the slave's own declaration", "the six-year timer is CANCELLED",
                                                     "engine: cancel_timers()"], RED)
    s.arrow(440, 170, 440, 240, "declares 'I love my master'", RED, label_dy=-4)
    s.box(660, 240, 240, 100, "JUBILEE RELEASE", ["Leviticus 25:10 'you shall return every man'",
                                                  "Kiddushin 15a: written for the pierced one", "effect jubilee_release, a 50-year timer"], RED, dashed=True)
    s.arrow(550, 290, 660, 290, "IMPORT from another book", RED, label_dy=-6)
    s.text(480, 385, "'Forever' is a scoped constant; its scope is set in Leviticus. Daemon: world_engine.law_slave_term.",
           10.5, SOFT, italic=True)
    s.write("04_slave_clock.svg")


# --------------------------------------------------------- 5. the affliction
def affliction():
    s = SVG(1000, 640)
    s.text(500, 28, "The affliction machine (Leviticus 13-14): three tracks, shared-day weeks, and the ten houses",
           14, INK, bold=True)
    # person track
    s.text(60, 70, "PERSON  (skin, boil, burn, scall, bald)", 12, GOLD, bold=True, anchor="start")
    s.box(40, 85, 170, 70, "examined", ["ink 13:3: the priest sees"], GOLD, title_size=12)
    s.box(260, 85, 170, 70, "SHUT-IN week 1", ["ink 13:4 'and he shall shut'"], GOLD, title_size=12)
    s.box(480, 85, 170, 70, "SHUT-IN week 2", ["skin, scall, bald only;", "boil and burn: one week (ink's silence)"], GOLD, title_size=12)
    s.box(720, 60, 240, 60, "DECREED IMPURE", ["isolated_outside_camp (13:45-46)"], RED, title_size=12)
    s.box(720, 140, 240, 60, "RELEASED", ["ink 13:6: washed and pure"], BLUE, title_size=12)
    s.arrow(210, 120, 260, 120, "no sign yet")
    s.arrow(430, 120, 480, 120, "stood")
    s.arrow(650, 105, 720, 90, "a decreeing sign", RED, label_dy=-10, size=10)
    s.arrow(650, 135, 720, 165, "dim or gone", BLUE, label_dy=14, size=10)
    s.arrow(430, 100, 720, 75, "sign in week 1", RED, curve=-30, label_dy=-8, size=10)
    s.text(500, 190, "two weeks = THIRTEEN days: day seven closes week one and opens week two [Sifra; Mishnah Negaim 3:3]",
           10.5, SOFT, italic=True)
    # garment track
    s.text(60, 240, "GARMENT", 12, GOLD, bold=True, anchor="start")
    s.box(40, 255, 170, 60, "SHUT-IN week 1", ["ink 13:50"], GOLD, title_size=12)
    s.box(260, 255, 170, 60, "SHUT-IN week 2", ["washed first (13:54)"], GOLD, title_size=12)
    s.box(480, 255, 170, 60, "BURNED", ["ink 13:55; effect burned_in_fire"], RED, title_size=12)
    s.box(720, 255, 240, 60, "washed, PURE", ["13:58; the asymmetry with the person"], BLUE, title_size=12)
    s.arrow(210, 285, 260, 285, "stood")
    s.arrow(430, 285, 480, 285, "spread or stood", RED)
    s.arrow(430, 300, 720, 300, "gone after washing", BLUE, curve=30, label_dy=18, size=10)
    # house track
    s.text(60, 360, "HOUSE  (three weeks = NINETEEN days)", 12, GOLD, bold=True, anchor="start")
    s.box(40, 375, 170, 60, "SHUT week 1", ["ink 14:38"], GOLD, title_size=12)
    s.box(260, 375, 170, 60, "SHUT week 2", ["after 'stood'"], GOLD, title_size=12)
    s.box(480, 375, 190, 70, "PULL, SCRAPE, PLASTER", ["ink 14:40-42; one more week"], GOLD, title_size=11.5)
    s.box(720, 360, 240, 50, "PEEL, PURE", ["dim or gone in week 1"], BLUE, title_size=12)
    s.box(720, 425, 240, 50, "PEEL + BIRDS", ["stood then dim or gone; 14:49-53"], BLUE, title_size=12)
    s.box(480, 490, 190, 60, "DEMOLISHED", ["ink 14:45 'and he shall tear down'", "effect demolished"], RED, title_size=12)
    s.box(720, 490, 240, 60, "BIRDS  (quiet after plaster)", ["the returning fork's other arm"], BLUE, title_size=12)
    s.arrow(210, 405, 260, 405, "stood")
    s.arrow(210, 390, 720, 385, "dim / gone in week 1", BLUE, curve=-40, label_dy=-6, size=10)
    s.arrow(430, 405, 720, 450, "dim / gone in week 2", BLUE, curve=20, label_dy=-6, size=10, label_t=0.75)
    s.arrow(430, 420, 480, 420, "spread, or stood-stood", RED, label_dy=16, size=10)
    s.arrow(125, 435, 480, 445, "spread in week 1", RED, curve=50, label_dy=20, size=10)
    s.arrow(575, 445, 575, 490, "RETURNED", RED, label_dy=-4, size=10)
    s.arrow(670, 430, 720, 510, "quiet", BLUE, label_dy=12, size=10)
    s.text(500, 600, "The ten-houses table (Sifra, Metzora, Section 7) is the teacher's own enumeration of this tree; "
           "the compiled house machine reproduces all ten rows.", 10.5, SOFT, italic=True)
    s.text(500, 622, "Source: cold_run_negaim.py (16/16 cells + 10/10 houses).", 10.5, SOFT, italic=True)
    s.write("05_affliction_machine.svg")


# ------------------------------------------------------- 6. the installation
def installation():
    s = SVG(960, 330)
    s.text(480, 28, "The installation transaction (Leviticus 8): atomic components, a seven-day timer, a commit point",
           14, INK, bold=True)
    s.box(30, 80, 210, 100, "COMMANDED", ["components checked: bullock,", "ram (olah), ram (milluim), basket",
                                          "missing any -> ATOMIC-BLOCK, nothing happens"], GOLD, title_size=12)
    s.box(300, 80, 200, 100, "CONFINED  7 days", ["ink 8:33 'you shall not go out'", "effect confined_seven_days",
                                                  "timer: released at day seven"], GOLD, title_size=12)
    s.box(560, 80, 190, 100, "INVESTED", ["commit at the blood sprinkling", "[Sifra, Mekhilta DeMiluim I 34]",
                                          "effect invested_office"], RED, title_size=12)
    s.box(790, 80, 150, 100, "RELEASED", ["day seven; the timer fires", "effect released"], BLUE, title_size=12)
    s.arrow(240, 130, 300, 130, "all four present")
    s.arrow(500, 130, 560, 130, "milluim blood sprinkled", RED, label_dy=-6, size=10)
    s.arrow(750, 130, 790, 130, "", BLUE)
    s.box(300, 220, 200, 70, "LEFTOVER", ["ink 8:32: 'what remains you shall burn'", "effect burn_remainder"], SOFT, title_size=12)
    s.arrow(400, 180, 400, 220, "any remainder", SOFT, label_dy=-4, size=10)
    s.text(480, 315, "Daemon: world_engine.law_installation, compiled from cold_run_tzav.py F7. "
           "Scene 6 of the engine replays Leviticus 8 itself as the tape.", 10.5, SOFT, italic=True)
    s.write("06_installation.svg")


# ------------------------------------------------------- 7. Yom Kippur order
def yoma():
    steps = [
        ("16:3", "bull designated"), ("16:4", "linen donned"), ("16:5", "two goats taken"),
        ("16:6", "first confession"), ("16:7-8", "goats stationed; lots"), ("16:9-10", "Name-goat named"),
        ("16:11", "second confession; bull slain"), ("16:12-13", "coals and incense inside"),
        ("16:14", "bull blood: one up, seven down"), ("16:15", "goat slain; its blood"),
        ("16:16-17", "the hall atoned"), ("16:18-19", "inner altar: mixed bloods"),
        ("16:20-22", "third confession; goat dispatched"), ("16:24", "immersion; the two rams"),
        ("16:25", "fat to smoke"), ("16:23", "RELOCATED: linen stripped"), ("16:26", "dispatcher washes"),
        ("16:27-28", "the burnt pair outside"),
    ]
    cols, w, h, gx, gy = 6, 140, 58, 155, 90
    s = SVG(60 + cols * gx, 120 + 3 * gy + 40)
    s.text(s.w / 2, 28, "The Yom Kippur service order (Leviticus 16): the verse sequence as the program counter, one recorded relocation",
           13.5, INK, bold=True)
    for i, (ref, what) in enumerate(steps):
        r, c = divmod(i, cols)
        x, y = 30 + c * gx, 60 + r * gy
        color = RED if ref == "16:23" else GOLD
        s.box(x, y, w, h, "%d. %s" % (i + 1, ref), [what], color, title_size=11.5, line_size=10)
        if i + 1 < len(steps):
            r2, c2 = divmod(i + 1, cols)
            if r2 == r:
                s.arrow(x + w, y + h / 2, x + gx, y + h / 2, "", GOLD)
            else:
                s.arrow(x + w / 2, y + h, 30 + w / 2, 60 + r2 * gy, "", GOLD, curve=-120)
    s.text(s.w / 2, s.h - 14, "Step 16 executes late by the Sifra's order meta-rule: 'the whole passage is in order except this verse' "
           "(Acharei Mot, Chapter 6). Source: cold_run_yoma.py, 18/18.", 10.5, SOFT, italic=True)
    s.write("07_yom_kippur_order.svg")


# ----------------------------------------------- 8. the fourth book's runners
def numbers_runners():
    """The eighteen runners of the book of Numbers in scroll order, each with its span, its score as printed on the
    2026-09-13 rerun (catalog_facts.json), and the earlier programs it calls live (DEPENDENCY_INDEX.md)."""
    import json, re
    facts = json.load(open(os.path.join(os.path.dirname(HERE), "catalog_facts.json"), encoding="utf-8"))["spans"]
    dep = open(os.path.join(os.path.dirname(os.path.dirname(HERE)), "World", "step9", "DEPENDENCY_INDEX.md"), encoding="utf-8").read()
    calls = {}
    for sec in re.split(r"\n(?=## cold_run_)", dep):
        m = re.match(r"## (cold_run_\w+)\.py — (.*)", sec.split("\n", 1)[0])
        if not m: continue
        co = re.search(r"- calls out \(live\): (.*)", sec)
        calls[m.group(1)] = (m.group(2).strip(), co.group(1).strip() if co else "none")
    order = ["bamidbar", "naso", "beha", "pesach_sheni", "shelach", "mekoshesh", "korach", "chukat", "balak", "second_census",
             "zelophehad", "musafim", "vows", "midian", "gad_reuben", "journeys", "borders", "refuge"]
    cols, w, h, gx, gy = 3, 380, 96, 400, 112
    rows = (len(order) + cols - 1) // cols
    s = SVG(40 + cols * gx, 70 + rows * gy + 30)
    s.text(s.w / 2, 28, "The fourth book's eighteen runners, in scroll order: span, score on the 2026-09-13 rerun, and the programs each calls live", 13.5, INK, bold=True)
    for i, k in enumerate(order):
        r, c = divmod(i, cols)
        x, y = 20 + c * gx, 50 + r * gy
        name = "cold_run_%s" % k
        span, co = calls.get(name, ("", "none"))
        sl = (facts.get(name) or {}).get("score_line") or ""
        m = re.search(r"(\d+/\d+)", sl)
        span_short = span if len(span) <= 52 else span[:49] + "..."
        callees = [c_.strip() for c_ in co.split(",")] if co != "none" else []
        line1 = "calls: " + ", ".join(callees[:6]) + (" ..." if len(callees) > 6 else "") if callees else "calls: none"
        line2 = "      " + ", ".join(callees[6:12]) + (" ..." if len(callees) > 12 else "") if len(callees) > 6 else ""
        lines = [span_short, "%s cells" % m.group(1) if m else "(no matrix line)", line1] + ([line2] if line2 else [])
        s.box(x, y, w, h, name, lines, GOLD, title_size=12, line_size=10)
    s.text(s.w / 2, s.h - 12, "Every call is a live import the dependency gate verified; the labels and teachers are in DEPENDENCIES.md and THE_LINKS.md.", 10.5, SOFT, italic=True)
    s.write("08_numbers_runners.svg")


if __name__ == "__main__":
    layers(); dependencies(); ox(); slave(); affliction(); installation(); yoma(); numbers_runners()
