#!/usr/bin/env python3
"""dependency_census.py — THE DEPENDENCY GATE (2026-09-06, the dependency-debt
sitting; the owner: "make sure we code properly going forward").

The dependency audit (REPORT_DEPENDENCIES.md) found that motion (1) of the
compile compiled a span's ink but never censused its CROSS-REFERENCES, so a
dependency became a live call only when a Mishnah row happened to name the
other type; the rest stood as notes or silence. This tool makes the census a
GATE that runs before every cold sweep (run_cold_all.py calls it first):

  1. Every cold_run_*.py must DECLARE its verse span in
     dependency_dispositions.yaml (spans:). An undeclared runner fails.
  2. THE TYPE CENSUS: every verse of every declared span is scanned for the
     type tokens below (the burnt, meal, sin, peace, and guilt offerings, the
     bird pair, the Passover, the firstborn, the tithe, the valuation, the
     jubilee, the seventh year, the installation, leprosy, the discharges,
     interest, the Hebrew slave, the ghost and familiar spirit, the talion
     formula). A token whose HOME runner is another runner is a REQUIRED EDGE
     runner -> home.
  3. THE POINTER CENSUS: every explicit cross-reference form inside a
     declared span — "as prescribed" (כמשפט), "as/when" (כאשר) before a
     procedure verb, the comparative kaf on an offering noun, "one law" — is
     a REQUIRED POINTER at its verse.
  4. Every required edge and pointer must carry a DISPOSITION in the yaml:
       CALL       — a live import edge exists (verified against the source);
       OWED       — the callee is not compiled yet; the entry names a
                    COMPILE_DEBT.md line (verified by substring);
       PARAMETER  — the ink points to a quantity or a datum, not a procedure;
       INTERNAL   — the pointer's target is inside the same runner;
       RUN_CITATION — "as the LORD commanded": the run citing its spec
                    (graded at the spec/run sittings);
       FALSE      — the token is a false positive (a homograph); the entry
                    says which.
       REVERSE    — the home runner already calls THIS one (verified); a
                    call back would cycle, so the edge is live the other way;
       VIA        — the type's procedure for this verse is reached through
                    another runner this one calls (the `via` field, verified).
     A missing disposition FAILS the gate. A CALL without a live import
     edge FAILS. A live import edge dispositioned as anything but CALL
     FAILS (the file must not understate what the code does).
     A LIVE IMPORT EDGE is read from three forms (edges_of): `alias.name(`
     on an imported cold_run module; THE REGISTRATION FORM — the module
     imported and then named as a string in a `('cold_run_x', 'fn')` tuple
     (the sequential run's DAEMON_ORDER, fetched through sys.modules); and
     THE DAEMON REFERENCE — `alias.law_x` placed in a world's laws list (the
     yovel fork's exile daemon; daemons alone are named law_*). O4, 2026-09-07.
     A bare import never used is not an edge; a constant read alone is not a call form.
  5. Coverage is printed first (a report of zero is worth only the coverage
     line above it), and an ADVISORY list of verses no cell in the runner
     cites (by address) — not gated, since address styles vary, but printed
     so a sub-span never again hides behind a check mark unseen.

  6. An edge may carry an ungated `carries:` field naming what crosses it
     (value / count / procedure / status / window / place / inventory /
     verdict) — the scroll's own distinction between a fetched number and
     a censused count, kept as documentation beside the verified kind
     (the two-thread consensus of 2026-09-06). The cell's provenance tag
     (I/M/A/D/P) remains where the honest fractions count it.
  7. The gate WRITES World/step9/DEPENDENCY_INDEX.md each run — the graph
     generated from the dispositions and the live scan, per runner: its
     span, the calls out, the callers in, every required edge with its
     disposition, every pointer. Documentation and the site's dependency
     view; never a runtime path.
  8. THE LINK REVIEW LAW (owner-ruled 2026-09-07; sitting LR1). The type
     census ENUMERATES shared-token candidates — which is what a person may
     do — and the tradition's rule is that a person does not derive a
     verbal analogy on his own (Pesachim 66a:12, Niddah 19b:12;
     logic/MIDDOT.md under I2). So every edge and pointer answers THE TWO
     QUESTIONS in a field, `link:`:
       reference    — the ink names an institution, the edge calls its
                      definition (licensed by ink alone);
       transfer     — a rule moves on a shared word or a topic: `taught_by:`
                      must name a teacher (a sugya "Tractate 12a:3", a
                      Mishnah/Tosefta/Sifra/Sifrei/Mekhilta/Rabbah/Tanchuma
                      passage, or a catalogued move M-nn WITH its exemplar);
       hypothesis   — an untaught transfer, kept and labeled, never counted
                      toward compiled (class H); needs a why;
       none         — only with FALSE (a homograph has no link), or with a
                      CALL from a runner whose declared span is EMPTY (the
                      sequential run's registration edges: no verse compiled,
                      no ink of its own, no rule crossing — O4, 2026-09-07);
       UNCLASSIFIED — asked, not yet answered: counted, printed by --links
                      (the LR2 worklist), never silent.
     A transfer without a teacher FAILS; an entry without `link:` FAILS
     ("we need to keep up with these"); `none` off a FALSE FAILS unless the
     runner is span-less.
  9. EVERY LIVE IMPORT EDGE HAS ITS OWN ENTRY (O4 THE EDGE FILING, 2026-09-07
     — the debt LR3 named). An edge the token census never required is still
     the code's: a live edge (r -> h) with no entry (r -> h) FAILS, whatever
     the census says, and a REVERSE entry on the callee's side (h -> r) files
     the callee's required edge, never the caller's call. Every CALL entry on
     file, required or not, must be live. The "live edges beyond the token
     census" line reports them all on file or fails naming each; `--emit`
     prints their stubs.

Run: python3 World/step9/dependency_census.py [--emit] [--debt] [--links] [--no-index]
  --emit prints yaml stubs for every undispositioned edge/pointer.
  --debt prints the OWED edges and pointers — the compile-debt worklist,
         generated, not hand-noted.
  --links prints the UNCLASSIFIED and hypothesis entries — the link
         review's worklist, generated.
Exit 1 on any failure.
"""
CARRIES = {'value', 'count', 'procedure', 'status', 'window', 'place', 'inventory', 'verdict'}
import re
LINKS = ('reference', 'transfer', 'hypothesis', 'none', 'UNCLASSIFIED')
_TAUGHT = re.compile(r'\b(Mishnah|Tosefta|Sifra|Sifrei|Mekhilta|Rabbah|Tanchuma|Onkelos|Talmud|Yerushalmi)\b|\b[A-Z][a-z]+ \d{1,3}[ab]:\d{1,3}\b')
_MOVE = re.compile(r'\bM-\d\d\b')

def taught_ok(s):
    """A teacher is a cited passage, or a catalogued move with its exemplar named — never a bare move number."""
    if not s or not str(s).strip(): return False
    s = str(s)
    if _TAUGHT.search(s): return True
    return bool(_MOVE.search(s) and re.search(r'exemplar', s, re.I) and re.search(r'\d+:\d+', s))
import sqlite3, re, unicodedata, glob, os, sys, json
from collections import defaultdict
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DB = os.path.join(ROOT, 'elijah_docket', 'tanakh.sqlite')
YAML = os.path.join(HERE, 'dependency_dispositions.yaml')
DEBT = os.path.join(HERE, 'COMPILE_DEBT.md')

def strip(s):
    s = unicodedata.normalize('NFD', s)
    return ''.join(c for c in s if not unicodedata.combining(c) and c not in '־׀׃׳״/')

# ---- the type vocabulary: token pattern -> home runner(s) -------------
TOK = [
 ('olah',        r'^ו?[הלכב]?ה?על(ה|ת|ות|תו|תם|תיכם|תך|תכם)$', {'offerings'}),
 ('bird_olah',   r'^ו?[הלכבמ]?ה?(תרים|תר|יונה)$', {'minchah'}),
 ('minchah',     r'^ו?[הלכב]?ה?מנח(ה|ת|תו|תם|ות|תיכם|תכם)$', {'minchah'}),
 ('shelamim',    r'שלמי', {'offerings'}),
 ('chatat',      r'^ו?[הלכב]?ה?חטא(ת|תו|תם|ות)$', {'chatat'}),
 ('asham',       r'^ו?[הלכב]?ה?אשמ(ו|ם|ות|ה)?$', {'vayikra5', 'tzav'}),
 ('pesach',      r'^ו?[הלכב]?ה?פסח$', {'pesach'}),
 ('matzah',      r'^המצות$', {'pesach'}),   # 'the feast of UNLEAVENED BREAD' (Exod 23:15, Lev 23:6); the bare form is a homograph of 'commandments'
 ('firstborn',   r'^ו?[הלכב]?ה?בכ(ו)?ר(ות|ה)?$', {'pesach'}),
 ('first_fruits', r'^ו?[הלכב]?ה?בכ(ו)?רי(ם)?$', {'moadim'}),
 ('tithe',       r'מעשר', {'temurah', 'yovel'}),
 ('valuation',   r'^ו?[הלכב]?ערכך', {'yovel'}),
 ('jubilee',     r'^ו?[הלכב]?ה?יבל$', {'yovel'}),
 ('seventh_year', r'^ו?[הלכב]?ה?שביע(ת|ית)$|^תשמטנה$|^שמט', {'calendar', 'yovel'}),
 ('installation', r'מלאים', {'tzav'}),
 ('tzaraat',     r'צרעת', {'negaim'}),
 ('zav',         r'^ו?[הלכב]?ה?זב(ה|ו|ים)?$', {'clocks'}),
 ('niddah',      r'^ו?[הלכב]?ה?נד(ה|ת|תה)$', {'clocks'}),
 ('interest',    r'נשך|תרבית|מרבית', {'yovel'}),
 ('hebrew_slave', r'^עברי$', {'mishpatim'}),
 ('molech_ov',   r'^ו?[הלכב]?ה?(אבות|ידעני|ידענים|מלך)$', {'sanctions'}),
 ('talion_formula', r'^תחת$', {'lev24'}),
 # ---- the sanctuary's cross-references into Exod 30 (added at sitting E2, 2026-09-06: the construction run of
 # Exod 36-38 builds the incense altar, the laver, and counts the half-shekel census — institutions whose SPEC is
 # Exod 30:1-38, the E4 span; their home runner is cold_run_incense_shekel.py, OWED until E4 compiles it) ----
 ('incense',      r'^ו?[הלכב]?ה?קטרת$', {'incense_shekel'}),
 ('laver',        r'^ו?[הלכב]?ה?כי(ו)?ר$', {'incense_shekel'}),
 ('shekel',       r'^ו?[הלכב]?ה?שקל(ים)?$', {'incense_shekel'}),
 ('anointing_oil', r'^ו?[הלכב]?ה?משח(ה|ת)$', {'incense_shekel'}),
 # ---- THE PRE-SINAI CODE (added at sitting G1, 2026-09-06 — the Genesis type tokens: institutions whose FIRST seat is Genesis
 # and whose runner, cold_run_pre_sinai.py, is a LEAF CALLER of every Sinai engine that names them — Sanhedrin 59a's own rule,
 # 'a command given to the sons of Noah and REPEATED at Sinai', is the edge). The bare 'מול' ('opposite', Exod 26:9, 28:25,
 # 34:3, Lev 8:9) is NOT in the circumcision pattern — a homograph of the imperative; the ל-prefixed 'לשבת' ('to dwell',
 # Lev 20:22) and the suffixed 'שבתו' ('his idleness', Exod 21:19) are NOT in the sabbath pattern; the poured blood's 'ישפך'
 # (the sin offering's base, Lev 4) shares its consonants with 'shall be shed' (Gen 9:6) and is dispositioned FALSE by name.
 ('sabbath',      r'^ו?[הבכמ]?ה?שבת(ון|ות|תי|תיכם|כם|ה)?$', {'pre_sinai'}),
 ('circumcision', r'^ו?(' + '|'.join([
        'המול', 'ימול', 'נמול', 'נמלו', 'וימל', 'ימל',                    # 'circumcise' — the verb's forms
        'מלתם', 'ומלתם', 'ומלתה', 'למול', 'מלה', 'נמלים', 'המלות',        # 'circumcise' — with suffixes and prefixes
        'ערל', 'ערלה', 'ערלת', 'ערלתו', 'ערלתם', 'ערלים', 'ערלכם',        # 'foreskin', 'uncircumcised'
        'הערל', 'וערל', 'וערלתם', 'לערל', 'ערלי',                         # 'foreskin' — with prefixes
    ]) + ')$', {'pre_sinai'}),
 ('life_blood',   r'^בנפשו$', {'sanctions', 'pre_sinai'}),   # 'its blood in its life' — Gen 9:4 and Lev 17:14 alone in the Tanakh: each the other's home
 ('shed',         r'^ו?(שפך|ישפך|שפכו|תשפך|שפכתי|ישפכו)$', {'pre_sinai'}),
 ('fruitful',     r'^ו?(פרו|רבו|הפריתי)$', {'pre_sinai'}),
 ('appointed_time', r'^ו?[לב]מועד(ים|ו|ה|ם|יו)?$', {'moadim'}),   # 'for seasons' (Gen 1:14), 'at this set time' (17:21), 'in its season' (Exod 13:10), 'at the appointed time' (23:15, 34:18)
 # ---- THE FAMILY CODE (added at sitting G2, 2026-09-06 — the Genesis institutions of the house: the field bought for a grave,
 # the wife taken, the sinew, the widow waiting for the levir, the pledge, the harlot, the birthright, the inheritance. The
 # runner cold_run_family.py is their HOME where Genesis is the first seat (the sinew has NO Sinai seat — Mishnah Chullin 7:6:
 # 'said at Sinai, written in its place' — the repetition test's one exception); the tenure of the field is the jubilee
 # engine's, the widow's two law seats are the ordinances' and the priesthood's (Yevamot 59a tries 'widow-widow from Tamar'
 # and refuses it), the harlot's definition the priesthood's, the half-shekel's name 'beka' the construction run's. Homographs
 # kept OUT of the patterns: 'הגיד' ('he told', Gen 3:11 etc.) is not the sinew; 'נחל' bare (the stream, 32:24) is not the
 # inheritance; the verb forms 'you shall inherit the land' (Exod 23:30, 32:13) match the noun pattern and are FALSE by name.
 ('sinew',        r'^ו?ב?גיד$|^הנשה$', {'family'}),   # no ה-prefix: 'והגיד' (Lev 14:35 'and he shall TELL the priest') is the verb, not the sinew
 ('levir',        r'^ו?(יבם|יבמה|ויבמה|יבמי|יבמתו|יבמתך|יבמך|יבמת|ליבם|יבמו|יבמים)$', {'family'}),
 ('wife_taken',   r'^לאשה$', {'family'}),   # 'to him as a WIFE' — the marriage formula's closing token (Gen 24:67, 38:14; Exod 22:15 the seduced virgin's)
 ('holding',      r'^ו?[הלכבמ]?ה?אחז(ה|ת|תו|תם|תכם|תך|תיכם)$', {'yovel'}),   # 'a HOLDING of a grave' (Gen 23:4, 9, 20; 49:30), 'an everlasting holding' (17:8, 48:4); Lev 25's tenure
 ('inheritance',  r'^ו?[הלכבמ]?ה?נחל(ה|ת|תו|תם|תך|תכם|תי|ות|תיכם)$|^ו?(נחלו|התנחלתם|ינחל|תנחל|ינחלו|תנחלו|הנחיל|להנחיל|ינחילנו|הנחילו|בהנחל|הנחלתי|ונחלתם|תתנחלו)$', {'family'}),
 ('birthright',   r'^ו?[הלכב]?ה?בכר(ה|תו|תי|תך|תם)$', {'family'}),   # the birthright NOUN (Gen 25:31-34, 27:36, 43:33; Deut 21:17 'the right of the firstborn') — distinct from the firstborn person
 ('harlot',       r'^ו?[הלכב]?ה?(זונה|זנה|קדשה)$', {'priesthood'}),   # 'he thought her a HARLOT' (38:15), 'the cult harlot' (38:21-22); Lev 21:7, 21:14 the priest's ban
 ('beka',         r'^ו?[הלכב]?ה?בקע$', {'sanctuary_build'}),   # 'a BEKA its weight' (Gen 24:22) = 'a beka a head' (Exod 38:26) — the half-shekel's name at two seats
 ('pledge',       r'^ו?[הלכב]?ה?(ערבון|חבל|תחבל|יחבל|חבלת|עבט|העבוט|עבטו|עבוט)$', {'ordinances'}),   # Tamar's 'PLEDGE' (38:17-20) and the ordinances' 'if you take in pledge' (Exod 22:25) — one institution, two words
 ('widow',        r'^ו?[הלכב]?ה?אלמנ(ה|ות|תו|תה|ותה|ותיך|תך)$', {'ordinances', 'priesthood'}),   # 'sit as a WIDOW' (38:11), 'her widow's garments' (38:14, 19); Exod 22:21-23 the affliction ban, Lev 21:14 and 22:13 the priest's
]
# ---- the explicit pointer forms --------------------------------------
PTR = [
 ('AS_PRESCRIBED', r'^כמשפט'),
 ('AS_LAW_OF', r'^כתורת|^כתורה'),
 ('AS_WHEN', r'^כאשר$'),
 ('LIKE_OFFERING', r'^כחטאת|^כאשם|^כמנחת|^כמנחה|^כשלמים|^כעלה|^כזבח|^כחלב'),
 ('ONE_LAW', r'^תורה$'),   # only with the next token 'אחת'
]

def load_yaml():
    if not os.path.exists(YAML):
        sys.exit('DEPENDENCY GATE: %s missing — every runner must declare its span and every edge its disposition' % YAML)
    d = yaml.safe_load(open(YAML, encoding='utf-8')) or {}
    edges, ptrs = d.get('edges', []) or [], d.get('pointers', []) or []
    for x in edges + ptrs:   # YAML reads a bare FALSE as the boolean; the disposition is the word
        if x.get('disposition') is False: x['disposition'] = 'FALSE'
    return d.get('spans', {}) or {}, edges, ptrs

def verses(db, spans):
    rows = db.execute("select v.book, v.chapter, v.verse, group_concat(w.he,' ') from verses v join words w on w.verse_id=v.id "
                      "where v.book in ('Gen','Exod','Lev','Num','Deut') group by v.id order by v.id").fetchall()
    out = []
    for book, ch, vs, text in rows:
        for r, sp in spans.items():
            for b, c, a, z in sp:
                if b == book and c == ch and a <= vs <= z:
                    out.append((r, book, ch, vs, [strip(w) for w in text.split(' ')]))
    return out

def edges_of(src):
    """The live import edges of one runner's source: an imported cold_run module used as `alias.name(`, or named as a
    string in a registration tuple `('cold_run_x', 'fn')` (the sequential run's form, O4); `from cold_run_x import`."""
    edges = set(); imported = {}
    for m in re.finditer(r'^\s*import (cold_run_\w+)(?: as (\w+))?', src, re.M):
        imported[m.group(1)] = m.group(2) or m.group(1)
    for m in re.finditer(r'^\s*import ((?:cold_run_\w+(?: as \w+)?, ?)+cold_run_\w+(?: as \w+)?)', src, re.M):
        for part in m.group(1).split(','):
            part = part.strip(); mm = re.match(r'(cold_run_\w+)(?: as (\w+))?', part)
            if mm: imported[mm.group(1)] = mm.group(2) or mm.group(1)
    for full, alias in imported.items():
        if re.search(r'\b' + re.escape(alias) + r'\.\w+\(', src): edges.add(full[9:])
        elif re.search(r"\(\s*'" + re.escape(full) + r"'\s*,\s*'\w+'\s*\)", src): edges.add(full[9:])   # the registration form
        elif re.search(r'\b' + re.escape(alias) + r'\.law_\w+\b', src): edges.add(full[9:])   # the daemon reference (alias.law_x in a laws list; daemons alone are named law_*)
    for m in re.finditer(r'^\s*from (cold_run_\w+) import', src, re.M): edges.add(m.group(1)[9:])
    return edges

def import_edges():
    E = {}
    for f in sorted(glob.glob(os.path.join(HERE, 'cold_run_*.py'))):
        E[os.path.basename(f)[9:-3]] = edges_of(open(f, encoding='utf-8').read())
    return E

def cited_verses(runner):
    src = open(os.path.join(HERE, 'cold_run_%s.py' % runner), encoding='utf-8').read()
    cited = set()
    for m in re.finditer(r'(?<![\d:])(\d{1,2}):(\d{1,2})(?:-(?:(\d{1,2}):)?(\d{1,2}))?', src):
        c, a = int(m.group(1)), int(m.group(2))
        c2 = int(m.group(3)) if m.group(3) else c
        z = int(m.group(4)) if m.group(4) else a
        if c2 == c:
            for v in range(a, min(z if z >= a else a, a + 60) + 1): cited.add((c, v))
        else:
            for v in range(a, a + 61): cited.add((c, v))
            for v in range(1, z + 1): cited.add((c2, v))
    return cited

def link_checks(head, x, disp, spanless=False):
    """Rule 8 on one edge or pointer: the two questions answered in the field, a transfer with its teacher.
    `spanless`: the entry's runner declares an empty span (the sequential run) — `none` is licensed on its CALLs (O4)."""
    out = []
    lk = x.get('link')
    if lk is None:
        out.append('%s: NO link — THE TWO QUESTIONS (reference / transfer / hypothesis / none; the link review law)' % head); return out
    if lk not in LINKS:
        out.append('%s: unknown link %r (not one of %s)' % (head, lk, LINKS)); return out
    if lk == 'transfer' and not taught_ok(x.get('taught_by')):
        out.append('%s: link transfer WITHOUT A TEACHER — taught_by must name a sugya, a Mishnah/Tosefta/Sifra/Sifrei/Mekhilta passage, '
                   'or a catalogued move M-nn with its exemplar (a person does not derive a verbal analogy on his own)' % head)
    if lk == 'hypothesis' and not x.get('why'):
        out.append('%s: link hypothesis without a why (what transfer, and why no teacher)' % head)
    if lk == 'none' and disp != 'FALSE' and not (disp == 'CALL' and spanless):
        out.append('%s: link none on a %s entry — none belongs to FALSE alone (or a span-less runner\'s registration CALL)' % (head, disp))
    if lk == 'reference' and not x.get('why'):
        out.append('%s: link reference without a why (which institution the ink names)' % head)
    return out

def main():
    emit = '--emit' in sys.argv
    spans, edges_y, ptrs_y = load_yaml()
    db = sqlite3.connect(DB)
    runners = sorted(os.path.basename(f)[9:-3] for f in glob.glob(os.path.join(HERE, 'cold_run_*.py')))
    fails = []
    undeclared = [r for r in runners if r not in spans]
    if undeclared: fails.append('UNDECLARED runners (no span in %s): %s' % (os.path.basename(YAML), undeclared))
    spans = {r: [tuple(x) for x in sp] for r, sp in spans.items() if r in runners}
    VV = verses(db, spans)
    E = import_edges()
    # ---- the type census: required edges ----
    need = defaultdict(lambda: defaultdict(list))
    for r, book, ch, vs, words in VV:
        for w in words:
            for name, pat, homes in TOK:
                if re.search(pat, w):
                    for h in homes:
                        if h != r and h in spans: need[r][h].append(('%s %d:%d' % (book, ch, vs), name, w))
    # ---- the pointer census ----
    ptrs = []
    for r, book, ch, vs, words in VV:
        for i, w in enumerate(words):
            for name, pat in PTR:
                if re.search(pat, w):
                    if name == 'ONE_LAW' and not (i + 1 < len(words) and words[i + 1].startswith('אחת')): continue
                    ptrs.append((r, '%s %d:%d' % (book, ch, vs), name, ' '.join(words[i:i + 3])))
    # ---- the dispositions ----
    ed = {(e['from'], e['to']): e for e in edges_y}
    # LR2 (2026-09-07): a pointer is keyed by verse, form AND runner — one clause compiled in two spans (Exod 21:22 in
    # mishpatim and mishpatim_2) files two dispositions, and the old (verse, form) key silently dropped one of the 72.
    pd = {(p['verse'], p['form'], p.get('runner')): p for p in ptrs_y}
    if len(pd) != len(ptrs_y): fails.append('POINTERS: %d on file but %d distinct (verse, form, runner) keys — a duplicate entry' % (len(ptrs_y), len(pd)))
    n_edges = sum(len(v) for v in need.values())
    print('DEPENDENCY GATE coverage: %d runners declared, %d verses scanned, %d type tokens, %d pointer forms; '
          'required edges %d, required pointers %d; live import edges %d; dispositions on file: %d edges, %d pointers'
          % (len(spans), len(VV), len(TOK), len(PTR), n_edges, len(ptrs), sum(len(v) for v in E.values()),
             len(ed), len(pd)))
    stubs = []
    for r in sorted(need):
        for h, lst in sorted(need[r].items()):
            vv = sorted(set(v for v, _, _ in lst)); toks = sorted(set(n for _, n, _ in lst))
            live = h in E.get(r, set())
            e = ed.get((r, h))
            if e is None:
                fails.append('EDGE %s -> %s [%s] at %s: NO DISPOSITION' % (r, h, ','.join(toks), ', '.join(vv[:6])))
                stubs.append({'from': r, 'to': h, 'tokens': toks, 'verses': vv, 'disposition': 'CALL' if live else 'OWED', 'why': ''})
                continue
            d = e.get('disposition')
            if d == 'CALL' and not live: fails.append('EDGE %s -> %s dispositioned CALL but no live import edge in cold_run_%s.py' % (r, h, r))
            if d != 'CALL' and live: fails.append('EDGE %s -> %s is a live import edge but dispositioned %s — the file understates the code' % (r, h, d))
            if d == 'OWED' and not (e.get('why') and e['why'].split('|')[0].strip() in open(DEBT, encoding='utf-8').read()):
                fails.append('EDGE %s -> %s OWED but its why does not name a COMPILE_DEBT.md line (the text before "|" must appear there)' % (r, h))
            if d == 'REVERSE' and r not in E.get(h, set()):
                fails.append('EDGE %s -> %s dispositioned REVERSE but cold_run_%s.py has no live import edge back to %s' % (r, h, h, r))
            if d == 'VIA' and e.get('via') not in E.get(r, set()):
                fails.append('EDGE %s -> %s dispositioned VIA %r but cold_run_%s.py has no live import edge to it' % (r, h, e.get('via'), r))
            if d in ('PARAMETER', 'FALSE', 'REVERSE', 'VIA') and not e.get('why'): fails.append('EDGE %s -> %s %s without a why' % (r, h, d))
            if d not in ('CALL', 'OWED', 'PARAMETER', 'FALSE', 'REVERSE', 'VIA'): fails.append('EDGE %s -> %s: unknown disposition %r' % (r, h, d))
            if e.get('carries') is not None and e['carries'] not in CARRIES:
                fails.append('EDGE %s -> %s: carries %r is not one of %s' % (r, h, e['carries'], sorted(CARRIES)))
            fails.extend(link_checks('EDGE %s -> %s' % (r, h), e, d))
    # ---- the link contract on EVERY entry on file (an edge the census no longer requires still answers), and every
    # CALL entry on file, required or not, must be LIVE (O4: the check had run on required edges only) ----
    for e in edges_y:
        key = (e.get('from'), e.get('to'))
        if key in ed and (key[0] in need and key[1] in need[key[0]]): continue
        fails.extend(link_checks('EDGE %s -> %s' % key, e, e.get('disposition'), spanless=(spans.get(key[0]) == [])))
        if e.get('disposition') == 'CALL' and key[1] not in E.get(key[0], set()):
            fails.append('EDGE %s -> %s dispositioned CALL but no live import edge in cold_run_%s.py' % (key[0], key[1], key[0]))
    # ---- rule 9 (O4, 2026-09-07): live edges never required by a token are still the code's — each has its own entry ----
    extra_live = [(r, h) for r, hs in E.items() for h in hs if r in spans and h not in need.get(r, {})]
    unfiled_live = sorted((r, h) for r, h in extra_live if (r, h) not in ed)
    for r, h in unfiled_live:
        fails.append('LIVE EDGE %s -> %s has NO ENTRY on file — the file understates the code: file it with its link (rule 9)' % (r, h))
        stubs.append({'from': r, 'to': h, 'disposition': 'CALL', 'link': 'UNCLASSIFIED', 'why': ''})
    for (r, verse, form, ctx) in ptrs:
        p = pd.get((verse, form, r))
        if p is None:
            fails.append('POINTER %s %s in %s ("%s"): NO DISPOSITION' % (verse, form, r, ctx))
            stubs.append({'verse': verse, 'form': form, 'runner': r, 'text': ctx, 'disposition': '', 'target': '', 'why': ''})
            continue
        d = p.get('disposition')
        if d == 'CALL':
            t = p.get('target')
            if t not in E.get(r, set()): fails.append('POINTER %s %s: CALL to %r but cold_run_%s.py has no live import edge to it' % (verse, form, t, r))
        elif d == 'OWED':
            if not (p.get('why') and p['why'].split('|')[0].strip() in open(DEBT, encoding='utf-8').read()):
                fails.append('POINTER %s %s OWED but its why does not name a COMPILE_DEBT.md line' % (verse, form))
        elif d not in ('INTERNAL', 'RUN_CITATION', 'PARAMETER', 'FALSE'):
            fails.append('POINTER %s %s: unknown disposition %r' % (verse, form, d))
        elif not p.get('why'): fails.append('POINTER %s %s: %s without a why' % (verse, form, d))
        fails.extend(link_checks('POINTER %s %s' % (verse, form), p, d))
    for p in ptrs_y:
        if (p.get('verse'), p.get('form'), p.get('runner')) not in set((v, f, r) for r, v, f, _ in ptrs):
            fails.extend(link_checks('POINTER %s %s' % (p.get('verse'), p.get('form')), p, p.get('disposition')))
    # ---- the link census (rule 8): printed every run, never silent ----
    from collections import Counter
    lc = Counter();
    for x in edges_y + ptrs_y: lc[x.get('link', 'MISSING')] += 1
    print('LINK CENSUS (the link review law): ' + ', '.join('%s %d' % (k, lc[k]) for k in LINKS + ('MISSING',) if lc[k])
          + ' — of %d edges + %d pointers' % (len(edges_y), len(ptrs_y)))
    # ---- advisory: verses no cell cites, by address ----
    print('ADVISORY (not gated) — verses of each declared span no address in the runner cites:')
    for r in sorted(spans):
        cited = cited_verses(r); unc = []
        for b, c, a, z in spans[r]:
            zz = db.execute('select max(verse) from verses where book=? and chapter=?', (b, c)).fetchone()[0]
            for v in range(a, min(z, zz) + 1):
                if (c, v) not in cited: unc.append((c, v))
        runs = []
        for c, v in unc:
            if runs and runs[-1][0] == c and runs[-1][2] == v - 1: runs[-1][2] = v
            else: runs.append([c, v, v])
        print('  %-12s %3d uncited: %s' % (r, len(unc), ', '.join('%d:%d' % (c, a) if a == z else '%d:%d-%d' % (c, a, z) for c, a, z in runs)[:160]))
    if extra_live:
        print('live edges beyond the token census (calls the census did not require): %d — %s' % (
            len(extra_live), ('ALL ON FILE (rule 9)' if not unfiled_live else 'UNFILED %d: %s' % (len(unfiled_live), unfiled_live))))
    if emit and stubs:
        print('\n# ---- yaml stubs for the undispositioned ----')
        print(yaml.safe_dump(stubs, allow_unicode=True, sort_keys=False))
    # ---- the OWED worklist (--debt) ----
    owed_e = [e for e in edges_y if e.get('disposition') == 'OWED']
    owed_p = [p for p in ptrs_y if p.get('disposition') == 'OWED']
    if '--debt' in sys.argv:
        print('\nOWED WORKLIST (generated from the dispositions): %d edges, %d pointers' % (len(owed_e), len(owed_p)))
        for e in owed_e: print('  EDGE %s -> %s — %s' % (e['from'], e['to'], e.get('why', '')))
        for p in owed_p: print('  POINTER %s %s in %s — %s' % (p['verse'], p['form'], p.get('runner', ''), p.get('why', '')))
        if not owed_e and not owed_p: print('  (none — every required edge and pointer is live, reversed, routed, or a datum)')
    # ---- the link worklist (--links): the UNCLASSIFIED and the hypotheses, generated ----
    if '--links' in sys.argv:
        for label in ('UNCLASSIFIED', 'hypothesis'):
            xs = [x for x in edges_y + ptrs_y if x.get('link') == label]
            print('\nLINK WORKLIST — %s: %d entries' % (label, len(xs)))
            for x in xs:
                head = ('EDGE %s -> %s' % (x['from'], x['to'])) if 'from' in x else ('POINTER %s %s in %s' % (x['verse'], x['form'], x.get('runner', '')))
                print('  %s [%s] — %s' % (head, x.get('disposition'), (x.get('why') or '')[:140]))
    # ---- the generated index (documentation; never a runtime path) ----
    if '--no-index' not in sys.argv:
        L = ['# THE DEPENDENCY INDEX — GENERATED by dependency_census.py from dependency_dispositions.yaml and the',
             '# live import scan of World/step9/cold_run_*.py. Do not edit: rerun the gate. Documentation and the',
             '# site\'s dependency view; never a runtime path (the two-thread consensus of 2026-09-06).',
             '#',
             '# coverage: %d runners, %d verses, %d type tokens, %d pointer forms; required edges %d, pointers %d; live import edges %d'
             % (len(spans), len(VV), len(TOK), len(PTR), n_edges, len(ptrs), sum(len(v) for v in E.values())), '']
        callers = defaultdict(set)
        for r, hs in E.items():
            for h in hs: callers[h].add(r)
        for r in sorted(spans):
            sp = '; '.join('%s %d:%d-%d' % (b, c, a, z) for b, c, a, z in spans[r])
            L.append('## cold_run_%s.py — %s' % (r, sp))
            L.append('- calls out (live): %s' % (', '.join(sorted(E.get(r, ()))) or 'none'))
            L.append('- called by (live): %s' % (', '.join(sorted(callers.get(r, ()))) or 'none'))
            req = sorted(need.get(r, {}).items())
            if req:
                L.append('- required edges from the ink:')
                for h, lst in req:
                    e = ed.get((r, h), {}); vv = sorted(set(v for v, _, _ in lst)); toks = sorted(set(n for _, n, _ in lst))
                    L.append('  - -> %s [%s] at %s: %s%s%s%s — %s' % (
                        h, ','.join(toks), ', '.join(vv[:8]) + (' ...' if len(vv) > 8 else ''), e.get('disposition', '?'),
                        (' via ' + e['via']) if e.get('via') else '', (' carries ' + e['carries']) if e.get('carries') else '',
                        ' link ' + str(e.get('link', '?')) + ((' taught by ' + str(e['taught_by'])) if e.get('taught_by') else ''),
                        e.get('why', '')))
            pp = [p for p in ptrs if p[0] == r]
            if pp:
                L.append('- pointers in the ink:')
                for (_, verse, form, ctx) in pp:
                    p = pd.get((verse, form, r), {})
                    L.append('  - %s %s "%s": %s%s%s — %s' % (verse, form, ctx, p.get('disposition', '?'),
                             (' -> ' + p['target']) if p.get('target') else '',
                             ' link ' + str(p.get('link', '?')) + ((' taught by ' + str(p['taught_by'])) if p.get('taught_by') else ''),
                             p.get('why', '')))
            L.append('')
        with open(os.path.join(HERE, 'DEPENDENCY_INDEX.md'), 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(L) + '\n')
        print('index: World/step9/DEPENDENCY_INDEX.md regenerated (%d runners)' % len(spans))
    if fails:
        print('\nDEPENDENCY GATE: %d failure(s)' % len(fails))
        for f in fails: print('  FAIL', f)
        sys.exit(1)
    print('DEPENDENCY GATE: every required edge and pointer dispositioned; every CALL live; every OWED on the debt list [gate satisfied]')

if __name__ == '__main__':
    main()
