# HOW THE WORLD GETS BUILT
### A tutoring document — the database reading of Genesis

Written 2026-08-23, at the owner's request, after the night the schema
insight landed. This is the LEARNING companion to THE_WORLD.md (which
is the architecture note file — short, for building from). This file
is for understanding. It goes slow, defines every term, quotes the
actual receipts from our frozen units, and cites the tradition where
the tradition already said it first.

Everything quoted as a "receipt" below is real: it is copied from the
frozen unit YAMLs in logic/units/ — the machine's own record of what
each verse does, extracted at derivation and locked by the freeze.
Nothing here required changing one character of evidence. That is the
single most important fact in this document: **the structure was
already in our receipts. We recorded it verse by verse without
noticing we were building a database. This document is the noticing.**

---

## 1. The one-sentence insight

**Genesis 1:1 declares two root containers — the heavens and the
earth — and the rest of the Torah fills in, structures, links,
breaches, restores, deeds, and delegates their records.**

The owner said it first, as a question: "Does the statement 'create
heaven and earth' declare data structure? If you have heaven, then
something is added to heaven… does that sound like a database
structure or data records to be filled in?" The answer, checked
against 73 frozen Genesis units, is yes — and the text keeps doing it
for fifty chapters.

---

## 2. The machine we already have (a recap, so this stands alone)

Every frozen unit renders each verse as a short list of machine
operations ("ops"). The important ones for this document:

| Op | What it does | Plain example |
|---|---|---|
| DECLARE | someone speaks a demand; it enters the open queue | God: let there be a firmament |
| RESULT | the receipt; a demand is settled and leaves the queue | "and it was so" |
| EVENT | something happens | God makes the firmament |
| REGISTRY_INSTALL | an entity enters the world | WORLD += {gan} — the garden |
| NAME | a label is written into the registry | name(or) := yom — light is named Day |
| PRECONDITION_STATE | a standing state is recorded | darkness over the face of the deep |
| INVARIANT | a constraint that must keep holding | the firmament keeps dividing |
| EVENT_PARTITION | a two-sided division is drawn | waters-under / waters-over |
| NOTE_PRESUPPOSED | something is READ that was never installed | the waters of 1:6 |
| COMMIT | a day closes into the ledger | "a second day" |
| WITNESS_STATE | an oral-chain state, WALLED from facts | the upper waters hang by the word |
| CASE / HANDLER / STATUTE / PATTERN | standing law installs | Exodus 21's rules |

Running all 97 frozen units in order builds THE WORLD — 1,809 facts,
191 open demands, 81 names — and lands on the guarded hash. That run
is a PROOF: the text has one execution and we replay it exactly.

What this document adds is a second way to read the same ops: not as
a sequence of happenings but as a STRUCTURE being assembled.

---

## 3. Database words in plain English

Eight words carry the whole idea. Each gets one sentence and one
Genesis example.

- **Container (a "table")** — a thing that holds records. *The
  heavens. The earth. Later: the garden, a city, the ark.*
- **Record** — one entry living in a container. *The sun is a record
  in the firmament. A nation is a record in the earth.*
- **Field (a "slot")** — a named property on a record. *The lights
  have a location slot; the ground has a produce slot; a person has
  an occupation slot.*
- **Insert** — putting a record into a container. *"God SET them in
  the firmament of the heaven" (Genesis 1:17).*
- **Update** — changing a field on an existing record. *Avram's name
  field becomes Avraham.*
- **Partition** — splitting one container into two. *Waters above /
  waters below. Light / darkness. The earth divided in Peleg's days.*
- **Link (a "foreign key")** — one record pointing at another. *The
  river Pishon points at the land of Havilah; Havilah points at its
  gold.*
- **Trigger** — a stored rule that fires when a condition is seen.
  *"When the bow is seen in the cloud, I will remember My covenant."*

And one word for our method: a **fold** is a program that walks all
the frozen ops in order and accumulates something. corpus_world.py is
a fold that accumulates facts. The *structural fold* we intend to
build is a fold that accumulates this document's tree.

---

## 4. Genesis 1:1 — declaring the roots

בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ
("In the beginning God created the heavens and the earth.")

Today the machine records this as a creation event installing two
entities into a flat registry. The structural reading adds: these two
are not ordinary records — they are the two ROOT CONTAINERS. Nothing
in the rest of the Torah is ever created outside them. Everything
that follows is added to heaven, added to earth, or added to
something that was added to them.

The tradition supports reading 1:1 as declaring things that get
completed later:

- **Created, then hung.** Rashi on Genesis 1:14, from the sages: the
  lights were created on day one and only SUSPENDED in the firmament
  on day four. Creation-time and placement-time are two different
  columns on the same record. Our day-4 receipt (below) records
  exactly the placement.
- **Fluid, then congealed.** Midrash Rabbah, Genesis 4:2 with the
  Jerusalem Talmud, Berakhot 1:1: the works of day one were fluid and
  congealed on day two — day 1 creates material, day 2 structures it.
- **Heaven's own name is a join.** Our day-2 receipt records
  `name(raqia) := shamayim` — the firmament BUILT on day two IS the
  container NAMED Heaven. The build and the root merge in the
  registry. (Midrash Rabbah, Genesis 4:7 adds the etymology: Rav
  reads שָׁמַיִם ("Heaven") as אֵשׁ + מַיִם ("fire" + "water")
  kneaded together — the container's name records its materials.)

One more receipt matters here, and it is my favorite line the machine
ever wrote. Genesis 1:2's receipt, verbatim from the frozen unit:

> choshekh, tehom, mayim, ruach are READ without prior install
> **(uninitialized entities)**

The machine already speaks database. Darkness, the deep, the waters,
the wind — read before anything installed them. The text opens with
uninitialized state, and the machine flagged it years before we asked
this question.

---

## 5. The week as schema-then-records

The oldest structural observation about Genesis 1, now checkable in
our receipts: **days 1–3 create the domains; days 4–6 fill them; the
days match one-to-one.**

| Creates the domain (days 1–3) | Fills it (days 4–6) |
|---|---|
| **Day 1** — light / darkness partitioned | **Day 4** — luminaries inserted into the firmament, to rule day and night |
| **Day 2** — the firmament; waters above / below | **Day 5** — fish into the waters, birds across the firmament's face |
| **Day 3** — land and seas; vegetation | **Day 6** — land animals from the earth; the human over it all |

Then Genesis 2:1 closes the population in the text's own words:

וַיְכֻלּוּ הַשָּׁמַיִם וְהָאָרֶץ וְכָל־צְבָאָם
("And the heavens and the earth were finished, **and all their
host**") — the containers, and their contents, complete. Day 7
commits: no inserts, no utterances (our day-7 unit records ZERO
census utterances — the speech-less day), the ledger closes, and rest
itself is the day's one creation (the tradition's teaching, carried
in our day-7 unit as a witness state: menuchah, created_with_the_day).

**The receipts already carry the filling as structure.** Verbatim
from the frozen units:

- Day 4 — `HOLDS(exists(meorot), loc=raqia_ha_shamayim, t1)` — the
  luminaries exist **with a location slot**: the firmament of the
  heavens. The verse said it first: וַיִּתֵּן אֹתָם אֱלֹהִים
  בִּרְקִיעַ הַשָּׁמַיִם ("and God SET them IN the firmament of the
  heavens," 1:17).
- Day 5 — `HOLDS(swarm(mayim), product=sheretz_nefesh_chaya, t1)` —
  the waters carry a **product slot**: they produce swarming life.
  And `HOLDS(fly(of), loc=pnei_raqia_ha_shamayim, t1)` — the birds'
  location: the face of the firmament.
- Day 6 — `HOLDS(totze(aretz), product=nefesh_chaya_le_minah, t1)` —
  תּוֹצֵא הָאָרֶץ ("let the earth BRING FORTH"): the earth is a
  producer with a typed product — living soul, by its kind.

Notice the grammar of the domains: the waters SWARM, the earth
BRINGS FORTH — domains are not passive boxes; they are producers
whose product slots are typed ("by its kind"). And day 6's blessing
writes the standing instruction that chapter 11 will enforce:

פְּרוּ וּרְבוּ וּמִלְאוּ אֶת־הָאָרֶץ
("Be fruitful and multiply and FILL THE EARTH") — a mandate recorded
in our day-6 unit as standing facts. **The blessing is a fill
instruction on the earth domain.** Hold that thought until Babel.

---

## 6. EARTH — the domain that structures itself

### 6.1 The garden: the first sub-container, and the map layer

Genesis 2:8 — God plants a garden. The receipt:

> EVENT plant · Agent YHWH_Elohim · Theme gan
> REGISTRY_INSTALL **WORLD += {gan}**

A new container, installed inside earth, by planting. And in the same
verse the machine invents a class we will need forever — Eden itself
enters as:

> eden are READ without prior install **(the place-name enters as
> known geography)**

"Known geography." Places the text treats as already-there — Eden,
Shinar, the river of Egypt, the great river Euphrates — are
presupposed, not created. That class IS the world's **map layer**:
geography the simulation must carry as background, distinct from
things whose creation the text narrates.

Nesting goes one level deeper immediately: the tree of life is
בְּתוֹךְ הַגָּן ("in the MIDST of the garden," 2:9) — the same
preposition that put the firmament "in the midst of the waters."
Containers inside containers, in the text's own prepositions.

### 6.2 The four rivers: links and resources

Genesis 2:10–14. The receipts, in order:

> `HOLDS(nahar_yotze_me_eden(le_hashqot_et_ha_gan))` — a river goes
> OUT of Eden TO WATER the garden (a flow between containers)
> `WORLD += {nahar, nahar_1, nahar_2, nahar_3, nahar_4}` — five
> installs: the river and its four heads
> `name(nahar_1) := Pishon` … `name(nahar_2) := Gichon` …
> `name(nahar_3) := Chidekel ∧ name(nahar_4) := Perat`
> `HOLDS(sovev_kol_eretz_ha_chavilah(nahar_1))` — Pishon CIRCLES the
> land of Havilah
> `HOLDS(sham_ha_zahav(chavilah))` — "THERE is the gold"

Read that as a database and it is three linked tables: rivers, lands,
resources. Pishon → Havilah → gold (and the text adds bdellium and
onyx). Gihon → Cush. Tigris → east of Assyria. The Euphrates needs no
link — it is the known river. Four chapters into the Torah, the world
has a hydrology with foreign keys.

### 6.3 The curse: an UPDATE on the produce slot

Genesis 3 does not delete anything. It UPDATES fields. The receipts
from the sentences unit (3:14–24):

> serpent — `HOLDS(al_gechonkha_telekh)` (on your belly you shall go)
> ∧ `HOLDS(afar_tokhal_kol_yemei_chayekha)` (dust you shall eat)
> ground — `HOLDS(kotz_ve_dardar_tatzmiach_lakh(adamah))` — thorn
> and thistle **it shall sprout for you**
> man — bread by the sweat of the face, and the return-to-dust
> clause: עַד שׁוּבְךָ אֶל־הָאֲדָמָה ("until you return to the
> ground") — the record's end-state points back at its source
> container

Compare day 3's produce slot: the earth brought forth grass, herb
yielding seed, fruit tree. After the curse the SAME slot on the SAME
container yields thorn and thistle. **The schema survives; the output
changes.** That is what a field update is. The domain was not
destroyed — its production rule was rewritten, per record, by
sentence.

And the chapter ends with a new record class: a **boundary guard**.

> `station(keruvim)` · `WORLD += {keruvim, lahat_ha_cherev}` — the
> cherubim and the flame of the turning sword, INSTALLED and
> STATIONED at the east of the garden, guarding the way to the tree
> of life.

Access control, at a container's entrance, facing a specific record.

### 6.4 Man starts creating containers

Genesis 4:17, in Cain's line — the receipt is startlingly literal:

> `WORLD += {ir}` — a CITY is installed
> `name(ir) := Chanokh` — and named, after his son

The first human-made container. God installed domains; now a man
installs one and writes to the registry himself. The same unit fills
in the first **occupation fields** on person records: Yaval "father
of tent-dweller and herd," Yuval "father of all who grasp harp and
pipe," Tuval-Kayin "forger of every craftsman of bronze and iron" —
culture entering the schema as fields on people.

From here the human-made container class only grows: the tower and
city of Babel (below), altars, wells (below), and eventually the ark
— which gets its own section because it is the best schema story in
Genesis.

### 6.5 Babel: refusing the fill instruction

Genesis 11. The receipt records something that never happened before:

> `DECLARE(ish_el_reehu, CMD-US?(nivneh(ir_u_migdal)))`

DECLARE — the op that until now belonged to God and the ledger's
great speakers — spoken by "each man to his fellow": **let US build a
city and a tower.** The first human-spoken build demand in the
corpus. And the tower's spec aims at the other root container:
וְרֹאשׁוֹ בַשָּׁמַיִם ("its top in the heavens") — an attempted write
from earth into heaven.

Now recall day 6's mandate: וּמִלְאוּ אֶת־הָאָרֶץ ("and FILL the
earth"). Babel's whole point, in its own words, is פֶּן־נָפוּץ
("LEST WE BE SCATTERED") — they cluster to avoid filling. The
scatter that answers them — וַיָּפֶץ יְהוָה אֹתָם עַל־פְּנֵי
כָל־הָאָרֶץ ("and the LORD scattered them over the face of ALL the
earth") — is the fill instruction being ENFORCED. The blessing was a
distribution requirement on the earth domain; Babel violated it; the
scatter executes it. The language partition rides along: one tongue
becomes seventy, so the population partition (next section) can hold.

### 6.6 The nations table: earth's population partitioned

Genesis 10 — and the text states its own schema, three times, once
per son of Noah. The receipt for Ham's line (verbatim pattern, same
for Shem and Yefet):

> `HOLDS(eleh_vnei_cham_le_mishpechotam_li_leshonotam_be_artzotam_be_goyehem)`

"These are the sons of Ham, **by their families, by their tongues, in
their lands, in their nations.**" Four columns: family, tongue, land,
nation. Seventy records. The Canaanite's ten peoples enumerated and
then: "and afterward the families of the Canaanite SPREAD ABROAD" — a
distribution note on a partition. And one man's name carries the op
itself: פֶּלֶג ("Peleg — for in his days the earth was DIVIDED,"
niflegah, 10:25) — a person record whose name field stores a
partition event on the earth domain.

### 6.7 Land becomes property: deeds, borders, assignments

Three receipt-backed stages, in order of formality:

1. **Borders by decree.** Genesis 15:18, the covenant between the
   pieces: `HOLDS(mi_nehar_mitzrayim_ad_ha_nahar_ha_gadol_nehar_perat)`
   — "from the river of Egypt to the great river, the river
   Euphrates." The rivers of chapter 2's hydrology come back as
   BORDER MARKERS — the map layer reused as a deed's metes and
   bounds. Ten nations listed as the land's current holders.
2. **A purchase, witnessed.** Genesis 23, Machpelah — the receipts
   read like a closing: `DECLARE(avraham, LET(qach(kesef_ha_sadeh)))`
   ("take the silver of the field" — a demand to accept payment!),
   the price stated (`arba_meot_sheqel_kesef` — four hundred shekels
   of silver, "between me and you"), then
   `weigh_silver · Agent avraham · Beneficiary efron` — and the text
   closes with the field, the cave, and every tree in the border
   RISING (וַיָּקָם — "and it was established") to Abraham as a
   possession before the witnesses at the gate. The first fully
   receipted ownership transfer: parties, price, payment event,
   witnesses, and a description of the parcel.
3. **An assignment granted.** Genesis 47 — the sons of Jacob DECLARE
   a dwelling demand (`yeshvu_na_avadekha_be_eretz_goshen` — "let
   your servants dwell in the land of Goshen") and Pharaoh's grant is
   the RESULT that settles it. A land assignment as demand → receipt,
   through the machine's ordinary queue.

Property law grows out of the map layer in three steps: decreed
borders, purchased parcels, granted residencies.

---

## 7. WATERS — breach and restore

The creation schema gave waters their structure on days 2 and 3: the
vertical partition (above/below the firmament) and the horizontal
gathering (seas vs land). The flood is the text operating on that
structure directly — not a lot of rain, but two named apertures in
the schema opening at once. The receipts:

> Genesis 7:11 — `split(e2) ∧ Theme(mayenot_tehom_rabbah)` — the
> fountains of the GREAT DEEP split open (the waters below burst UP)
> Genesis 7:11 — `open(e3) ∧ Theme(arubot_ha_shamayim)` — the
> WINDOWS OF THE HEAVENS open (the waters above pour DOWN)

Day 2's partition breached from both sides simultaneously. The land
domain submerges under the water domain (the mountains covered); the
world runs back toward Genesis 1:2's uninitialized waters. This is
the tradition's own reading — the flood as un-creation — and our
receipts carry it as paired structural ops. Then the restore:

> Genesis 8:2 — `stop_up(e4) ∧ Theme(mayenot_tehom_va_arubot_ha_shamayim)`
> — both apertures closed in one op

and the day-3 gathering re-runs (the waters recede, the tops of the
mountains are seen — land re-emerges from water exactly as it first
did). Genesis 8:22 then re-affirms the standing invariants — seedtime
and harvest, cold and heat, summer and winter, day and night "shall
not cease" — the schema's constraints re-committed after the breach.

**Wells: access points, with a registry restore.** Water re-enters
the story as infrastructure in Genesis 26. The receipts are a
sysadmin's diary:

> `redig_wells · Agent yitzchaq · Theme beerot_avraham` — Isaac
> re-digs his FATHER'S wells (stopped up by the Philistines)
> `restore_names_like_father` — **and restores their NAMES,
> "according to the names his father had called them"**
> `dig_and_find · Theme beer_mayim_chayim` — a new well of LIVING
> water
> `name(beer_eseq) := eseq` ("Contention") ·
> `name(beer_sitna) := sitna` ("Enmity") ·
> `name(beer_rechovot) := rechovot` ("Wide places")

The machine's own op name is `restore_names_like_father` — a registry
RESTORE from the previous generation's backup. And the three new
wells carry their dispute status in their names: two contested, one
at last uncontested — access-point records with a conflict field,
written into the map.

---

## 8. HEAVENS — records, apertures, triggers, and a gate

The heavens fill on day 4 (the `loc=raqia_ha_shamayim` insert) and
day 5 (birds on the firmament's FACE — note the slot: not IN it, on
its surface; the receipts keep even that distinction). Then three
later structures:

### 8.1 The windows — the heavens are openable

אֲרֻבֹּת הַשָּׁמַיִם ("the windows of the heavens," 7:11) — the
flood receipts above show the heavens have APERTURES: openable,
closable, named. The container has hardware.

### 8.2 The bow in the cloud — the sky's first trigger

Genesis 9:13–14. The receipts, verbatim:

> `HOLDS(et_qashti_natati_be_anan)` — "My bow I have SET in the
> CLOUD" — a record installed in a heaven sub-container (the cloud)
> `HANDLER IF(be_anni_anan_ve_nireatah_ha_qeshet)
> THEN(ve_zakharti_et_briti)` — IF, when I cloud the cloud, the bow
> is seen — THEN I will remember My covenant

A HANDLER — the op class that carries Exodus 21's law — installed in
Genesis 9, riding a sky record. The heavens' first stored trigger: a
visible condition, a covenant consequence, standing forever. The
covenant sign is not a memory aid bolted on; in the machine's terms
it IS an if/then rule whose condition is a record in the cloud.

### 8.3 The ladder and the gate — a channel between the roots

Genesis 28:12,17. The receipts:

> `dream_event(yaaqov, sulam)` — the Torah's first narrated dream-act
> `HOLDS(sulam_earthward_head_heavenward_angels)` — the ladder: SET
> EARTHWARD, its head HEAVENWARD, angels ascending and descending
> `HOLDS(fear_doublet_bet_elohim_shaar_ha_shamayim)` — "this is none
> other than the HOUSE OF GOD, and this is the GATE OF THE HEAVENS"
> (שַׁעַר הַשָּׁמַיִם — shaar ha-shamayim)

A channel between the two root containers, with traffic in both
directions — and then the stunning part: the interface point gets an
EARTH ADDRESS. Jacob names the place Bethel. The gate of heaven has a
location record in the map layer. (Babel tried to build this channel
upward by force and was scattered; Bethel receives it downward in a
dream and gets a name in the registry. The contrast is the text's
own.)

---

## 9. THE ARK — a container with a spec sheet

The flood needed one section of its own, because before the breach
comes the most explicit container specification in the Torah.
Genesis 6:14–22, receipts in order:

> `DECLARE(Elohim, LET(aseh(noach, tevah)))` — the build demand
> enters the queue: make yourself an ark
> `HOLDS(tevat_atzei_gofer_qinim)` — material (gopher wood) and
> internal structure: קִנִּים ("rooms/nests" — compartments!)
> `HOLDS(ve_khafarta_ba_kofer)` — sealed inside and out with pitch
> `HOLDS(shelosh_meot_amah_orekh) ∧ HOLDS(chamishim_amah_rochbah) ∧
> HOLDS(sheloshim_amah_qomatah)` — dimensions: 300 cubits long, 50
> wide, 30 high
> `HOLDS(tzohar_la_tevah)` — a light/window
> `HOLDS(petach_ba_tzidah)` — a door in its side
> `HOLDS(tachtiyim_shniyim_u_shlishim)` — THREE DECKS: lower, second,
> third
> `HOLDS(shnayim_mi_kol_tavi_el_ha_tevah)` — the manifest: TWO of
> every kind, male and female
> `HOLDS(le_minehu_manifest_of_behemah_remes)` — the manifest is BY
> KIND — the same type column day 5 and 6 created ("after its kind")
> is now the loading list's sort key
> `make(noach, tevah)` · `WORLD += {tevah}` — built and installed
> `RESULT: HOLDS(aseh(noach, tevah))` — the receipt: the demand pops

Then boarding (Genesis 7): the demand `bo(noach, el_ha_tevah)` —
come INTO the ark — with the clean animals upgraded to SEVENS
(`shivah_shivah_ha_behemah_ha_tehorah`) and the purpose slot stated:
לְחַיּוֹת זֶרַע עַל־פְּנֵי כָל־הָאָרֶץ ("to keep SEED alive on the
face of all the earth") — and the LORD shuts the door behind him
(וַיִּסְגֹּר יְהוָה בַּעֲדוֹ — "and the LORD closed it for him,"
7:16).

Read as a system: **the ark is a backup.** A specified, compartmented,
sealed container is built to the declared spec; records are selected
BY KIND from every table of the land and air domains; redundancy is
set higher for the records that will be needed first (the clean
kinds, for the altar of chapter 8); the container is closed by the
system owner, not the operator; the storage domain is then breached
and flooded; and when the structure is restored, the container
reopens and the records re-populate the domains — with the fill
instruction reissued to Noah in Genesis 9 in the very words of day 6:
פְּרוּ וּרְבוּ וּמִלְאוּ אֶת־הָאָרֶץ ("be fruitful and multiply and
fill the earth"). Backup, wipe, restore, re-fill. The week's schema
survives the flood because one container was built to spec before
the windows opened.

---

## 10. THE REGISTRY — who holds the pen

The names registry is the world's oldest table, and its story across
Genesis is a story about DELEGATION and UPDATE SEMANTICS.

**Days 1–3: God names.** or → yom, choshekh → layla (light → Day,
darkness → Night), raqia → shamayim, and the gathered waters → seas.
Five namings, all divine, all at creation.

**Chapter 2: the pen is handed over.** God brings the beasts to the
man "to see what he would CALL them; and whatsoever the man called
every living creature, that was its name" (2:19). Our receipt even
preserves the cross-unit bookkeeping: the beasts are "named in this
span, FORMED at gen_06" — created in one unit, labeled in another,
provenance held. Then `name(ishah) := ishah` (2:23, the man names
the woman "Woman") and after the sentences, `name(ishah) := Chavah`
(3:20 — Eve, "mother of all living"): the same record named twice,
by the same human namer, before and after the fall.

**Places pour in.** The city Chanokh (4:17). Babel (11:9 — named BY
its scatter). Beer-lachai-roi, Beer-sheva. Bethel. Machanayim and
Peniel (Jacob's receipts: `name(maqom_machanayim) := machanayim`,
`name(maqom_peniel) := peniel`). The wells Eseq, Sitnah, Rechovot.
The registry becomes a gazetteer — every named place is an address
in the map layer, and most carry their story in their name.

**Renames: the update semantics get formal.** Two receipts:

> Genesis 17:5 — `HOLDS(lo_yiqare_od_shimkha_avram)` ∧
> `HOLDS(ve_hayah_shimkha_avraham)` — "your name shall NO MORE be
> called Avram; your name SHALL BE Avraham." (And 17:15 the same for
> Sarai → Sarah: "do not call her name Sarai, for Sarah is her
> name.")
> Genesis 32:29 — `HOLDS(lo_yaaqov_yeamer_od_ki_im_yisrael
> (decree_fact))` — "no more Yaakov but Yisrael" — and the machine
> marked it **decree_fact**.

Here the tradition itself discusses the two update modes, explicitly
(Babylonian Talmud, Berakhot 13a): one who calls Abraham "Avram"
after the change transgresses — the old key is RETIRED, the update is
destructive. But Jacob is called Jacob by the text itself forever
after — Yisrael is an ALIAS added alongside, both keys live. The
Talmud raises exactly this contrast. Two rename semantics —
replace vs alias — distinguished in the fifth chapter of tractate
Berakhot, and our receipts already carry the difference (the
absolute retirement clause on Abraham's; a decree fact, with usage
continuing, on Jacob's).

**People are records with fields.** The genealogy ledgers (Genesis 5,
11) are literally tables: name, age at begetting, remaining years,
total, died — row after row, with one record removed early ("and he
was not, for God TOOK him" — Enoch, an exit with a nonstandard
close). The occupation fields of Cain's line (tents/herds, music,
metal). The seventy souls of Genesis 46 — a census with subtotals by
mother. And one PATTERN receipt writes standing practice out of a
single night: `PATTERN(lo_yokhlu_bene_yisrael_et_gid_ha_nashe)` —
"therefore the children of Israel eat not the sinew of the thigh" —
a story compiling into a standing rule, the narrative machine feeding
the law machine.

---

## 11. The new record classes (the collector's list)

Everything above, compressed into the classes the structural fold
will need. Each is evidenced; none is invented.

| # | Class | First appearance | Receipt anchor |
|---|---|---|---|
| 1 | Root containers | Genesis 1:1 | heavens + earth installed |
| 2 | Domains with product slots | days 3, 5, 6 | `product=` receipts |
| 3 | Inhabitants with location slots | days 4, 5 | `loc=` receipts |
| 4 | Known geography (map layer) | Eden, 2:8 | "the place-name enters as known geography" |
| 5 | Geographic links + resources | the four rivers, 2:10–14 | Pishon → Havilah → gold |
| 6 | Field updates by decree | the curse, 3:14–19 | thorn-and-thistle on the ground's produce slot |
| 7 | Boundary guards | 3:24 | cherubim + flaming sword stationed |
| 8 | Human-made containers | Cain's city, 4:17 | `WORLD += {ir}` · `name(ir) := Chanokh` |
| 9 | Specified containers (backup) | the ark, 6:14–22 | dimensions, decks, manifest by kind |
| 10 | Schema breach / restore | the flood, 7:11 / 8:2 | fountains split + windows open; stop_up |
| 11 | Domain triggers | the bow, 9:13–14 | HANDLER riding a cloud record |
| 12 | Population partitions | nations table, ch. 10 | family/tongue/land/nation ×3; Peleg |
| 13 | Fill-instruction enforcement | Babel, ch. 11 | the mandate of 1:28 vs "lest we be scattered" |
| 14 | Channels between roots | the ladder, 28:12,17 | earthward-set, heavenward-headed; the gate |
| 15 | Ownership: borders, deeds, grants | chs. 15, 23, 47 | rivers as markers; weigh_silver; Goshen demand→receipt |
| 16 | Registry delegation + rename semantics | 2:19; 17:5; 32:29 | man names; replace (Avraham) vs alias (Yisrael) |
| 17 | Registry restore | the wells, 26:18 | `restore_names_like_father` |
| 18 | Person records with fields | chs. 4, 5, 46 | occupations; lifespans; the seventy |

---

## 12. What this means for the build

**Nothing gets re-derived.** The constitution rules it: the frozen
ops are evidence, immutable; what this document describes is a MODEL
— a second fold over the same evidence. corpus_world.py folds the ops
into facts and demands; the STRUCTURAL FOLD will fold the same ops
into the tree: roots, domains, sub-containers, records, slots, links,
guards, triggers, channels — every edge citing the op that grounds
it, exactly the way every fact today cites its verse.

**What the dashboard gains.** A WORLD TREE tile: heaven and earth
standing empty for three days, then filling; the garden budding
inside earth; the ark assembling its decks and taking its manifest;
the tree going dark under the flood and re-lighting; the nations
fanning out of the ark's three name-branches. The stationary
dashboard's rule — the change announces itself — applies: the branch
that grew is the branch that flashes.

**What stays carried, never flattened.** Created-time vs placed-time
are two columns (the light of day 1, hung on day 4 — the tradition's
teaching, not our invention). Disputes stay disputes. The witness
tier stays walled — the hidden light and the hanging waters are in
the tree only as witness annotations, never as machine facts. And
the map layer keeps its honesty: known geography is presupposed, not
created, and the fold must say so.

**The two machines stay two.** The proof machine replays the one
execution and lands on the hash. The structural fold reads its
receipts and shows the shape. Neither replaces the other; the second
makes the first VISIBLE.

---

## 13. Provenance — where every claim above lives

All receipts quoted are from logic/units/*.yaml (frozen, hash-guarded
through corpus_world.py). Units cited in this document:

gen_01_creation_boot (1:1–5) · gen_02_raqia_day (1:6–8) ·
gen_03_double_build (1:9–13) · gen_04_lights_calendar (1:14–19) ·
gen_05_swarms_blessing (1:20–23) · gen_06_land_adam_dominion
(1:24–31) · gen_07_completion_sanctity (2:1–3) ·
gen_08_toledot_garden_first_rule (2:4–17) ·
gen_09_helper_woman_first_speech (2:18–25) · gen_11_sentences_exile
(3:14–24) · gen_12_cain_abel (4:1–16) · gen_13_cain_line_seth
(4:17–26) · gen_14_adam_line_ledger (ch. 5) · gen_16_ark_spec
(6:9–22) · gen_17_boarding (7:1–16) · gen_19_the_remembering
(8:1–14) · gen_20_exit_altar (8:15–22) · gen_22_covenant_bow
(9:8–17) · gen_24_nations_table (ch. 10) · gen_25_babel (11:1–9) ·
gen_31_covenant_pieces (ch. 15) · gen_33_shaddai_covenant_flesh
(ch. 17) · gen_39_machpelah_purchase (ch. 23) ·
gen_45_wells_covenant_esau_wives (26:17–35) · gen_48_bethel_ladder_vow
(ch. 28) · gen_55_two_camps_wrestled_name (ch. 32) ·
gen_70_goshen_and_the_fifth (ch. 47)

Tradition cited: Rashi on Genesis 1:14 (created day one, hung day
four) · Midrash Rabbah, Genesis 4:2 with Jerusalem Talmud, Berakhot
1:1 (fluid then congealed) · Midrash Rabbah, Genesis 4:7 (Heaven =
fire + water) · Babylonian Talmud, Berakhot 13a (Avram/Avraham vs
Yaakov/Yisrael — the two rename semantics).

*Experimental model — not binding religious law. The receipts are
the evidence; this document is a reading of them.*
