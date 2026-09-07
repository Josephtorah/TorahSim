# REPORT — THE EVENT-TYPE REGISTRY (D9-i, THE DAEMON CAMPAIGN's seeding sitting, 2026-09-07)

The owner's word: "Go" — the first sitting after compaction #72, on the ruled order of THE DAEMON
CAMPAIGN (COMPILE_DEBT.md D9: the seeding sitting first, then the daemon-edge gate, then the wraps
by engine family, then the deliverable rule amended). This sitting built the campaign's first
registry: World/step9/event_vocabulary.yaml, loaded and linted by World/step9/events_layer.py.

## What it is

The effects registry (effect_vocabulary.yaml, 242 effects) says what a compiled verdict may WRITE
to the ledger. The event-type registry says what the simulator's TAPE may CARRY — the other side of
every daemon. A daemon `law_x(event, world)` consumes an event by its `kind` and writes effects; the
kinds were, until this sitting, bare strings inside twelve functions and seven scene tapes, with no
registry, no witness, and no check that a watched kind is ever submitted or that a submitted kind is
ever watched. Now each type carries, in the effects registry's own harvest shape:

- `en` — the English;
- `he` — the verse's own words at the witness, pointed, with the English beside them;
- `form` — act / speech / statute / case (below);
- `witness` — one or more `"Book c:v | consonantal run"` pairs, MACHINE-VERIFIED by the lint against
  the Tanakh DB (elijah_docket/tanakh.sqlite): the run must be found contiguous in its verse;
- `ink` — every address the tape cites for the type;
- `corpus` — the frozen unit and the narrative tape's own EVENT label at that address where the unit
  logged one (the join by verse address to the corpus world's 557 narrative events);
- `tape` — who submits it (file, subjects) and who consumes it (daemon → effects written);
- `fields` — the event's parameters beyond kind / subject / case_source;
- `aliases_in_code` — where the seeding found one act under two names or one name over two acts.

Beneath the types, `narrative_verbs:` enumerates the corpus tape's own 254 verb labels (the frozen
units' EVENT operators) by count with each label's first witness; the 38 transliterated labels carry
their Hebrew and English, verified the same way; the 40 events whose operator carried no parseable
verb label are named by unit. Those labels are NOT event types — a daemon may watch one only after
it is promoted into `events:` with witnesses.

## How it was harvested (by script, coverage first)

- `d9_harvest.py` (scratchpad) scanned 34 files (every cold_run_*.py and world_engine.py): 74
  `.submit(` calls → 100 submit records (72 explicit dicts, 28 from tuple-driven tapes, 0 unresolved),
  and 12 daemons (`def law_*`) with the kinds each watches, the fields it reads, the effects it emits.
- `d9_join.py` joined every submitted kind's case source to the corpus world's events by verse
  address: 13 of the 82 submitted kinds meet a unit's own EVENT label at their address; 24 of the 557
  corpus events are touched; the law and run chapters (Exod 36-40, Lev 8-9, most of Gen 38 and 48-49)
  logged no EVENT operator — the narrative tape and the law tape are two different instruments.
- `d9_registry_gen.py` wrote the YAML: the hand layer is the English, the form, and the witness runs;
  every other field is generated from the two harvests; every witness run was verified before the
  file was written (a run not in its verse aborts the generator).
- `events_layer.py` lint: 84 types, 127 witness runs checked, 254 labels, 38 transliterations verified,
  0 flags.

| the census | count |
|---|---|
| daemons | 12 (the #72 tail said ten — law_vestments and law_eighth_day were missed; a count typed from memory) |
| kinds consumed by daemons | 82 |
| kinds submitted on tapes | 82 |
| union (kinds on the tape) | 83 |
| event types registered | 84 (the union + hands_feet_washed, declared before any tape submits it) |
| witness runs verified | 127 |
| forms | act 51 / speech 26 / statute 1 / case 6 |
| distinct effects the twelve daemons write | 101 of the registry's 242 (13 written by more than one daemon — the same ledger write reached from different acts: accepted, inspected_as_commanded, pays, and ten more) |
| corpus labels | 254 (38 transliterations glossed and verified; 40 unlabeled events in 9 units) |

## The four forms

The harvest sorted the kinds into forms the text itself distinguishes:

- **act** (51) — a deed the run records: the narrative verb, usually the wayyiqtol ("and he did"):
  וַיִּשְׁקֹל (and he weighed — Gen 23:16), וַיַּז (and he sprinkled — Lev 8:30), הוּקַם (was erected — Exod 40:17).
- **speech** (26) — a command, blessing, oath, sentence or plea the text records as UTTERED. The
  utterance is the event; the obligation it creates is the daemon's write: שְׁבִי אַלְמָנָה (sit as a widow
  — Gen 38:11) sets the timer, קִבְרוּ אֹתִי (bury me — Gen 49:29) opens the debit.
- **statute** (1) — the narrator's own law sentence inside the story: לֹא יֹאכְלוּ בְנֵי יִשְׂרָאֵל (the sons of
  Israel shall not eat — Gen 32:33), the sinew.
- **case** (6) — the law's own case token, the "when/if" clause. The skeleton's test scenes replay
  recorded Mishnah cases (Kiddushin 1:2, Bava Kamma 1:4 and 2:4, Shevuot 8:1, Bava Kamma 9:5), and
  the witness of such a kind is the clause the case instantiates, not a narrative: כִּי תִקְנֶה עֶבֶד עִבְרִי
  (when you buy a Hebrew slave — Exod 21:2), וְכִי יִגַּח שׁוֹר (and when an ox gores — Exod 21:28). This is
  the deliverable rule's amended sixth motion read off the ink: "conditions read from the ink's case
  tokens first."

## The seeding's findings (recorded, not fixed)

Each stands in the registry under `aliases_in_code`, for the daemon-edge gate (D9-ii) to flag and
the wrap sittings to unify — the seeding's job was to see, not to edit twelve daemons by hand.

1. **One name over two acts.** `washed` is submitted by the investiture tape for Lev 8:6 — וַיִּרְחַץ
   אֹתָם בַּמָּיִם (and he washed them with water: the body, Onkelos's immersion) — and by the erection
   tape for Exod 40:31 — וְרָחֲצוּ מִמֶּנּוּ (and they washed from it) אֶת יְדֵיהֶם וְאֶת רַגְלֵיהֶם (their hands and
   their feet: the laver's law of Exod 30:19-21). Two daemons watch the one name and write different
   effects (immersed against hands_feet_sanctified). The registry declares the split:
   `hands_feet_washed`, the first type registered before any tape submits it; the erection's kind is
   to be renamed at its wrap.
2. **One act under two names, at one verse — twice.** Lev 8:30's sprinkling is
   `milluim_blood_sprinkled` in the skeleton's law_installation and `garments_sprinkled` in the
   investiture's law_investiture; Lev 8:31-32's leftover is `milluim_leftover` and `meal`. Two
   daemons on one verse: in a world that registered both, both would fire.
3. **One type, two field contracts.** `renamed` is consumed by law_family (with a `name` field) and
   law_pre_sinai (without) — the same effect written under two interfaces.
4. **A branch watched and never fired.** `jubilee_proclaimed` is watched by law_slave_term and no
   tape submits it: the skeleton's scene 5 reaches the jubilee through slave_pierced's jubilee_year
   TIMER. The gate's coverage column will show it — "every daemon prints its watch coverage."
5. **An event submitted and consumed by nothing.** `overflow_reported` (Exod 36:5, the craftsmen's
   report) is on the construction tape and no daemon watches it — the daemon comments "no law." It is
   registered with its witness, honestly orphaned.
6. **Near-doublets that are NOT aliases**, kept distinct with the distinction written: work_completed
   (Exod 39:32, the making's completion) against work_finished (Exod 40:33, the erection's);
   glory_seen (Lev 9:23) against glory_filled (Exod 40:34); did_all (Lev 8:36) against inspected
   (Exod 39:43). Different verses, different acts.

## The join's honest shape

The corpus world's 557 events are the derivation era's EVENT operators — the narrative units' own
labels ('say' 58, 'beget' 30, 'take' 20, transliterations like 'chalam' and 'gava'). Where a
frozen unit logged an event at a tape verse, the registry cites it: purchased ↔ weigh_silver (Gen
23:16), gathered ↔ gava (Gen 49:33), crossed ↔ sikel_yadav (Gen 48:14), ceased_and_blessed ↔
finish + cease (Gen 2:2), circumcised ↔ circumcise (Gen 17:23, 21:4). The other 69 kinds sit on
chapters where no unit logged an EVENT operator at all — the sanctuary construction, the
investiture, the erection, the eighth day, and the recorded-case scenes. The two tapes measure
different things and the registry keeps both witnesses without pretending they coincide.

## What D9-ii builds on this

- `World.submit` validates the kind through `events_layer.validate` — an unregistered kind refuses
  the tape, as effects_layer refuses an unregistered effect.
- `daemon_census.py`, run by run_cold_all.py after the dependency gate: every daemon's watched kinds
  ∈ the event registry and submitted somewhere (watched-never-fired flagged); every effect it writes
  ∈ the effects registry; the aliases_in_code pairs flagged until unified; every compiled function
  with no daemon OWED — the generated worklist, written to DAEMON_INDEX.md.
- The fence's cascade depth bound and cycle detection in the engine (design, then the wraps).

## Lessons banked

- zsh does not word-split an unquoted `$r` — `${=r}` does; a loop that silently ran the whole
  harvest forty-one times was the tell.
- A relative `sqlite3.connect` CREATES an empty file where none exists: a stray 0-byte
  logic/corpus/corpus_world.sqlite was made by a probe and removed the same minute; the real DB is
  the repo root's corpus_world.sqlite (gitignored, rebuilt by the bake).
- Adjacent Python string literals concatenate — a case_source regex that stops at the first literal
  truncates the address; a conditional `'effect': (a if event.get(f) else b)` hides the field name
  as a false effect. Both caught by the generator's own assertion against the effects registry.
- A count carried in a compaction tail ("ten daemons") is a recital; the grep is the measurement.
