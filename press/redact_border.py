#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
"""redact_border.py — the crossing convention, made mechanical.

Work derived in the workshop crosses into canon by copy. One documented
redaction is applied at copy time (logic/README.md, "The border
redaction"): the workshop's name and its private filenames become the
names THIS repository actually uses. That redaction was hand-applied
for years of crossings and it slipped twice — the pinned snapshot
filename rode into seven unit files across two landings before a sweep
caught it. Hand discipline is not a mechanism; this is.

Run it as the step AFTER copying and BEFORE rendering, every landing:

    python3 press/redact_border.py            # report only
    python3 press/redact_border.py --apply    # rewrite in place

It touches the canonical layer only (logic/), never the received
records under scans/, and never anything outside this repository. It
rewrites nothing but the mapped names: operator text, citations,
confidence grades, and Hebrew are left byte-for-byte as frozen.

NOTE ON THE CHANGELOG GATE: rewriting a unit YAML that is not otherwise
being landed makes it a diff against HEAD, which the changelog gate
answers for — such a unit needs a changelog line saying the redaction
was applied. Do NOT bump its rev to satisfy anything: rev 3 signals a
derivation pass, and a redaction is not a derivation.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCAN = os.path.join(ROOT, "logic")

# The mapping of logic/README.md's border table, as patterns. Each entry
# is (compiled pattern, replacement, what it is). Add a row when a new
# private name is met at the border — and say so in the README table.
RULES = [
    (re.compile(r"torah_grok\.SNAPSHOT-\s*\n?\s*main-[0-9a-f]+\.sqlite"),
     "source-snapshot.sqlite", "the pinned gloss snapshot"),
    (re.compile(r"torah_grok\.sqlite"),
     "derivation.sqlite", "the live derivation database"),
]
# A last net: any surviving mention of the workshop by name is reported,
# never rewritten blindly — an unmapped case needs a human decision and
# a new row in the table above.
RESIDUE = re.compile(r"[Tt]orah_?[Gg]rok")

SKIP_DIRS = {"__pycache__"}
EXTS = (".yaml", ".yml", ".md", ".py")


def self_test():
    """A zero looks the same whether the scan covered everything or
    nothing. Before reporting one, prove the patterns fire and prove the
    walk reaches the canonical units — the weakness that let the leak
    through was a check that could not show its own coverage."""
    probe = ("regenerated from torah_grok.sqlite tree_json; "
             "verified against torah_grok.SNAPSHOT-main-51801ca.sqlite")
    out = probe
    for pat, repl, _what in RULES:
        out = pat.sub(repl, out)
    if "torah_grok" in out:
        raise SystemExit("redact_border: SELF-TEST FAILED — the rules no "
                         "longer match the known border names; fix RULES "
                         "before trusting any report from this tool.")
    return True


def main():
    apply = "--apply" in sys.argv[1:]
    self_test()
    changed, residue, total = [], [], 0
    scanned, units_seen = 0, 0
    for base, dirs, files in os.walk(SCAN):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for f in sorted(files):
            if not f.endswith(EXTS):
                continue
            path = os.path.join(base, f)
            rel = os.path.relpath(path, ROOT)
            scanned += 1
            if rel.startswith(os.path.join("logic", "units")):
                units_seen += 1
            text = open(path, encoding="utf-8").read()
            out, hits = text, 0
            for pat, repl, _what in RULES:
                out, n = pat.subn(repl, out)
                hits += n
            if hits:
                total += hits
                changed.append((rel, hits))
                if apply:
                    with open(path, "w", encoding="utf-8") as fh:
                        fh.write(out)
            for m in RESIDUE.finditer(out):
                residue.append((rel, out[max(0, m.start() - 40):
                                          m.end() + 40].replace("\n", " ")))

    for rel, n in changed:
        print("  %-58s %d occurrence(s)" % (rel, n))
    # Coverage is printed WITH the result, always: the canonical units
    # are the surface the leak crossed on, so a report that does not say
    # how many of them it read is not a report.
    print("scanned %d file(s) under logic/, of which %d unit YAML(s); "
          "pattern self-test passed" % (scanned, units_seen))
    print("border redaction: %d occurrence(s) in %d file(s)%s"
          % (total, len(changed), " — REWRITTEN" if apply
             else " — report only, pass --apply to rewrite"))
    if residue:
        print("UNMAPPED mentions of the workshop by name — decide each, "
              "then add a row to the table in logic/README.md:")
        for rel, ctx in residue[:20]:
            print("   %s: …%s…" % (rel, ctx))
    return 1 if (residue or (changed and not apply)) else 0


if __name__ == "__main__":
    sys.exit(main())
