#!/usr/bin/env python3
"""
build_torahcode_data.py — home-side generator for the PUBLIC TorahCode repo's
data/ tree. Runs in Torah_Grok (needs the private snapshot DB); writes only
public artifacts:

  TorahCode/data/lexicon.json      Strong's-number -> English gloss (the lemma
                                   bridge), + unpointed-spelling fallback, +
                                   the hand supplement — exactly the three
                                   layers the tanakh_run app derives at boot.
  TorahCode/data/units_index.json  the 97 frozen derivation units (id, book,
                                   verse span, title) — what dependency
                                   proofs resolve against.
  TorahCode/data/tanakh.sqlite     copied from elijah_docket/ (WLC text +
                                   OSHB lemma/morph tags — see ATTRIBUTION.md
                                   in TorahCode).

The 147 MB private snapshot never leaves home; this exports the ~1 MB the
public app actually needs. Rerun after gloss-override changes to refresh.
"""
import json
import shutil
import sqlite3
from pathlib import Path

HOME = Path("<repo-old>")
PUB = Path("<home>/TorahCode")
SNAPSHOT = HOME / "torah_grok.SNAPSHOT-main-51801ca.sqlite"
MAIN_DB = HOME / "torah_grok.sqlite"
TANAKH = HOME / "elijah_docket" / "tanakh.sqlite"

# same four hand entries as the app's SUPPLEMENT dict (keyed by unpointed
# spelling; wins over the lemma gloss)
SUPPLEMENT = {
    "ארבעתים": "fourfold",
    "ישלם": "he-shall-repay",
    "וישלם": "and-he-shall-repay",
    "שבעתים": "sevenfold",
}


def build_lexicon():
    # queries identical to the app's _build_lexicon(): ORDER BY n makes the
    # most frequent gloss for a key win (later assignment overwrites).
    lex, skel = {}, {}
    db = sqlite3.connect(SNAPSHOT)
    for lemma, gloss, _n in db.execute(
            "SELECT lemma, gloss, count(*) n FROM words "
            "WHERE gloss IS NOT NULL AND gloss != '' "
            "GROUP BY lemma, gloss ORDER BY n"):
        base = (lemma or "").split("/")[-1].split(" ")[0]
        if base.isdigit():
            lex[base] = gloss.split("/")[-1]
    for plain, gloss, _n in db.execute(
            "SELECT replace(he_plain,'/',''), gloss, count(*) n FROM words "
            "WHERE gloss IS NOT NULL AND gloss != '' "
            "GROUP BY 1, gloss ORDER BY n"):
        skel[plain] = gloss
    db.close()
    return lex, skel


def build_units_index():
    db = sqlite3.connect(MAIN_DB)
    units = [
        {"unit_id": uid, "book": book, "refs": refs, "title": title,
         "genre": genre}
        for uid, book, refs, title, genre in db.execute(
            "SELECT unit_id, book_en, refs, title_en, genre FROM units "
            "WHERE status='frozen' ORDER BY id")
    ]
    db.close()
    return units


def main():
    (PUB / "data").mkdir(parents=True, exist_ok=True)

    lex, skel = build_lexicon()
    lexicon = {
        "_note": ("Word-by-word English gloss layers for the interlinear "
                  "display. 'lexicon' maps Strong's numbers to glosses; "
                  "'skeleton' maps unpointed Hebrew spellings to glosses "
                  "(fallback); 'supplement' is hand-written and wins over "
                  "both. Derived from Strong's Concordance (1890, public "
                  "domain) plus project hand glosses (CC BY 4.0). A reading "
                  "aid, not a translation."),
        "lexicon": lex, "skeleton": skel, "supplement": SUPPLEMENT,
    }
    out = PUB / "data" / "lexicon.json"
    out.write_text(json.dumps(lexicon, ensure_ascii=False, indent=0,
                              sort_keys=True), encoding="utf-8")
    print("lexicon.json: %d Strong's entries, %d skeleton entries, %d KB"
          % (len(lex), len(skel), out.stat().st_size // 1024))

    units = build_units_index()
    index = {
        "_note": ("The derived units of this project: each is a contiguous "
                  "verse span whose content was derived under the method "
                  "laws and frozen. Dependency proofs resolve backward "
                  "edges against these spans. Full derivations in units/."),
        "count": len(units), "units": units,
    }
    out = PUB / "data" / "units_index.json"
    out.write_text(json.dumps(index, ensure_ascii=False, indent=1),
                   encoding="utf-8")
    print("units_index.json: %d units" % len(units))

    shutil.copyfile(TANAKH, PUB / "data" / "tanakh.sqlite")
    print("tanakh.sqlite copied: %d MB"
          % ((PUB / "data" / "tanakh.sqlite").stat().st_size // 2**20))


if __name__ == "__main__":
    main()
