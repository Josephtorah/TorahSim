#!/usr/bin/env python3
# LESSON ONE — the Second Passover: the verse becomes code.
# THE LAW OF THIS FILE (owner-ruled 2026-09-03): the CODE below is
# built from the ink of Numbers 9 alone. The Mishnah appears ONLY in
# the DATA section at the bottom — test cases and parameter settings
# fed in at run time. Nothing from the Mishnah is inside the code.

# ---------------------------------------------------------------
# THE CODE — every line cites the verse word that licenses it
# ---------------------------------------------------------------

def passover(person, data):
    """Numbers 9:2-14 as a machine.
    `person` — the input case.  `data` — the values the ink does not
    state (here: which location counts as 'distant')."""

    # Numbers 9:14 — "one statute shall there be for you, and for the
    # stranger, and for the native of the land": the stranger is not a
    # branch; the same function runs for him.  (No code needed — the
    # absence of a branch IS the implementation.)

    # Numbers 9:10 — "any man WHEN he is impure for a corpse
    # [tamei la-nefesh] OR on a distant journey [ba-derekh rechokah]"
    deferred_class = person["impure_by_corpse"] or \
        is_distant(person["location"], data)

    if person["performed_first"]:
        # Numbers 9:2-3 — "the children of Israel shall perform the
        # Passover at its appointed time... on the fourteenth day of
        # this month at twilight... according to all its statutes"
        return "FULFILLED at the first Passover (month 1, day 14)"

    if deferred_class:
        # Numbers 9:11 — "in the SECOND month on the fourteenth day
        # at twilight they shall perform it; with unleavened bread
        # and bitter herbs they shall eat it"
        # Numbers 9:12 — "they shall leave none of it until morning,
        # nor break a bone of it: according to every statute of the
        # Passover they shall perform it"
        return ("DEFERRED to the second Passover (month 2, day 14, "
                "twilight; same statutes) — and EXEMPT from being cut "
                "off for the first")
        # the exemption rides the verse NAMING this class for
        # deferral rather than condemnation — see the Mishnah's own
        # question about why only these two are named (data file).

    if person["refused"]:
        # Numbers 9:13 — "the man who is PURE, and was NOT on a
        # journey, and REFRAINS [ve-chadal] from performing the
        # Passover — that soul shall be CUT OFF from its people"
        return "CUT OFF (karet) — pure, present, and refraining"

    # The remaining case: missed the first, but neither in the named
    # deferral class nor a refuser (the ink's karet clause requires
    # REFRAINING — chadal, a chosen desisting). The second Passover
    # stands open to him; refusing THAT would make him a refuser.
    return ("DEFERRED to the second Passover — and LIABLE to be cut "
            "off if he refrains from the second as well")


def is_distant(location, data):
    # Numbers 9:10 — the ink gives the PREDICATE ("on a distant
    # journey") but no number and no landmark. The threshold is DATA.
    scale = data["distance_scale"]          # ordered, near -> far
    return scale.index(location) > scale.index(data["distant_threshold"])


# ---------------------------------------------------------------
# THE DATA — from the Mishnah, fed at run time, never in the code
# ---------------------------------------------------------------

# Mishnah Pesachim 9:2 — the parameter's TWO recorded settings:
# "What is a distant journey? From Modiim and beyond — Rabbi Akiva.
#  Rabbi Eliezer says: from the threshold of the Temple courtyard
#  and beyond."  (A dispute = two data configurations. Both run.)
SCALE = ["courtyard", "jerusalem", "modiim", "beyond_modiim"]
SETTINGS = {
    "Rabbi Akiva":    {"distance_scale": SCALE, "distant_threshold": "modiim"},
    "Rabbi Eliezer":  {"distance_scale": SCALE, "distant_threshold": "courtyard"},
}

# Mishnah Pesachim 9:1 — the test cases and expected outputs:
# "One who was impure or on a distant journey and did not observe the
#  first — observes the second. One who forgot or was prevented and
#  did not observe the first — observes the second. If so, why does
#  the verse name the impure and the distant? That THESE are exempt
#  from karet, and THOSE are liable to karet [if they skip the
#  second]."
CASES = [
    ("the impure man (in Jerusalem)",
     {"impure_by_corpse": True, "location": "jerusalem",
      "performed_first": False, "refused": False},
     "DEFERRED", "EXEMPT"),
    ("the far traveler (beyond Modiim)",
     {"impure_by_corpse": False, "location": "beyond_modiim",
      "performed_first": False, "refused": False},
     "DEFERRED", "EXEMPT"),
    # REFINEMENT after the first run: these two must stand INSIDE the
    # courtyard, or the case is ambiguous between the two settings —
    # under Rabbi Eliezer, a man merely in Jerusalem is already in the
    # distant class. The machine caught the underspecified data; the
    # fix is in the DATA, never the code.
    ("the man who simply refused (pure, at the courtyard)",
     {"impure_by_corpse": False, "location": "courtyard",
      "performed_first": False, "refused": True},
     "CUT OFF", None),
    ("the man who forgot (pure, at the courtyard)",
     {"impure_by_corpse": False, "location": "courtyard",
      "performed_first": False, "refused": False},
     "DEFERRED", "LIABLE"),
    ("anyone who performed the first",
     {"impure_by_corpse": False, "location": "jerusalem",
      "performed_first": True, "refused": False},
     "FULFILLED", None),
]

# ---------------------------------------------------------------
# THE TEST — feed the data in; require the Mishnah's output
# ---------------------------------------------------------------
if __name__ == "__main__":
    for setting_name, data in SETTINGS.items():
        print("== running under the %s setting (threshold: %s) ==" %
              (setting_name, data["distant_threshold"]))
        ok = 0
        for label, person, want, karet in CASES:
            out = passover(person, data)
            match = want in out and (karet is None or karet in out)
            ok += match
            print("  %-46s -> %s   [%s]" %
                  (label, out.split(" — ")[0], "ok" if match else "MISMATCH"))
        print("  %d/%d cases match the Mishnah's verdicts\n" % (ok, len(CASES)))

    # The dispute made visible: one case that CLASSIFIES DIFFERENTLY
    # under the two recorded settings — a pure man standing in
    # Jerusalem (inside Modiim, outside the courtyard) who missed the
    # first Passover without refusing:
    probe = {"impure_by_corpse": False, "location": "jerusalem",
             "performed_first": False, "refused": False}
    print("== the dispute as two runtime settings ==")
    for setting_name, data in SETTINGS.items():
        cls = "IN the deferred class" if is_distant(probe["location"], data) \
              else "NOT in the deferred class"
        print("  under %-14s the man in Jerusalem is %s" % (setting_name, cls))
    print("  (same code, same case — the recorded dispute is two DATA settings)")
