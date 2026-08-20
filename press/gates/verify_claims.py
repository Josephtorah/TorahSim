#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_claims.py — Oral-first claims-manifest verifier (process rewrite
2026-08-08, owner order: crowns = chain-attested + DB-verified; no
self-directed crown search).

Usage:  python3 logic/solo_tools/verify_claims.py <manifest.json>

Manifest: JSON list of claim objects:
  {"id": "G08-01", "source": "Bereshit Rabbah 12:6", "ref": "Gen 2:4",
   "claim_en": "...", "scope": "torah|scripture", "check": {...}}

The tradition often counts Scripture-wide; our DB is Torah-only. A
scripture-scope claim VERIFIES when the Torah-side facts are consistent
with it (expected Torah refs all present, no extras); the report labels
it "torah-side". check.type == "manual" -> UNCHECKABLE (instrument gap
or non-DB claim); the row must carry check.note saying why.

Exit code: 0 if no FAILED rows, 2 otherwise. Reviewers re-run this
script; a FAILED row is a review BLOCKER unless the unit files it as a
discrepancy observation.
"""
import json, re, sqlite3, sys

DB = "data/source-snapshot.sqlite"
DM = "data/debut-snapshot.sqlite"
FINALS = {"ך": "כ", "ם": "מ", "ן": "נ", "ף": "פ", "ץ": "צ"}


def norm(s):
    return "".join(FINALS.get(ch, ch) for ch in s.replace("/", ""))


def parse_ref(ref):
    m = re.match(r"(\w+) (\d+):(\d+)$", ref)
    return m.group(1), int(m.group(2)), int(m.group(3))


class V:
    def __init__(self):
        self.db = sqlite3.connect(DB)
        self.dm = sqlite3.connect(DM)

    def q(self, sql, args=()):
        return self.db.execute(sql, args).fetchall()

    def tokens(self, where):
        """where: translit / translit_like / he_plain_joined (slash-stripped
        he_plain equality) / lemma / lemma_like / strong, optional morph_like. Returns (book, ch, vs, idx, translit, he_plain)."""
        conds, args = [], []
        if "translit" in where:
            conds.append("w.translit = ?"); args.append(where["translit"])
        if "translit_like" in where:
            conds.append("w.translit LIKE ?"); args.append(where["translit_like"])
        if "he_plain_joined" in where:
            conds.append("REPLACE(w.he_plain,'/','') = ?")
            args.append(where["he_plain_joined"])
        if "lemma" in where:
            conds.append("w.lemma = ?"); args.append(where["lemma"])
        if "lemma_like" in where:
            conds.append("w.lemma LIKE ?"); args.append(where["lemma_like"])
        if "morph_like" in where:
            conds.append("w.morph LIKE ?"); args.append(where["morph_like"])
        sql = ("SELECT v.book, v.chapter, v.verse, w.idx, w.translit, "
               "w.he_plain FROM words w JOIN verses v ON w.verse_id = v.id "
               "WHERE " + " AND ".join(conds) +
               " ORDER BY v.book, v.chapter, v.verse, w.idx")
        return self.q(sql, args)

    def verse_tokens(self, ref):
        b, c, vs = parse_ref(ref)
        return self.q("SELECT w.idx, w.translit, w.he_plain, w.he, w.mark_id "
                      "FROM words w JOIN verses v ON w.verse_id = v.id "
                      "WHERE v.book=? AND v.chapter=? AND v.verse=? "
                      "ORDER BY w.idx", (b, c, vs))

    # ---- check types -------------------------------------------------
    def token_count(self, c):
        rows = self.tokens(c["where"])
        if c.get("verse_initial"):
            rows = [r for r in rows if r[3] == 0]
        refs = ["%s %d:%d" % r[:3] for r in rows]
        ok = True
        if "expect_total" in c:
            ok &= len(rows) == c["expect_total"]
        if "expect_refs" in c:
            ok &= sorted(set(refs)) == sorted(set(c["expect_refs"]))
        return ok, "count=%d refs=%s" % (len(rows), sorted(set(refs))[:12])

    def adjacency(self, c):
        rows = self.tokens(c["first"])
        second = c["second"] if isinstance(c["second"], list) else [c["second"]]
        hits = []
        for b, ch, vs, i, t, h in rows:
            nxt = self.q("SELECT w.translit FROM words w JOIN verses v ON "
                         "w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND "
                         "v.verse=? AND w.idx=?", (b, ch, vs, i + 1))
            if nxt and nxt[0][0] in second:
                hits.append("%s %d:%d" % (b, ch, vs))
        ok = sorted(set(hits)) == sorted(set(c["expect_refs"]))
        return ok, "pairs=%s" % sorted(set(hits))

    def career(self, c):
        rows = self.dm.execute("SELECT ordinal, total, word_id FROM "
                               "token_ordinals WHERE strong=? ORDER BY ordinal",
                               (str(c["strong"]),)).fetchall()
        tot = rows[0][1] if rows else 0
        ok = tot == c["expect_total"]
        det = "total=%d" % tot
        if "expect_all_in" in c and rows:
            b0, c0 = c["expect_all_in"].split()
            allin = True
            for o, t, wid in rows:
                r = self.q("SELECT v.book, v.chapter FROM words w JOIN verses "
                           "v ON w.verse_id=v.id WHERE w.id=?", (wid,))
                if not r or r[0][0] != b0 or r[0][1] != int(c0):
                    allin = False
            ok &= allin
            det += " all_in_%s=%s" % (c["expect_all_in"].replace(" ", "_"), allin)
        return ok, det

    def spelling_variants(self, c):
        rows = self.tokens(c["where"])
        full = ["%s %d:%d" % r[:3] for r in rows if c["pattern_full"] in r[5]]
        ok = sorted(set(full)) == sorted(set(c["expect_full_refs"]))
        return ok, "full=%s of %d tokens" % (sorted(set(full)), len(rows))

    def final_letters(self, c):
        toks = self.verse_tokens(c["ref"])
        lo, hi = c["idx"]
        got = "".join(norm(h)[-1] for i, t, h, he, mk in toks if lo <= i <= hi)
        ok = got == norm(c["spell"])
        return ok, "finals=%s" % got

    def initial_letters(self, c):
        toks = self.verse_tokens(c["ref"])
        lo, hi = c["idx"]
        got = sorted(norm(h)[0] for i, t, h, he, mk in toks if lo <= i <= hi)
        ok = got == sorted(norm(c["multiset_of"]))
        return ok, "initials=%s" % "".join(got)

    def letters_multiset(self, c):
        toks = self.verse_tokens(c["ref"])
        tok = [h for i, t, h, he, mk in toks if i == c["idx"]][0]
        ok = sorted(norm(tok)) == sorted(norm(c["equals_letters_of"]))
        return ok, "letters=%s vs %s" % (norm(tok), norm(c["equals_letters_of"]))

    def mark(self, c):
        toks = self.verse_tokens(c["ref"])
        got = [mk for i, t, h, he, mk in toks if i == c["idx"]]
        ok = bool(got) and got[0] == c["expect_mark"]
        return ok, "mark=%s" % (got[0] if got else None)

    def verse_word_count(self, c):
        toks = self.verse_tokens(c["ref"])
        ok = len(toks) == c["expect_total"]
        return ok, "words=%d" % len(toks)

    def verse_token_count(self, c):
        toks = self.verse_tokens(c["ref"])
        n = sum(1 for i, t, h, he, mk in toks if t == c["translit"])
        ok = n == c["expect_total"]
        return ok, "in-verse count=%d" % n

    def maqqef_after(self, c):
        b, ch, vs = parse_ref(c["ref"])
        got = self.q("SELECT w.maqqef_after FROM words w JOIN verses v ON "
                     "w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND "
                     "v.verse=? AND w.idx=?", (b, ch, vs, c["idx"]))
        ok = bool(got) and got[0][0] == c["expect"]
        return ok, "maqqef_after=%s" % (got[0][0] if got else None)

    def he_contains(self, c):
        toks = self.verse_tokens(c["ref"])
        got = [he for i, t, h, he, mk in toks if i == c["idx"]]
        ok = bool(got) and c["contains"] in got[0]
        return ok, "he=%s" % (got[0][-4:] if got else None)


def main(path):
    claims = json.load(open(path, encoding="utf-8"))
    v = V()
    counts = {"VERIFIED": 0, "FAILED": 0, "UNCHECKABLE": 0}
    for cl in claims:
        ck = cl["check"]
        if ck["type"] == "manual":
            st, det = "UNCHECKABLE", ck.get("note", "no note")
        else:
            ok, det = getattr(v, ck["type"])(ck)
            st = "VERIFIED" if ok else "FAILED"
        scope = " (torah-side)" if cl.get("scope") == "scripture" and st == "VERIFIED" else ""
        counts[st] += 1
        print("%-11s %s [%s] %s%s\n            %s" %
              (st, cl["id"], cl["source"], cl["claim_en"], scope, det))
    print("\nSUMMARY: %(VERIFIED)d verified, %(FAILED)d failed, "
          "%(UNCHECKABLE)d uncheckable" % counts)
    sys.exit(2 if counts["FAILED"] else 0)


if __name__ == "__main__":
    main(sys.argv[1])
