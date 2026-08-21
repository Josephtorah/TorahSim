#!/usr/bin/env python3
"""day_one_v2_DRAFT.py — Genesis 1:1-5 re-derived UNDER THE READINGS.

DRAFT for the 2026-08-20 comparison exercise (owner order): the full-rule
method applied to day one — the 2026-07-30 triage ledger's read sources
drive the logic; every operator line cites claim ids from
claims_manifest.json. No freeze, no stamp, no canon edit.

Registers (v1's machine kept): TIME / WORLD / REGISTRY / SPECS / TESTS /
LEDGER — plus UTTERANCES (new, per C1/C2) and WITNESS (dispute record,
per C5). Runs both readings of the C5 dispute and asserts they converge.

Run: python3 day_one_v2_DRAFT.py  (prints the day-one trace, exits 0 green)
"""


def run(reading):
    """reading: 'A' = found-materials (Bereshit Rabbah 1:9),
                'B' = day-one-creations (Chagigah 12a:6)."""
    assert reading in ("A", "B")
    W = {"TIME": None, "WORLD": set(), "REGISTRY": {}, "SPECS": [],
         "TESTS": {}, "LEDGER": {}, "UTTERANCES": 0, "WITNESS": {},
         "FLAGS": set()}

    # --- STEP 1  Gen 1:1  בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ
    # (be-reshit bara Elohim et ha-shamayim ve-et ha-aretz — "in the
    #  beginning God created the heavens and the earth")
    W["TIME"] = "t0"                       # C10: be-kadmin, temporal anchor
    W["UTTERANCES"] += 1                   # C1: ma'amar #1 despite no va-yomer
    themes = frozenset({"shamayim", "aretz"})   # C4: UNORDERED set — no
    #   temporal claim in surface order (Mekhilta: "both created together")
    includes = {"shamayim": {"sun", "moon", "constellations"},
                "aretz": {"trees", "grasses", "garden"}}   # C3: et-inclusions
    W["WORLD"] |= set(themes)
    W["WORLD"].add("matter_bulk")          # C2: bulk-create — all matter at
    #   once; the later fiats differentiate, not create from nothing again
    if reading == "B":                     # C5 reading B: the 1:2 entities are
        W["WORLD"] |= {"tohu", "vohu", "choshekh", "ruach", "mayim", "tehom"}
        W["WORLD"] |= {"length_of_day", "length_of_night"}   # Chagigah 12a:6

    # --- STEP 2  Gen 1:2  precondition block (zero events, v1 confirmed)
    state_facts = {"tohu(aretz)", "vohu(aretz)",
                   "over(choshekh, face(tehom))"}
    invariant = "hover(ruach_Elohim, face(mayim))"          # participle
    if reading == "A":                     # C5 reading A: found materials —
        W["FLAGS"].add("presupposed_read: choshekh/tehom/mayim/ruach "
                       "read without prior install (BR 1:9's philosopher)")
    W["WITNESS"]["1:2-materials"] = {
        "A": "Bereshit Rabbah 1:9 — found materials, answered elsewhere",
        "B": "Chagigah 12a:6 — ten things created on day one"}
    # C12: the census's own dissent — is 1:2's ruach ("wind/spirit") an
    # utterance? R. Yaakov ben Kurshai: yes; Menachem bar Yosei swaps it
    # for Gen 2:18. Carried as a recorded dispute, never decided here.
    W["UTTERANCES_DISPUTED"] = [
        ("Gen.1.2", "ruach as ma'amar ('utterance')",
         {"R. Yaakov ben Kurshai": "counts 1:2",
          "Menachem bar Yosei": "swaps for Gen 2:18"})]

    # --- STEP 3  Gen 1:3  וַיֹּאמֶר … יְהִי אוֹר וַיְהִי־אוֹר
    # (va-yomer … yehi or va-yehi or — "God said: let there be light —
    #  and there was light")
    W["UTTERANCES"] += 1                   # ma'amar #2 (first va-yomer form)
    W["SPECS"].append("exists(or)")        # jussive yehi = LET (v1, TIR-026)
    W["WORLD"].add("or")                   # differentiation of matter_bulk
    #   under C2 — not a second ex-nihilo create
    result_latency = 0                     # C6: va-yehi not ve-haya — "it
    W["SPECS"].pop()                       #   already was"; queue pops same verse

    # --- STEP 4  Gen 1:4  test + partition
    W["TESTS"]["tov(or)"] = "PASS"         # v1 confirmed
    # C7 + OWNER RULING 2026-08-20: the hidden light enters the world as
    # TYPED state — witness-grounded, distinct from the text-grounded
    # WORLD set, so a later text that refers to it (Ps 97:11 "light is
    # sown for the righteous") finds it mechanically, while the evidence
    # tier stays honest.
    # The light's EXISTENCE stays text-grounded (created at 1:3); only
    # the HIDING is testimony — witnessed state about a text-grounded
    # entity, not a second entity.
    W["WORLD_WITNESSED"] = {
        "hidden(or)": {                     # אוֹר הַגָּנוּז (or ha-ganuz,
            #   "the hidden light")
            "tier": "witness-grounded",
            "claim": "the primordial light hidden for the righteous; "
                     "tov ('good') read as the righteous",
            "sources": ["Bereshit Rabbah 3:6", "Chagigah 12a:10"]}}
    assert "choshekh" in W["WORLD"] or reading == "A"   # C5: under B the
    #   divide operates on an INSTALLED entity; under A the v1 flag stands
    partition = ("or", "choshekh")         # disjoint after the divide

    # --- STEP 5  Gen 1:5  naming + commit
    # C8: yom polysemy SPLIT (Onkelos): registry label = daytime sense
    #   (yemama, "daytime"); the ledger's calendar unit is the other sense.
    W["REGISTRY"]["or"] = "yom[daytime]"       # label write, LABEL != ENTITY
    W["REGISTRY"]["choshekh"] = "layla"        # (C7: "is the light the day?!")
    day_label = ("cardinal", "echad")      # C9: chain-witnessed intentional —
    #   yoma CHAD ("ONE day"), not ordinalized; [OPEN] closes to WITNESSED
    W["LEDGER"][1] = {"spec": "done", "test": "PASS", "names": 2,
                      "unit_sense": "yom[calendar]",       # C8
                      "label_form": day_label,             # C9
                      "cycle": "erev->boqer seder zemanim"}  # C11
    return W, state_facts, invariant, result_latency, partition, includes


def main():
    A = run("A")
    B = run("B")

    # C1/C2/C12 — utterance census: 2 counted, 1 disputed (never decided)
    for W, *_ in (A, B):
        assert W["UTTERANCES"] == 2, "day one carries utterances 1 and 2 of the ten"
        assert len(W["UTTERANCES_DISPUTED"]) == 1, \
            "C12: the ruach dispute is carried, not resolved"
        assert "matter_bulk" in W["WORLD"], "C2: bereshit-utterance seeds all matter"

    # C4 — theme order carries no claim (frozenset == frozenset regardless of order)
    assert frozenset({"shamayim", "aretz"}) == frozenset({"aretz", "shamayim"})

    # C5 — the dispute converges: identical post-1:5 OBSERVABLE state
    for key in ("REGISTRY", "TESTS", "LEDGER", "UTTERANCES", "TIME"):
        assert A[0][key] == B[0][key], f"C5 convergence fails on {key}"
    assert any("presupposed_read" in f for f in A[0]["FLAGS"]), \
        "reading A keeps v1's honest flag"
    assert not any("presupposed_read" in f for f in B[0]["FLAGS"]), \
        "reading B dissolves the flag: day-one creations"

    # C6 — latency zero
    assert A[3] == 0 and B[3] == 0

    # C7 + owner ruling — typed witnessed state: present under both
    # readings, tier honest, and never mixed into the text-grounded WORLD
    for W, *_ in (A, B):
        wl = W["WORLD_WITNESSED"]["hidden(or)"]
        assert wl["tier"] == "witness-grounded" and len(wl["sources"]) == 2
        assert "or" in W["WORLD"], "the light's existence is text-grounded"
        assert not set(W["WORLD_WITNESSED"]) & W["WORLD"], \
            "the tier wall: witnessed state never enters the text-grounded set"

    # C8 — the two senses of yom ('day') are distinct registry facts
    W = B[0]
    assert W["REGISTRY"]["or"] == "yom[daytime]"
    assert W["LEDGER"][1]["unit_sense"] == "yom[calendar]"
    assert W["REGISTRY"]["or"] != W["LEDGER"][1]["unit_sense"]

    # C9 — cardinal preserved
    assert W["LEDGER"][1]["label_form"] == ("cardinal", "echad")

    # C3 — inclusions declared on both themes
    inc = B[5]
    assert inc["shamayim"] >= {"sun", "moon"} and "garden" in inc["aretz"]

    print("day one v2 DRAFT — both readings run, all assertions green")
    print("  utterances after day one: 2 counted + 1 disputed (C1, C12)")
    print("  C5 dispute: A flags presupposed read; B installs on day one; "
          "observable state converges")
    print("  registry: or -> yom[daytime], choshekh -> layla; "
          "ledger unit yom[calendar]; day label cardinal echad ('one')")


if __name__ == "__main__":
    main()
