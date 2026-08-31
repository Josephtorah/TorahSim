# THE VAYETZE PILOT — what the estimate was worth

**Date:** 2026-08-30 · **Span:** Genesis 28:10–32:3, 148 verses, units gen_48–gen_55
· **Purpose:** turn "six to seven sittings" into a measurement by running all
four phases on the parashah with the densest movement in Genesis.

Run it: `python3 placement/gazetteer.py && python3 placement/extract.py vayetze
&& python3 placement/build_placement.py`

---

## THE HEADLINE: THE ESTIMATE RESTED ON A NUMBER THAT COUNTED PEOPLE AS PLACES

The plan said **654 of 909 location-bearing verses (72%) name a target the
machine can propose from.** That number counted *any proper noun* in the verse.
Once persons are separated from places — which is what phase 1 exists to do —
it collapses:

| | Vayetze | all Genesis |
|---|---|---|
| verses with a location-bearing verb | 92 | 909 |
| …and ANY proper noun — **the old measure** | 65 (71%) | 621 (68%) |
| …and a **PLACE** proper noun — the real test | **6 (7%)** | **187 (21%)** |

The old figure reproduces exactly (71% / 68% against the recorded 72%), so this
is the same measurement corrected, not a different one. `RESUME.md` had already
flagged the risk in words — *"Abraham took Sarah has a verb and a proper noun
and no destination"* — and it turns out to be the dominant case, not an edge
case.

## PRECISION AND RECALL, MEASURED

Six proposals from 148 verses. Every one graded against the verse:

| ref | proposal | grade |
|---|---|---|
| 28:10 | Jacob **from** Beer-sheba | ✅ correct |
| 28:10 | Jacob **to** Haran | ⚠️ goal, not position |
| 31:18 | — **at** Padan-aram | ❌ wrong |
| 31:18 | Isaac **to** Canaan | ⚠️ place right, subject wrong |
| 31:23 | — **at** mount Gilead | ⚠️ place right, subject missing |
| 31:25 | Laban **at** mount Gilead | ✅ correct |

- **Precision on the full triple (who + relation + where): 2 of 6 = 33%.**
- Precision on place-and-relation alone: 4 of 6 = 67%.
- Reading the parashah found **7 accepted placements**; the machine supplied
  2 of them. **Recall = 29%.**

### The three failure modes, each worth a design decision

1. **GOAL IS NOT POSITION.** "He went toward Haran" (28:10) states a
   destination. Recorded as a placement it puts Jacob at Haran one verse before
   he reaches Bethel. `to` rows must never create position on their own.
2. **A LOCATIVE INSIDE A SUBORDINATE CLAUSE IS NOT A PLACEMENT.** "which he had
   acquired in Padan-aram" (31:18) locates the *acquiring* of livestock. The
   extractor cannot see clause boundaries.
3. **THE NEAREST-NAME HEURISTIC PICKS THE WRONG PERSON.** At 31:18 the nearest
   preceding name is Isaac — the man Jacob is going *to*, not the one moving.

## THE STRUCTURAL FINDING: PLACEMENT IS STATE, NOT A TAG

Vayetze places Jacob at Haran **once** and then says nothing about where he is
for the next eighty-eight verses. The twenty years of service, the wages, the
births of eleven children — all of it happens at an unnamed well, an unnamed
field, unnamed tents. A per-verse tagger leaves Jacob's location blank for most
of the parashah.

So every row carries a validity range and propagates until something moves it.
That is already the shape of the world's `entity_state`, and it works:

```
where is Jacob at Gen 30:25?
   Jacob is at Haran — placed Gen 29:4, holds until Gen 31:25
   (the verse itself names no place at all)
```

**The 88 verses with a movement verb and no named place are not a backlog to
clear. They are verses that need no placement of their own** — the state
already covers them. That inverts the plan's arithmetic: the reading queue is
not 255 verses of missing data, it is mostly verses already answered by
propagation.

## WHAT THE MACHINE CANNOT REACH, AND WHY

Every one of the five placements reading had to supply was invisible to the
machine *in principle*, not by a fixable bug:

- **28:11 Bethel** — the verse that positions Jacob has no name in it; the verse
  that names the place has no motion in it. The two never meet.
- **29:4 Haran** — arrival established by *reported speech about somebody else's
  origin*: "we are from Haran." No motion verb touches Jacob.
- **31:21 mount Gilead** — direction carried by the idiom "he set his face
  toward," which no preposition or ending marks.
- **31:25 Jacob** — two men placed in one verse; the extractor emits one
  proposal per place token and kept only the second.
- **32:1 Laban departs** — "returned to his place." The destination is a pronoun.

## WHAT PHASE 1 LEARNED (kept, because the bugs are the lesson)

The gazetteer was wrong four times before it was right, and every fix is
recorded in the script:

1. **"Governed by a locative preposition" is not a place signal.** "To Jacob"
   and "to Bethel" take the same preposition. The first draft reported Jacob,
   Joseph, Abraham, Pharaoh and the divine Name as places. Replaced by the rule
   that actually discriminates: **persons act, places do not.**
2. **Key on the lemma, not the surface form** — "and-Lot", "to-Pharaoh" and
   "from-Beer-sheba" were separate names from Lot, Pharaoh and Beer-sheba.
   400 real names, not 629.
3. **The directional ending is a suffix**, so a prefix guard misses it:
   "Timnah-ward he went up" read as "Timnah went up," and Sodom, Gerar, Zoar
   and Asshur all registered as people.
4. **"Land of X" is possession when occasional and toponymic when habitual.**
   Demoting it outright cost Canaan, the paradigmatic land of Genesis. Promoted
   at three or more occurrences: Canaan (8) and Egypt become places; Pharaoh
   (1) and the divine Name (1) stay persons.

And one signal was missing entirely: **Genesis MAKES toponyms by naming them**
("and Jacob called it Galeed"). The fold already recorded every such naming, so
the gazetteer now reads the corpus's own `names` table rather than
pattern-matching the formula. That alone recovered Bethel, Galeed, Mahanaim,
Peniel and Rehoboth.

Final gazetteer: 21 places, 144 persons, **14 both**, 20 probable places,
201 unknown (mostly genealogy names). The 14 "both" are not errors — they are
Genesis's real eponym problem: Egypt, Canaan, Shechem, Nahor, Haran, Seir and
Cush are each a person *and* a place in this book.

## THE REVISED ESTIMATE

The plan's six-to-seven sittings assumed the machine would propose most
placements and a human would check them. Measured, the machine proposes few and
gets a third of those fully right, so **the work is a reading task with machine
assistance, not a machine task with review.**

Against that, propagation removes most of the volume: entities are placed at a
handful of named seats per parashah and hold in between.

**Revised: about one sitting per parashah for the remaining eleven Genesis
parashiyot, plus one to generalise the placement table into the world proper —
call it twelve, against the estimated six.** Phases 1, 2 and 4 are now built and
reusable; what does not compress is phase 3, the reading.

**This is a measurement of Vayetze only.** Vayetze is unusual: it is one long
stay in one unnamed place. Parashiyot that travel — Lech Lecha, Vayera,
Vayishlach, Vayigash — will name more places per verse and should score better.
The honest range is that the machine's share rises in travel narratives; nothing
here measures by how much.

## WHAT IS BUILT AND WORKING

```
placement/gazetteer.py         phase 1 — 400 names classified from evidence
placement/gazetteer.json         its output, every verdict carrying its evidence
placement/extract.py           phase 2 — proposals for a parashah
placement/proposals_vayetze.json
placement/reviewed_vayetze.json  phase 3 — every proposal graded against the verse
placement/build_placement.py   phase 4 — folds accepted rows with propagation
```

`world.sqlite` now carries a `placement` table (7 rows, Vayetze). The world
still reconciles green against `corpus_world.fold()` on all ten counts and the
state hash — the placement layer is additive and touches no frozen evidence.

**Nothing was written back to the corpus.**
