# RESEARCH LOG — is 100% of the code in the written Torah?

Opened 2026-09-03 on the owner's order ("yes do the research. Keep
notes in a temp log we can review"). Working file — findings land
here as they happen, raw, dated, with dead ends kept.

## THE HYPOTHESIS (owner's formulation, 2026-09-03)

100 percent of the CODE is in the written Torah — all 24 books. The
Mishnah and Talmud are designed to teach us how to code FROM the
written text. Their case rows are TEST DATA (and the shape of that
data teaches the input schema), possibly from a source distinct from
the written code — we write the code to ACCEPT that type of data but
never encode the data into the source; then we test by feeding the
data in and requiring the Mishnah's output.

Discipline: keep an open mind; the owner allows he could be wrong;
divergences reported at the same size as confirmations. The
classification for every Mishnah/Talmud cell examined:
- **CODE-IN-INK** — the mechanism is in the written 24 books
  (including visible in an EXECUTION elsewhere in the canon).
- **DATA/PARAMETER** — a quantity, threshold, list-membership, or
  configuration the written code accepts as input; candidate for the
  second channel (the tradition's own label for much of this class:
  "transmitted to Moses from Sinai").
- **MISSING CODE** — mechanism not found in the ink and not
  plausibly data: honest evidence AGAINST the hypothesis.

## CASE 1 — THE SABBATH LABORS (chosen as the HARDEST case)

Why this one: Mishnah Chagigah 1:8 itself says the Sabbath rules are
"mountains hanging by a hair — little Scripture and many laws." If
the tradition's own worst-case assessment is wrong — if the code is
actually in the ink — the hypothesis survives its strongest known
counterexample. The dense code: Mishnah Shabbat 7:2, the THIRTY-NINE
primary labors (avot melakhot), each with derivative subclasses.

The teacher's own pointer to where the code lives: Babylonian Talmud
Shabbat 49b — the labors correspond to the labors of the TABERNACLE;
and the written Torah itself juxtaposes the Sabbath command directly
onto the tabernacle work orders (Exodus 35:1-3: the Sabbath, with
KINDLING named, immediately before the work list — and Exodus
31:12-17, the Sabbath planted in the middle of the build
instructions). Reading the juxtaposition as an INDEX — "the
forbidden labor types are the work types enumerated in the build
you are about to read" — is the teacher teaching us where in the
code the list is defined.

So the mechanical experiment: for each of the 39, hunt the labor's
own root across the written 24 books — the tabernacle span first,
then the whole canon including the execution logs — with probe
discipline (a scan that can't find a planted known instance reports
nothing). Then classify.

### Experiment 1.1 — the 39 roots hunted across the canon
(running — results table below as they land)

### The execution logs identified going in (to be pulled at the row)
- Exodus 16 — THE FIRST RECORDED RUN of the Sabbath machine: the
  double portion, day-6 baking and boiling ordered in advance, the
  failed gathering on day 7, and 16:29's domain instruction ("let no
  man go out of his place").
- Numbers 15:32-36 — the wood-gatherer: a labor case executed to
  verdict, with a custody-pending-ruling step.
- Jeremiah 17:21-27 — the carrying re-statement citing its source.
- Nehemiah 13:15-22 — treading presses, loading, selling: an
  enforcement sweep naming multiple labor types in commercial run.
- Amos 8:5 — the market halting ("when will the Sabbath be gone,
  that we may set forth wheat?").
- Isaiah 58:13 — the business-and-speech layer.

### The data-channel prediction (to test after 1.1)
If the owner's split is right, the parts of the Sabbath corpus the
tradition marks as transmitted-not-derived should cluster as
QUANTITIES — the minimum amounts per labor (the food-bulk, the
thread-lengths, the two-letters/two-threads/two-stitches
thresholds), the 2000-cubit domain radius. Labor TYPES = code in
ink; labor THRESHOLDS = data. To be checked against the Mishnah's
own quantity chapters (Shabbat 7:3-8:7).

---

## FINDINGS — sitting of 2026-09-03

### Experiment 1.1 RESULT: 36 of 36 scannable labors have canon ink

The full scan ran (scratchpad scan_39_labors.py; every probe fired —
36/36 — before any result was trusted). Of the 39 rows of Mishnah
Shabbat 7:2:

- **36 labor-roots are attested in the written 24 books.** Highlights
  by where the ink sits:
  - IN THE SABBATH COMMANDS THEMSELVES: kindling (Exodus 35:3 — "you
    shall kindle no fire in all your dwellings"); plowing AND reaping
    (Exodus 34:21 — "in plowing and in harvest you shall rest");
    carrying-out via the domain rule (Exodus 16:29).
  - IN THE TABERNACLE BUILD NARRATIVE (the index target): dyeing (6
    hits — the rams' skins DYED red, Exodus 25:5 on), spinning
    (Exodus 35:25 — "every wise-hearted woman SPUN"), weaving (the
    weaver on the staffing list, 35:35), writing (8), slaughtering
    (4), demolishing, kindling, carrying (17).
  - IN EXECUTIONS ACROSS THE CANON: baking + boiling in the FIRST
    RECORDED RUN (Exodus 16:23 — "what you would bake, bake; what
    you would boil, boil," prep moved to day six); gathering as the
    capital case (Numbers 15:32 — מקשש עצים "gathering wood");
    grinding in the manna run (Numbers 11:8); sheaf-binding in
    Joseph's dream; winnowing by Boaz at night; kneading in
    Jeremiah 7:18; sewing as the canon's FIRST human labor (Genesis
    3:7 — fig leaves); erasing inside a written procedure (the
    sotah scroll, Numbers 5:23); the smith's hammer (Isaiah 41:7).
- **2 rows are technical loom-operations with no biblical lemma**
  (making the two loops; separating threads) — the honest residue,
  discussed below.
- **1 row is the tradition's own count-note** (salting/tanning
  doubled; the gemara itself records the fix — Shabbat 75b).
- Thinnest verb-match: SELECTING (the root at Ezekiel 20:38 carries
  the sense of sorting-out persons, not produce) — recorded as thin.

### Experiment 1.2: the INDEX RULE is the teacher's pointer, and the pointer's anchor is ink

Babylonian Talmud Shabbat 49b:7, pulled at the row: "They correspond
to the labors in the Tabernacle. All types of labor performed in the
Tabernacle are enumerated as primary categories... other labors,
EVEN IF SIGNIFICANT, are NOT enumerated, since they were not
performed in the Tabernacle." That is a DEFINITION BY REFERENCE: the
39 are not a free list; they are an INDEX into the tabernacle build
narrative — which is written code (Exodus 25–40, fully derived in
this project). And the linkage itself sits in the ink: the written
text plants the Sabbath command INSIDE the build orders (31:12-17)
and again as the HEADER of the work session (35:1-3, with kindling
named on the spot) — the juxtaposition the teacher reads
definitionally, by a published reading rule. The second recorded
derivation of the same constant — the labor-word count over the
written Torah, "forty minus one" (Shabbat 49b), with Rav Yosef's
recorded uncertainty — ALSO operates entirely on the written text.
Both recorded routes to "39" run through the ink.

### Experiment 1.3: the DATA CHANNEL is self-labeled, in the tradition's own words

Pulled at the rows: "Rabbi Chiyya bar Ashi said that Rav said: THE
MEASURES... are halakhot transmitted to Moses from Sinai" (Eruvin
4a:10; again at Sukkah 5b:13 with the examples — olive-bulk,
fig-bulk, egg-bulk). And the Mishnah's own quantity chapters are
parameter tables, nothing else: straw = a cow's mouthful (Shabbat
7:4), wine = enough to dilute a cup (8:1), the two-threads /
two-stitches / two-letters thresholds inside the 39 list itself.
THE OWNER'S PREDICTED SPLIT LANDS EXACTLY: the labor TYPES are code
(indexed to the written build); the QUANTITIES are data — and the
tradition itself files the quantities under a separate, transmitted
channel. The "yet unknown source" of the test data has a recorded
name.

### The residue, examined honestly

The two loom rows (loops, thread-separating) are operations INSIDE
weaving — subclass-grain craft detail under a category (weaving)
that is solidly in the tabernacle ink. Note also that both carry
their quantity on their face ("TWO loops," "weaving TWO threads") —
the threshold half of each row is data by the measures rule above.
Verdict for now: not clean counterexamples to the hypothesis, but
not claimed as ink either — logged as OPEN, category-covered,
operation-level residue.

### CASE 1 PRELIMINARY VERDICT

On the tradition's own declared worst case ("a mountain hanging by
a hair"), the structure decomposes exactly as the hypothesis
predicts: one general prohibition in ink + a category list DEFINED
BY REFERENCE to the written build narrative (the reference readable
in the ink's own juxtaposition) + 36 of 38 distinct categories
attested by root across the canon, many inside the tabernacle span
or the Sabbath commands themselves + a rich execution log across
Torah, Prophets, and Writings + the quantities self-labeled by the
tradition as a separate transmitted DATA channel. Residue: two
loom-internal operations and one thin verb. The mountain hangs by
considerably more than a hair — most of its mass is in the written
text, and what is not looks like data, not code.

---

## CASE 2 — THE SECOND PASSOVER (code, execution, parameter — complete in one law)

Chosen because it exhibits the whole hypothesis in miniature, with a
NATIONAL-scale execution.

**THE CODE (Numbers 9:10-11, pulled at the ink):** written in the
same case syntax measured in the compiler work — אִישׁ אִישׁ כִּי
יִהְיֶה טָמֵא לָנֶפֶשׁ אוֹ בְדֶרֶךְ רְחֹקָה ("any man WHEN he is impure
by a corpse OR on a distant journey") — a when-case with an
or-branch, two input conditions, one output: defer to the second
month, fourteenth day, same statutes (with matzah and bitter herbs).
Complete mechanism, in ink.

**THE EXECUTION (2 Chronicles 30, pulled at the ink):** Hezekiah,
the princes, and the whole assembly "resolved to keep the Passover
IN THE SECOND MONTH, for they could not keep it at that time — the
priests had not sanctified themselves in sufficient number and the
people had not gathered" (30:2-3): the deferral branch invoked at
national scale, reason logged. Then the exception: most of the
northern tribes "had not purified themselves, and ate the Passover
בְּלֹא כַכָּתוּב — NOT AS WRITTEN" (30:18) — **the execution log
itself citing the written code as the standard deviated from** —
resolved out-of-band by Hezekiah's prayer, "and the LORD healed the
people" (30:20). And the teaching layer AUDITS this very run:
Babylonian Talmud Sanhedrin 12b:10 (pulled) — "Hezekiah requested
compassion BECAUSE he encouraged the people to perform the second
Pesach; what were the circumstances..." — the run reviewed as an
edge case, in the record.

**THE DATA (Mishnah Pesachim 9:2, pulled):** "What is a DISTANT
JOURNEY? From Modiim and beyond — Rabbi Akiva; from the threshold
of the Temple courtyard — Rabbi Eliezer." The code says
distant-journey; the THRESHOLD VALUE is a parameter — and the
tradition preserves TWO recorded settings of it, names attached.
The test data (Mishnah Pesachim 9's rows: who defers, what differs
between the two Passovers) is exactly the input-vector material the
owner's design wants fed at test time, never encoded.

### CASE 2 VERDICT
Code 100% in ink (the mechanism, in the measured case syntax);
execution logged at national scale WITH a written-code
self-reference and a recorded audit; the one fuzzy predicate
(distance) parameterized by data with two recorded values. The
hypothesis holds without remainder on this law.

---

## QUEUE (next sittings)
- CASE 3: court/acquisition procedure — Ruth 4 as the civil-procedure
  transcript (gate, quorum, refusal, sandal, acquisition); Naboth as
  the corrupt run (already catalogued); Jeremiah 26's precedent
  citation; grade against Mishnah Sanhedrin/Bava Batra rows as DATA.
- CASE 4: vows — the other "flies in the air" case; Jephthah as the
  catastrophic unhandled input; Numbers 30 as the code; Hannah's vow
  as a clean run.
- THE BUILD IMPLICATION to draft after case 3: the Torah-only
  machine w/ strict code/data separation — code from ink, input
  schema learned from the Mishnah's case-shape, Mishnah rows fed as
  test data at runtime only.

---

# THE FULL EXPLANATION — every verse quoted in full
(added 2026-09-03 at the owner's ask: "cite every verse in full, I
have no idea what you are referring to in the summary explanations")

## The law this research established (owner-ruled 2026-09-03)

**THE CODE/DATA SEPARATION LAW: this is the process for writing the
logic per verse — WITHOUT the data.** The source code of every
derived law comes only from the written 24 books. The Mishnah and
Talmud teach us HOW to write that code and what SHAPE of input it
must accept — but their case rows and quantities are TEST DATA, fed
in at run time and never written into the source. The test:
input the Mishnah's case, require the Mishnah's verdict as output.

## CASE 1, verse by verse — the Sabbath

**The base prohibition and the actor schema — Exodus 20:9-10:**
ששת ימים תעבד ועשית כל מלאכתך — "Six days you shall labor and do
all your work." ויום השביעי שבת ליהוה אלהיך לא תעשה כל מלאכה אתה
ובנך ובתך עבדך ואמתך ובהמתך וגרך אשר בשעריך — "And the seventh day
is a Sabbath to the LORD your God: you shall not do ANY WORK — you,
and your son, and your daughter, your manservant, and your
maidservant, and your animal, and your stranger who is within your
gates." What this gives the code: the general prohibition (no
melakhah, "work") and the complete ACTOR LIST — self, children,
servants, animals, resident strangers. That list is the input
schema's first column: who the rule binds.

**The death statute, planted inside the tabernacle build orders —
Exodus 31:15:** ששת ימים יעשה מלאכה וביום השביעי שבת שבתון קדש
ליהוה כל העשה מלאכה ביום השבת מות יומת — "Six days shall work be
done, and on the seventh day is a Sabbath of complete rest, holy to
the LORD; WHOEVER DOES WORK on the Sabbath day shall surely be put
to death." Note where this verse sits: in the middle of the
instructions for building the tabernacle (Exodus 31:12-17). The
written text itself splices the Sabbath law into the build project.

**The header of the work session, with one labor named on the spot —
Exodus 35:2-3:** ששת ימים תעשה מלאכה וביום השביעי יהיה לכם קדש שבת
שבתון ליהוה כל העשה בו מלאכה יומת — "Six days shall work be done,
but on the seventh day there shall be for you a holy day, a Sabbath
of complete rest to the LORD; whoever does work on it shall be put
to death." And the next verse: לא תבערו אש בכל משבתיכם ביום השבת —
"You shall KINDLE NO FIRE in all your dwellings on the Sabbath
day." This is the opening of the assembly where Moses commissions
the tabernacle work (the work list follows immediately). So twice —
31:12-17 inside the orders, 35:1-3 as their header — the written
text binds the Sabbath prohibition to the tabernacle work. That is
the ink anchor for the teacher's index rule (Babylonian Talmud
Shabbat 49b, pulled earlier in this log): the forbidden labor
CATEGORIES are the work categories of the build. And one category —
kindling — is named right there in the command itself.

**Two more labors named in a Sabbath command — Exodus 34:21:**
ששת ימים תעבד וביום השביעי תשבת בחריש ובקציר תשבת — "Six days you
shall work, and on the seventh day you shall rest; IN PLOWING and
IN HARVEST you shall rest." Plowing and reaping, by name, in ink.

**The first recorded run of the machine — Exodus 16.** Verse 23
(pulled earlier in full): "...bake what you will BAKE, and boil
what you will BOIL" — baking and cooking commanded to happen on day
six, i.e., forbidden on day seven: two labor categories visible in
the run's own scheduling. Verse 27: ויהי ביום השביעי יצאו מן העם
ללקט ולא מצאו — "And it came to pass on the seventh day, some of
the people WENT OUT TO GATHER, and they found none" — the failed
run, logged: gathering attempted on the Sabbath, error recorded.
Verse 29: "...remain every man in his place; LET NO MAN GO OUT OF
HIS PLACE on the seventh day" — the domain machinery (the
going-out/carrying boundary) in the run's own instruction.

**The capital case, and the run PAUSING on unspecified code —
Numbers 15:32-35:** ויהיו בני ישראל במדבר וימצאו איש מקשש עצים ביום
השבת — "And the children of Israel were in the wilderness, and they
found a man GATHERING WOOD on the Sabbath day." ויקריבו אתו
המצאים אתו... אל משה ואל אהרן ואל כל העדה — "And those who found
him gathering wood brought him to Moses and Aaron and all the
congregation." ויניחו אתו במשמר כי לא פרש מה יעשה לו — "And they
placed him in custody, BECAUSE IT HAD NOT BEEN SPECIFIED what
should be done to him." ויאמר יהוה אל משה מות יומת האיש רגום אתו
באבנים כל העדה מחוץ למחנה — "And the LORD said to Moses: the man
shall surely be put to death; all the congregation shall stone him
with stones outside the camp." Read it as an engineer: a case
arrives, the handler is UNSPECIFIED, the system holds the case in
custody, the specification is requested and ARRIVES, the case
executes. The written Torah records its own patch-request protocol
— and not once: the same custody-pending-specification structure
appears at the blasphemer (Leviticus 24:12 — our Leviticus 24 call
site!), here at the wood-gatherer, at the second Passover (Numbers
9:8, below), and at the daughters of Zelophehad (Numbers 27:5).
Four recorded runtime code-requests.

**The tabernacle work-list ink — the index target.** Exodus 25:5:
וערת אילם מאדמים... — "and rams' skins DYED RED..." (dyeing, in the
materials list). Exodus 35:25: וכל אשה חכמת לב בידיה טוו ויביאו
מטוה את התכלת ואת הארגמן את תולעת השני ואת השש — "And every
wise-hearted woman SPUN with her hands, and they brought what they
had spun: the blue, and the purple, the scarlet, and the fine
linen" (spinning, executed in the build). Exodus 35:35: מלא אתם
חכמת לב לעשות כל מלאכת חרש וחשב ורקם... וארג — "He has filled them
with wisdom of heart to do every WORK of the CRAFTSMAN, and the
DESIGNER, and the EMBROIDERER... and the WEAVER" — the build's own
staffing verse naming the craft categories.

**The executions gallery across the 24 books** (each quoted in
full):
- Genesis 3:7 — ותפקחנה עיני שניהם... ויתפרו עלה תאנה ויעשו להם
  חגרת — "And the eyes of both were opened... and they SEWED fig
  leaves together and made themselves girdles." The first human
  labor in the canon is SEWING.
- Genesis 37:7 — והנה אנחנו מאלמים אלמים בתוך השדה — "Behold, we
  were BINDING SHEAVES in the midst of the field..." (Joseph's
  dream: sheaf-binding executed).
- Ruth 3:2 — הנה הוא זרה את גרן השערים הלילה — "Behold, he
  WINNOWS the barley threshing-floor TONIGHT" (winnowing, with a
  timestamp).
- Numbers 11:8 — שטו העם ולקטו וטחנו ברחים או דכו במדכה ובשלו
  בפרור — "The people went about and GATHERED it, and GROUND it in
  mills or BEAT it in a mortar, and BOILED it in a pot" — four
  labors in one verse of the manna run.
- Jeremiah 7:18 — הבנים מלקטים עצים והאבות מבערים את האש והנשים
  לשות בצק — "The sons GATHER WOOD, and the fathers KINDLE THE
  FIRE, and the women KNEAD DOUGH" — three labor categories in a
  single verse (an idolatry indictment, but the labors named are
  the labors).
- Numbers 5:23 — וכתב את האלת האלה הכהן בספר ומחה אל מי המרים —
  "And the priest shall WRITE these curses in a scroll, and ERASE
  them into the water of bitterness" — writing AND erasing inside
  one written procedure.
- Isaiah 41:7 — ויחזק חרש את צרף מחליק פטיש את הולם פעם — "The
  craftsman strengthened the smith, the one who SMOOTHS WITH THE
  HAMMER him who strikes the anvil" — the hammer-finishing craft.
- Jeremiah 17:21-22 — כה אמר יהוה השמרו בנפשותיכם ואל תשאו משא
  ביום השבת והבאתם בשערי ירושלם — "Thus says the LORD: guard
  yourselves, and CARRY NO BURDEN on the Sabbath day, nor bring it
  in through the gates of Jerusalem." ולא תוציאו משא מבתיכם ביום
  השבת וכל מלאכה לא תעשו... כאשר צויתי את אבותיכם — "And CARRY NO
  BURDEN OUT OF YOUR HOUSES on the Sabbath day, and do no work —
  ...AS I COMMANDED YOUR FATHERS." The prophet re-states the
  carrying law and cites its source in the written code.
- Nehemiah 13:15 (pulled in full earlier in this log): "treading
  winepresses on the Sabbath, bringing in heaps, LOADING donkeys —
  and also wine, grapes, figs, and EVERY BURDEN, brought into
  Jerusalem on the Sabbath day..." — and 13:19: ויהי כאשר צללו שערי
  ירושלם לפני השבת... ויסגרו הדלתות — "And when the gates of
  Jerusalem grew dark before the Sabbath, I commanded that the
  doors be SHUT... that no burden enter on the Sabbath day" — the
  enforcement run: gates closed, guards posted.
- Amos 8:5 (pulled in full earlier): the merchants asking "when
  will the Sabbath be gone, that we may open the grain" — the
  market halting because the machine is running.

**And the data channel, in the tradition's own words** (pulled at
the rows, quoted in the findings above): "THE MEASURES... are
halakhot transmitted to Moses from Sinai" (Babylonian Talmud Eruvin
4a; Sukkah 5b adds the examples — olive-bulk, fig-bulk, egg-bulk).
The Mishnah's quantity rows — straw = a cow's mouthful (Shabbat
7:4), wine = enough to dilute a cup (8:1) — are parameter tables.
The labor TYPES live in the verses above; the AMOUNTS live in a
separately-transmitted data channel, by the tradition's own label.

## CASE 2, verse by verse — the second Passover

**The triggering case — Numbers 9:6-7:** ויהי אנשים אשר היו טמאים
לנפש אדם ולא יכלו לעשת הפסח ביום ההוא — "And there were men who
were impure by a human corpse, and they could not perform the
Passover on that day, and they came before Moses and Aaron on that
day." אנחנו טמאים לנפש אדם למה נגרע — "We are impure by a human
corpse — WHY SHOULD WE BE DIMINISHED, not to offer the LORD's
offering at its appointed time among the children of Israel?" A
live input arrives that the code as-published does not handle, and
the affected users file the case themselves.

**The query — Numbers 9:8:** ויאמר אלהם משה עמדו ואשמעה מה יצוה
יהוה לכם — "And Moses said to them: STAND, AND I WILL HEAR what
the LORD commands concerning you." The runtime code-request,
verbatim — the same protocol as the wood-gatherer and the
blasphemer.

**The code arrives — Numbers 9:10-11** (pulled in full earlier in
this log): "Any man WHEN he is impure by a corpse OR on a distant
journey — he shall perform the Passover to the LORD in the SECOND
month, on the fourteenth day at twilight; with unleavened bread and
bitter herbs they shall eat it." A when-case with an or-branch: two
input conditions, one deferral output, same statutes.

**The else-branch — Numbers 9:13:** והאיש אשר הוא טהור ובדרך לא
היה וחדל לעשות הפסח ונכרתה הנפש ההוא מעמיה — "But the man who is
PURE, and was NOT on a journey, and refrains from performing the
Passover — that soul shall be cut off from its people..." The
negative branch closed explicitly: no free deferral for the
unqualified.

**The national execution — 2 Chronicles 30:2-3** (pulled in full
earlier): the king, the princes, and the whole assembly "resolved
to keep the Passover IN THE SECOND MONTH, for they could not keep
it at that time — the priests had not sanctified themselves in
sufficient number, and the people had not gathered to Jerusalem."
The deferral branch invoked at the scale of the kingdom, reason
logged. **The exception — 30:18:** "a multitude of the people...
had not purified themselves, and ate the Passover בְּלֹא כַכָּתוּב —
NOT AS WRITTEN — for Hezekiah prayed for them, saying: may the good
LORD atone for..." — the run's own log citing THE WRITTEN CODE as
the standard it deviated from, with an out-of-band resolution.
**30:20:** וישמע יהוה אל יחזקיהו וירפא את העם — "And the LORD
listened to Hezekiah and HEALED the people." And the teaching layer
audits this very run (Babylonian Talmud Sanhedrin 12b, pulled):
"Hezekiah requested compassion because he encouraged the people to
perform the second Pesach — what were the circumstances..."

**The parameter — Mishnah Pesachim 9:2** (pulled): "What is a
DISTANT JOURNEY? From Modiim and beyond — Rabbi Akiva; from the
threshold of the Temple courtyard and beyond — Rabbi Eliezer." The
code's predicate, parameterized; two recorded settings, names
attached. Data, not code — exactly as the law of this research
requires.

---

## CASE 3 — THE COURTS, WITH RUTH 4 AS THE TRANSCRIPT
(sitting of 2026-09-03, continued; every verse in full)

**The installation command — Deuteronomy 16:18:** שפטים ושטרים תתן
לך בכל שעריך אשר יהוה אלהיך נתן לך לשבטיך ושפטו את העם משפט צדק —
"JUDGES AND OFFICERS you shall appoint for yourself IN ALL YOUR
GATES which the LORD your God gives you, tribe by tribe; and they
shall judge the people with righteous judgment." The court system's
installation order: the office (judges), the enforcement arm
(officers), the venue (the gates), the jurisdiction map (per
tribe), the quality spec (righteous judgment).

**And the installation EXECUTED at kingdom scale — 2 Chronicles
19:5-8:** ויעמד שפטים בארץ בכל ערי יהודה הבצרות לעיר ועיר — "And he
[Jehoshaphat] APPOINTED JUDGES IN THE LAND, in all the fortified
cities of Judah, CITY BY CITY." ויאמר אל השפטים ראו מה אתם עשים כי
לא לאדם תשפטו כי ליהוה — "And he said to the judges: see what you
do, for you judge not for man but for the LORD, and He is with you
in the matter of judgment." וגם בירושלם העמיד יהושפט מן הלוים
והכהנים ומראשי האבות לישראל למשפט יהוה ולריב — "And also IN
JERUSALEM Jehoshaphat set of the Levites and the priests and the
heads of the fathers' houses of Israel, for the judgment of the
LORD and for disputes." Note the two-tier build: local courts city
by city, THEN the high court in Jerusalem — which is Deuteronomy
17:8-9's escalation protocol executed: כי יפלא ממך דבר למשפט...
וקמת ועלית אל המקום אשר יבחר יהוה — "WHEN A MATTER IS TOO HARD FOR
YOU in judgment, between blood and blood, between plea and plea,
between mark and mark — matters of dispute in your gates — you
shall arise AND GO UP to the place which the LORD your God shall
choose; and you shall come to the Levitical priests and to the
judge who shall be in those days, and inquire, and they shall
declare to you the word of judgment." The appellate route, in ink;
the appellate bench, installed in the run.

**The evidence rule — Deuteronomy 19:15:** לא יקום עד אחד באיש...
על פי שני עדים או על פי שלשה עדים יקום דבר — "One witness shall
not rise against a man for any iniquity or any sin... BY THE MOUTH
OF TWO WITNESSES OR BY THE MOUTH OF THREE WITNESSES shall a matter
be established." **The majority rule — Exodus 23:2:** לא תהיה אחרי
רבים לרעת ולא תענה על רב לנטת אחרי רבים להטת — "You shall not
follow a multitude to do evil, nor answer in a cause to turn aside
AFTER A MULTITUDE to pervert — " the clause the tradition reads for
majority-following in judgment (the very verse Rabbi Yehoshua
quoted back at heaven in Bava Metzia 59b).

**The bench sizes — and the answer sheet citing the ink for its own
constant.** Mishnah Sanhedrin 1:6, pulled at the row: "The Great
Sanhedrin was composed of SEVENTY-ONE... FROM WHERE is it derived?
As it is stated: 'GATHER ME SEVENTY MEN of the Elders of Israel'" —
and Moses over them. The written code (Numbers 11:16, pulled): אספה
לי שבעים איש מזקני ישראל — "Gather to Me SEVENTY MEN of the elders
of Israel... and they shall stand there WITH YOU." The Mishnah's
own text performs the derivation from the verse — the answer sheet
pointing at the code for its parameter. (The lesser court's 23 and
the monetary bench's 3 are reached by recorded composite arguments
— classified honestly as RECORDED-DERIVATION, thinner than direct
ink.) Mishnah Sanhedrin 1:1 (pulled): monetary cases — THREE
judges; the case-type → bench-size table is the data layer the
court code accepts.

**The court's address, found MECHANICALLY.** A canon-wide scan for
verses carrying both the gate-word (שער) and the elders-word (זקן)
returned EXACTLY SEVEN verses (probe fired at Deuteronomy 25:7
first): three CODE sites — Deuteronomy 21:19 (the rebellious son
"to the elders of his city, to the gate of his place"), 22:15 (the
defamed bride's parents "to the elders of the city, to the gate"),
25:7 (the levirate refusal, below); one PROCEDURE RUN — Joshua 20:4
(the manslayer at the refuge city "shall stand at the entrance of
the GATE of the city and speak his words in the ears of the ELDERS
of that city" — intake protocol executing); one TRANSCRIPT — Ruth
4:11 (below); one SHUTDOWN LOG — Lamentations 5:14: זקנים משער
שבתו — "THE ELDERS HAVE CEASED FROM THE GATE" — the courts going
down at the destruction, recorded in the log; and one PROVERB —
Proverbs 31:23 ("her husband is known in the gates, when he sits
among the ELDERS of the land" — the institution as a byword). Code,
run, transcript, outage report, and cultural echo — one scan.

**The refusal procedure — Deuteronomy 25:7-9, the code Ruth's court
runs beside:** ואם לא יחפץ האיש לקחת את יבמתו ועלתה יבמתו השערה אל
הזקנים — "And if the man does not desire to take his brother's
widow, then his brother's widow shall GO UP TO THE GATE, TO THE
ELDERS, and say: my husband's brother refuses to raise up for his
brother a name in Israel..." וקראו לו זקני עירו ודברו אליו ועמד
ואמר לא חפצתי לקחתה — "Then the elders of his city shall CALL HIM
and speak to him; and if he stands and says: I do not desire to
take her —" ונגשה יבמתו אליו לעיני הזקנים וחלצה נעלו מעל רגלו —
"then his brother's widow shall approach him IN THE SIGHT OF THE
ELDERS, and DRAW OFF HIS SHOE from his foot..." Venue, summons,
declaration on the record, and the shoe formality — in ink.

**THE TRANSCRIPT — Ruth 4, verse by verse:**
- 4:1 — ובעז עלה השער וישב שם והנה הגאל עבר... סורה שבה פה פלני
  אלמני — "And Boaz WENT UP TO THE GATE and sat there, and behold,
  the redeemer passed by... and he said: turn aside, sit here, such
  a one" — venue taken, the party summoned.
- 4:2 — ויקח עשרה אנשים מזקני העיר ויאמר שבו פה — "And he took TEN
  MEN OF THE ELDERS OF THE CITY and said: sit here." **The quorum
  parameter, in ink — the number ten.** And the tradition reuses
  this very verse as the source of the ten-man quorum for the
  grooms' blessing (the derivation runs at Babylonian Talmud
  Ketubot 7b — Rav Nachman from "Boaz assembled ten men," pulled at
  the row).
- 4:7 — וזאת לפנים בישראל על הגאולה ועל התמורה לקים כל דבר שלף איש
  נעלו ונתן לרעהו וזאת התעודה בישראל — "Now this was FORMERLY in
  Israel concerning redemption and exchange, TO CONFIRM every
  matter: a man drew off his shoe and gave it to his fellow; and
  this was the ATTESTATION in Israel." **The text documents its own
  legal formality, names its function (confirmation/attestation),
  and version-stamps it ("formerly") — a deprecation note inside
  the runtime log.**
- 4:9 — ויאמר בעז לזקנים וכל העם עדים אתם היום כי קניתי — "And Boaz
  said to the elders and all the people: YOU ARE WITNESSES THIS DAY
  that I have ACQUIRED all that was Elimelech's..." — the
  acquisition declared on the record, the witness rule invoked.
- 4:11 — ויאמרו כל העם אשר בשער והזקנים עדים — "And all the people
  who were in the gate, and the elders, said: WE ARE WITNESSES" —
  the record confirmed by the assembly, followed by the blessing.
Honest note: Ruth's case is the REDEEMER route (Leviticus 25:25 —
כי ימוך אחיך ומכר מאחזתו ובא גאלו הקרב אליו וגאל — "If your brother
becomes poor and sells of his possession, his REDEEMER who is near
to him shall come and redeem what his brother sold"), running
BESIDE the levirate code, not inside it — the shoe passes between
the men as the confirmation formality (per 4:7's custom note), with
no spitting and no brother. The transcript shows a related-but-
distinct procedure sharing the gate, the elders, the declaration,
and the shoe — the honest classification is: same court machinery,
different subroutine, with the custom layer version-stamped by the
text itself.

**THE ACQUISITION CODE AND ITS FULL RUNTIME PROTOCOL.**
- Money, at the gate — Genesis 23:16-18: וישקל אברהם לעפרן את הכסף
  ... ארבע מאות שקל כסף עבר לסחר — "And Abraham WEIGHED for Ephron
  the silver he had named in the hearing of the sons of Heth: four
  hundred shekels of silver, CURRENT WITH THE MERCHANT." ויקם שדה
  עפרון — "And the field of Ephron WAS ESTABLISHED" — the transfer
  verb — לאברהם למקנה לעיני בני חת בכל באי שער עירו — "to Abraham
  as an ACQUISITION, in the sight of the sons of Heth, before all
  who entered THE GATE of his city." Payment standard, public
  venue, effective transfer — in ink.
- The deed, executed step by step — Jeremiah 32:9-14: ואקנה את
  השדה... ואשקלה לו את הכסף — "And I BOUGHT the field... and
  WEIGHED him the money — seventeen shekels of silver." ואכתב בספר
  ואחתם ואעד עדים ואשקל הכסף במאזנים — "And I WROTE it in the DEED,
  and SEALED it, and CALLED WITNESSES, and weighed the money in the
  balances." ואקח את ספר המקנה את החתום המצוה והחקים ואת הגלוי —
  "And I took the deed of purchase — THE SEALED one, the terms and
  the conditions, AND THE OPEN one" — **two copies, sealed and
  open** — ונתתם בכלי חרש למען יעמדו ימים רבים — "and put them in
  an earthen vessel, THAT THEY MAY LAST MANY DAYS" — the durability
  requirement, stated in the run. Now the answer sheet: Mishnah
  Bava Batra 10:1 (pulled) — the ORDINARY document with witnesses
  inside versus the TIED document with witnesses on the back — the
  two-form deed doctrine whose runtime pair (open + sealed) is
  Jeremiah's transaction.
- The modes table: Mishnah Kiddushin 1:5 (pulled) — land by money,
  document, or possession; movables by pulling. And the teacher's
  own provenance split, at Bava Metzia 47b (pulled): **"BY TORAH
  LAW, money effects acquisition"** — and pulling is the Sages'
  enactment. The teaching layer itself separates the written-law
  mode from the enacted mode — our code/fence line, drawn in the
  tradition's own hand.

### CASE 3 VERDICT
The court's code is in the ink end to end: installation (Deut
16:18), venue and address (the seven-verse gate+elders set, found
mechanically), evidence threshold (Deut 19:15), majority clause
(Exod 23:2), escalation route (Deut 17:8-9), the refusal procedure
(Deut 25:7-9), and the acquisition modes with a complete deed
protocol visible in a single execution (Jeremiah 32). The
executions span the canon: Jehoshaphat's two-tier installation,
Joshua's intake, Ruth's full transcript with its ten-elder quorum
and version-stamped formality, Abraham's purchase, Jeremiah's deed,
Naboth's corrupt run, Jeremiah 26's precedent citation — and even
the SHUTDOWN is logged (Lamentations 5:14). The data layer:
bench-size table (71 ink-cited BY THE MISHNAH ITSELF from Numbers
11:16; 3 and 23 by recorded composite derivation), the quorum ten
(ink at Ruth 4:2, reused by the tradition), and one honest
self-labeled ENACTMENT (pulling, Bava Metzia 47b) — the fence
class, marked by the teacher exactly where the hypothesis expects
it. No missing-code residue found in this case.

QUEUE UPDATE: Case 4 (vows — Numbers 30 code; Jephthah the
unhandled input; Hannah the clean run) next; then the Torah-only
machine design.

---

## THE TEACHING FILE (2026-09-03, owner's ask: "Create an html
## training file... Show me how the verse becomes code")
LESSON ONE built: **How_A_Verse_Becomes_Code.html** (repo root, open
in any browser) + its runnable companion **passover_lesson.py** (repo
root — the code shown on the page verbatim). One example, complete:
the Second Passover. Seven steps: read the verses (all eight, Hebrew
+ English, including the runtime code-request story of Numbers
9:6-8); see the branch structure; write the code from ink only —
with THE GAP made explicit (the distance threshold declared as an
input parameter, never a constant, and the scroll's own dot over the
heh of רְחֹקָה "distant" flagging the word); read the ENTIRE Mishnah
(Pesachim 9:1-3, full text both languages, each row classified as
data); extract the data table; run the test — 5/5 under BOTH
recorded parameter settings, the Akiva/Eliezer dispute run as two
configurations of one code; the history log (2 Chronicles 30, "not
as WRITTEN"). REFINEMENT #1 kept on the page as a lesson: the first
run exposed two underspecified test cases ("in Jerusalem" is already
distant under Rabbi Eliezer's setting) — fixed in the DATA, code
untouched. The page is a living file; refinements at the owner's
word.

---

## THE CANTILLATION QUESTION — does the compiler need the accent tree?
(sitting of 2026-09-03, the owner's question: "do we even need the
cantillation tree to derive this code?" → "yes run the hunt")

Two prongs: the tradition's own records of parse-dependence, and a
mechanical measurement over the law code.

### Prong 1 — the tradition's own census of undecidable parses

Babylonian Talmud Yoma 52a:10 (pulled at the row): "Isi ben Yehuda
says: there are FIVE VERSES IN THE TORAH whose meaning CANNOT BE
DECIDED" — the tradition's complete list of grouping ambiguities.
The five, each pulled at its row (Yoma 52b:1-5):
1. שְׂאֵת ("lifted/borne") — Genesis 4:7, Cain — NARRATIVE.
2. מְשֻׁקָּדִים ("almond-blossomed") — Exodus 25:34, which menorah
   parts the ornament attaches to — TABERNACLE SPEC (a build
   detail; no verdict turns on it).
3. מָחָר ("tomorrow") — Exodus 17:9, the Amalek battle — NARRATIVE.
4. אָרוּר ("cursed") — Genesis 49:7, Jacob's blessing — POETRY.
5. וְקָם ("and he will rise") — Deuteronomy 31:16 — NARRATIVE.
**ZERO of the five are case law.** And the one recorded dispute the
Talmud itself resolves as "the punctuation of the cantillation
notes" (Mar Zutra, Chagigah 6b:13, pulled — whether the
burnt-offerings of Exodus 24:5 were sheep or cattle) is NARRATIVE
too — the covenant ceremony, not a case rule.

### Prong 2 — the mechanical measurement over the law code

Every branch/case keyword token (כִּי "when" and אִם "if", with
their and-forms) in Exodus 21:1-23:19 was located — 64 tokens — and
each classified by what precedes it:
- **44 of 64 stand at a VERSE BOUNDARY** (the maximal pause).
- **18 of 64 follow a PAUSE-CLASS (disjunctive) accent** — the
  accent layer AGREES with the keyword: the boundary is marked
  twice. Redundant encoding, not dependence.
- **2 of 64 follow a joining (conjunctive) accent — and both are
  COMPOUND KEYWORDS**: אַךְ אִם ("but if," Exodus 21:21) and כִּי
  אִם ("for if," 22:22), where the joining accent binds the two
  halves of the keyword itself. The accent here HELPS the parse of
  the keyword; it never obscures a branch boundary.
- **Zero cases anywhere** in the law code where finding a branch
  boundary requires consulting the accents against the words.

### VERDICT

**The compiler does not need the cantillation tree for the case-law
code — and both the tradition and the measurement say so.** The law
genre is written parse-unambiguous: branch structure is fully
carried by the keywords and the verse boundaries, with the accents
everywhere agreeing and nowhere deciding. The accent layer's real
recorded work lies where the tradition's own examples live —
narrative, poetry, and one spec-ornament grouping — serving the
READER (the public-reading aid its charter at Nehemiah 8:8 /
Megillah 3a describes) rather than the law compiler. This is itself
a design fact of the first importance for the 100-percent
hypothesis: THE CODE SECTIONS OF THE WRITTEN TORAH ARE ENGINEERED
FOR UNAMBIGUOUS MACHINE READING — the one genre that had to compile
is the one genre that never needs the parser to disambiguate.

Honest side-note kept with it: a DIFFERENT ink-layer flag DID prove
load-bearing for law this very day — the scribal DOT over the heh
of רְחֹקָה ("distant," Numbers 9:10), which Rabbi Yosei reads as
qualifying the parameter word (Mishnah Pesachim 9:2). Dots
(puncta), not accents: the scroll's point-flags mark semantic
qualifications, while the accents mark reading structure. Two
different annotation channels, two different jobs.

---

## THE DOT CHANNEL (2026-09-03, the owner's hunch: "maybe that mark
## is used elsewhere for the same reason")

The mark over the heh of רְחֹקָה ("distant," Numbers 9:10) is NOT a
cantillation accent — it is a scribal DOT, its own annotation
channel (its own codepoint in our text layer, distinct from the
whole accent range). The owner guessed it recurs with the same
function. CONFIRMED, exactly:

**The machine scan matched the tradition's enumeration to the
verse.** A canon-wide scan for the upper dot found FIFTEEN dotted
sites: TEN in the Torah — Genesis 16:5, 18:9, 19:33, 33:4 (Esau's
kiss, every letter dotted), 37:12; Numbers 3:39, 9:10 (ours), 21:30,
29:15; Deuteronomy 29:28 (eleven dots across two words) — and five
beyond: 2 Samuel 19:20, Isaiah 44:9, Ezekiel 41:20 and 46:22, Psalm
27:13. And the tradition's own record (Avot DeRabbi Natan 34:5,
pulled): "IN TEN PLACES in the Torah [words or letters] have dots
over them" — the closed list, matching the scan count exactly.

**The flag's meaning, per the teacher — a QUALIFICATION on the
dotted ink.** Three recorded expoundings pulled at the rows:
- Numbers 9:10 — the dotted heh of "distant": "not because he is
  truly distant" (Rabbi Yosei, Mishnah Pesachim 9:2) — a PARAMETER
  QUALIFIED.
- Numbers 3:39 — "the vav in ve-Aharon is dotted BECAUSE AARON WAS
  NOT PART OF THE CENSUS" (Bamidbar Rabbah 3:13) — an OPERAND
  EXCLUDED FROM A COUNT: the census total computes correctly only
  with the dotted name left out. A counting instruction, in a dot.
- Deuteronomy 29:28 — "WHY in a Torah scroll are there dots over
  each of the letters in the words 'to us and to our children'?"
  (Sanhedrin 43b:10-11) — the scope of collective liability
  QUALIFIED, with the dispute over the qualification recorded.

**What this adds to the front end.** The compiler's front-end
inventory grows by one small, closed element: letters, words,
roots, verse cuts — AND THE FIFTEEN DOTS, each a semantic-
qualification flag on its word, each with a recorded expounding in
the teacher layer. Unlike the accent tree (reader-service,
never law-deciding), the dot channel IS law-relevant — at least
three of the fifteen qualify parameters, counts, or liability
scope. The two-channel picture sharpens: ACCENTS mark reading
structure for people; DOTS mark semantic qualifications for the
law — and the dots are few, enumerated, and fully covered by
recorded teachings. The written code's own footnote system.

### The dot channel, checked site by site (owner: "are the other
### dots used in the mishnah talmud the same way?")

YES — every site checked carries a recorded expounding of the same
type: a QUALIFICATION of the dotted ink. Verified at pulled rows
this sitting (beyond the three already logged):
- Genesis 18:9 — Bava Metzia 87a:8: "Why are there dots upon the
  letters aleph, yod, vav [of 'to him']?" — the visitors' question
  redirected (they asked after Abraham too) — the addressee
  qualified.
- Genesis 19:33 — Nazir 23a:18: the dot over the vav of "and when
  she arose" — he DID know when she arose — the verse's "he knew
  not" QUALIFIED, and Lot's culpability for the second night
  established BY THE DOT. A liability verdict riding a single dot.
- Genesis 33:4 — Bereshit Rabbah 78:9: Esau's fully-dotted kiss —
  its sincerity the recorded dispute.
- Genesis 37:12 — Bereshit Rabbah 84:13: the dotted object-marker
  et — "they went to herd THEMSELVES" — the grammatical OBJECT
  CANCELLED by the dot.
- Psalm 27:13 — Berakhot 4a:14: David's dotted "if I had not
  [believed]" — his certainty qualified: doubt encoded.
- Genesis 16:5 and Numbers 29:15 — covered in the tradition's own
  site-by-site walk (Avot DeRabbi Natan 34:5 enumerates the ten
  Torah sites one by one with an expounding each).
Not individually verified this sitting: Numbers 21:30 and the four
beyond-Torah sites other than the Psalm (2 Samuel 19:20, Isaiah
44:9, Ezekiel 41:20, 46:22) — the ten-in-the-Torah census is the
teacher's own; the remainder queued.

**THE PROCESSING RULE — the channel has an algorithm, stated.**
Rabbi Shimon ben Elazar (Bereshit Rabbah 78:9, pulled): "Every
place you find the SCRIPT more numerous than the DOTS, you expound
the script; the DOTS more numerous than the script, you expound the
dots" — and at Esau's kiss, where dots equal script letter for
letter, the equal case gets its own recorded treatment (the
dispute). Compare the dotted-letter count to the undotted; the
majority channel receives the expounding. A counting rule over an
annotation layer — the teacher documenting HOW to process the dots,
not just what each one means. The dot channel is thus complete on
all three levels the compiler needs: a closed site list (15,
machine-verified against the tradition's census), a per-site
recorded expounding (qualification, in every checked case), and a
stated processing algorithm.

### The left/right seam, measured (owner: "the logic we found in the
### left right tree — statement and outcome? Does that apply?")

Measured over the case law (Exodus 21:2-22:16): of the 20
case-opener verses carrying both an etnachta (the top split) and a
verdict-class token, in **17 the verdict stands RIGHT of the split**
— the top cut lands on the condition‖outcome seam. The 3 exceptions
are instructive, not damning: 21:20's verdict ("he shall be
avenged") uses a verb outside the scan's verdict set and its
death-verb is the EVENT, not the sentence; 22:1's verdict is a
NOMINAL clause ("no bloodguilt for him") with no verdict verb at
all; and 22:14 is a TWO-CASE verse where the etnachta separates
case‖case rather than condition‖outcome. VERDICT: the
statement→outcome reading of the top split is real and strong in
case law — but it is REDUNDANT marking, like indentation agreeing
with braces: the seam is recoverable from the keywords and syntax
alone, and the accent split confirms it. Its compiler role is a
LINT (a disagreement between keyword-structure and accent-split is
a flag worth inspecting) and a display layer (the units'
tree_left/tree_right), never a derivation dependency.


---

## THE NARRATIVE MEASUREMENT — does the world machine need the accent tree?
## (2026-09-03, owner: "I still think we need the cantillation marks to
## derive the narrative am I wrong? ... Could we do that without the marks?"
## → "yes measure it on the creation week. use the oral torah where needed")

### The instrument

The seven frozen creation-week units (gen_01_creation_boot through
gen_07_completion_sanctity, Genesis 1:1–2:3, all FULL RULE) carry
**131 operators** — every derived world fact of the week: events,
states, declarations, namings, registry writes, tests, blessings,
spec-deltas, witness states, utterance-census entries. Each operator
was read and classified by the MINIMAL front-end layer that decides
its content:

- **W** — words alone: roots, word order, letter-visible spelling,
  formula tokens (וַיְהִי־כֵן "and it was so", וַיִּקְרָא "and he
  called", וַיְבָרֶךְ "and he blessed"), presence/absence of אֵת (the
  object marker), the day labels, verse cuts.
- **M** — words + morphology: the verb-form layer — jussive vs
  imperfect vs narrative-past vs perfect vs participle (the whole
  LET / LET? / event / state mood system), verb stems, gender and
  number agreement (the earth as build agent at 1:12 rides the
  feminine verb), pronominal suffixes.
- **P** — paragraph breaks needed as the deciding layer.
- **T** — the accent tree as the deciding witness.
- **O** — oral testimony is the content's source (the ink never says
  it): the ten-utterances census, the witness states (the hidden
  light, the suspended waters, the sea's stipulation, the moon's
  diminution, the staged grasses, the curtailed great creatures, the
  Torah-acceptance condition, rest-created-on-day-seven), the
  recorded census disputes, and Genesis 1:1's time anchor (below).

### THE NUMBERS

| unit | ops | W | M | O | T | P |
|---|---|---|---|---|---|---|
| creation_boot (1:1–5) | 18 | 5 | 8 | 5 | 0 | 0 |
| raqia_day (1:6–8) | 12 | 5 | 5 | 2 | 0 | 0 |
| double_build (1:9–13) | 20 | 11 | 5 | 4 | 0 | 0 |
| lights_calendar (1:14–19) | 20 | 11 | 4 | 5 | 0 | 0 |
| swarms_blessing (1:20–23) | 18 | 10 | 5 | 3 | 0 | 0 |
| land_adam_dominion (1:24–31) | 36 | 24 | 8 | 4 | 0 | 0 |
| completion_sanctity (2:1–3) | 7 | 3 | 3 | 1 | 0 | 0 |
| **WEEK** | **131** | **69 (53%)** | **38 (29%)** | **24 (18%)** | **0** | **0** |

**Zero of 131 facts has the accent tree as its sole deciding
witness.** The tree appears in the operator prose at exactly SIX
sites — 1:4 (the כִּי "that" ruling sits "under the etnachta arm"),
1:16 (the etnachta "stages" the both-great-then-split delta), 1:24
(the receipt token isolated as the right arm), 1:29 and 1:30 (the
food-grant demand and its receipt as right arms), 2:2 (the mirrored
[finished | ceased] halves) — and at every one of them it CONFIRMS
a fact already decided by words, morphology, or syntax. The
narrative verdict matches the case-law verdict exactly:
**corroboration, never derivation.**

### The paragraph finding — the day boundaries are INK

Measured in the source XML: **seven open-paragraph marks (פ —
petuchah, "open paragraph"), one at the close of each day** — after
1:5, 1:8, 1:13, 1:19, 1:23, 1:31, and 2:3. The scroll's own layout
segments the week into exactly seven paragraphs. In this span the
words already carry the boundary (the evening-morning refrain), so
the paragraph layer is redundant here — but unlike the accents, the
paragraph marks ARE in the scroll a scribe must write. Where a
narrative lacks a refrain, this is the ink's own scene divider.

### Exhibit 1 — the week's ONE real parse ambiguity, and who decided it

בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ
— "In the beginning God created the heavens and the earth"
(Genesis 1:1).

The bare consonants allow two readings: the absolute ("In the
beginning, God created...") or the construct ("In the beginning OF
God's creating..." — a dependent clause, no absolute origin). This
is a genuine attachment ambiguity, it affects a world variable (is
t0 an absolute timeline origin?), and the accents COULD have been
called as a witness. The derivation instead reached for the
teacher: the unit's TIME_ANCHOR is ruled temporal by Onkelos —
בְּקַדְמִין ("at the first") — and the tradition's own testimony at
Babylonian Talmud Megillah 9a records the elders changing the word
order for King Ptolemy ("God created in the beginning") to guard
against misreading. The one place narrative parse ambiguity was
real, ORAL TESTIMONY decided it — the accents were not even called.
Exactly the owner's instruction: "use the oral torah where needed."

### Exhibit 2 — the tree's best narrative moment, still redundant

וַיַּ֧רְא אֱלֹהִ֛ים אֶת־הָא֖וֹר כִּי־ט֑וֹב וַיַּבְדֵּ֣ל אֱלֹהִ֔ים
בֵּ֥ין הָא֖וֹר וּבֵ֥ין הַחֹֽשֶׁךְ — "And God saw the light, that it
was good; and God divided the light from the darkness" (Genesis 1:4).

Is כִּי here "that" (a complementizer — He saw THAT it was good) or
casuistic "if/when" (the law books' branch keyword)? The unit rules
complementizer, noting it sits under the etnachta arm with the
seeing. But the decider is syntax available from words + morphology:
כִּי directly after a verb of perception (וַיַּרְא "and he saw") is
"that" — the accent grouping agrees, the way indentation agrees
with braces. Corroboration.

### Exhibit 3 — the week's hardest reading problem is not a parse problem

וַיְכַ֤ל אֱלֹהִים֙ בַּיּ֣וֹם הַשְּׁבִיעִ֔י מְלַאכְתּ֖וֹ אֲשֶׁ֣ר
עָשָׂ֑ה וַיִּשְׁבֹּת֙ בַּיּ֣וֹם הַשְּׁבִיעִ֔י מִכׇּל־מְלַאכְתּ֖וֹ
אֲשֶׁ֥ר עָשָֽׂה — "And God finished on the seventh day His work
which He had made; and He ceased on the seventh day from all His
work which He had made" (Genesis 2:2).

Finished ON the seventh day — after 1:31's global inspection closed
the sixth? No accent placement can dissolve this; the words say it
plainly, twice. The tradition's answer is testimony, not parsing:
what the world still lacked, the seventh day itself supplied —
מְנוּחָה ("rest"), the bride for the canopy (Bereshit Rabbah 10:9;
the unit's witness state). The deep narrative problems of the week
live ABOVE the parse layer entirely.

### Two honest caveats

1. **The tree WAS the workbench.** The units' method field is named
   tree_derive_version — a fossil of the era when derivation was
   organized arm-by-arm — and each step's operators are grouped
   under tree_left/tree_right displays. The carving TABLE was the
   tree; the carved FACTS, measured one by one, never needed it as
   a witness. Rebuilt without accents, the step boundaries might
   fall differently; the 131 facts would not change.
2. **"Without the marks" ≠ "without the reading tradition."** 29% of
   the week's facts (38 of 131) are decided by MORPHOLOGY — the
   mood system (jussive LET vs imperfect LET?), the narrative-past
   event chain, gender agreement handing the earth her delegated
   build. Morphology as we consume it bakes in the vowels, which
   are the reading tradition's other half. The claim this
   measurement supports is precise: the ACCENTS are testimony and
   lint; the VOWELS-AND-GRAMMAR layer is load-bearing for
   narrative in a way it never was for case law (case law rode the
   branch keywords; narrative rides the verb forms).

### VERDICT

The owner asked: "I still think we need the cantillation marks to
derive the narrative — am I wrong?" Measured answer: **we USED them
(workbench + display), we do not NEED them (0 of 131 facts)** — the
world's states and variables come from words and roots (53%), the
verb-form layer (29%), and the teacher's testimony where the ink is
silent (18%), with the scroll's own paragraph marks as the ink-level
scene divider. The narrative front end is therefore: letters, words,
roots, verse cuts, paragraph breaks, the fifteen dots — plus the
GRAMMAR of the reading tradition (vowels/verb-forms) as narrative's
extra load-bearing layer, and the accent tree in the same seat it
holds in case law: the reader's aid, the redundancy lint, the
display.

### Appendix — the full per-operator classification (audit trail)

1:1 TIME_ANCHOR → O
1:1 EVENT → M
1:1 REGISTRY_INSTALL → W
1:1 ORAL_UTTERANCE → O
1:2 PRECONDITION_STATE → M
1:2 INVARIANT → M
1:2 NOTE_ZERO_EVENTS → M
1:2 NOTE_PRESUPPOSED → W
1:2 ORAL_UTTERANCE → O
1:3 ORAL_UTTERANCE → O
1:3 DECLARE → M
1:3 TRIPLE → M
1:3 RESULT → M
1:4 TEST → M
1:4 EVENT_PARTITION → W
1:4 WITNESS_STATE → O
1:5 NAME → W
1:5 COMMIT → W
1:6 ORAL_UTTERANCE → O
1:6 DECLARE → M
1:6 DECLARE → M
1:6 INVARIANT → M
1:6 NOTE_PRESUPPOSED → W
1:7 EVENT → M
1:7 EVENT_PARTITION → W
1:7 WITNESS_STATE → O
1:7 RESULT → W
1:7 RESULT → M
1:8 NAME → W
1:8 COMMIT → W
1:9 ORAL_UTTERANCE → O
1:9 DECLARE → M
1:9 DECLARE → M
1:9 NOTE_PRESUPPOSED → W
1:9 RESULT → W
1:9 RESULT → W
1:10 NAME → W
1:10 WITNESS_STATE → O
1:10 TEST → W
1:11 ORAL_UTTERANCE → O
1:11 DECLARE → M
1:11 INVARIANT → M
1:11 RESULT → W
1:12 EVENT → M
1:12 REGISTRY_INSTALL → W
1:12 NOTE_SPEC_DELTA → W
1:12 NOTE_SPEC_DELTA → W
1:12 WITNESS_STATE → O
1:12 TEST → W
1:13 COMMIT → W
1:14 ORAL_UTTERANCE → O
1:14 DECLARE → M
1:14 TRIPLE → M
1:14 NOTE_PRESUPPOSED → W
1:15 NOTE_PRESUPPOSED → W
1:15 RESULT → W
1:16 EVENT → M
1:16 REGISTRY_INSTALL → W
1:16 ASSIGN → W
1:16 NOTE_SPEC_DELTA → W
1:16 WITNESS_STATE → O
1:16 WITNESS_STATE → O
1:16 NOTE_SPEC_DELTA → W
1:16 WITNESS_STATE → O
1:16 NOTE_SPEC_DELTA → W
1:17 EVENT → M
1:17 WITNESS_READ → O
1:18 NOTE_SPEC_DELTA → W
1:18 TEST → W
1:19 COMMIT → W
1:20 ORAL_UTTERANCE → O
1:20 DECLARE → M
1:20 DECLARE → M
1:20 TRIPLE → W
1:20 NOTE_PRESUPPOSED → W
1:21 EVENT → M
1:21 ORAL_UTTERANCE → O
1:21 REGISTRY_INSTALL → W
1:21 RESULT → M
1:21 RESULT → W
1:21 NOTE_SPEC_DELTA → W
1:21 NOTE_SPEC_DELTA → W
1:21 WITNESS_STATE → O
1:21 NOTE_SPEC_DELTA → W
1:21 TEST → W
1:22 BLESS → M
1:22 NOTE_PRESUPPOSED → W
1:23 COMMIT → W
1:24 ORAL_UTTERANCE → O
1:24 DECLARE → M
1:24 TRIPLE → W
1:24 RESULT → W
1:24 NOTE_PRESUPPOSED → W
1:25 EVENT → M
1:25 REGISTRY_INSTALL → W
1:25 NOTE_SPEC_DELTA → W
1:25 NOTE_SPEC_DELTA → W
1:25 NOTE_SPEC_DELTA → W
1:25 TEST → W
1:26 ORAL_UTTERANCE → O
1:26 DECLARE → M
1:26 TRIPLE → M
1:26 NOTE_PRESUPPOSED → W
1:27 EVENT → M
1:27 REGISTRY_INSTALL → W
1:27 RESULT → W
1:27 NOTE_SPEC_DELTA → W
1:27 NOTE_SPEC_DELTA → W
1:27 NOTE_SPEC_DELTA → W
1:27 NOTE_SPEC_DELTA → W
1:28 BLESS → W
1:28 NOTE_SPEC_DELTA → W
1:28 NOTE_SPEC_DELTA → W
1:29 ORAL_UTTERANCE → O
1:29 EVENT → M
1:29 NOTE_PRESUPPOSED → W
1:29 ASSIGN → W
1:29 DECLARE → M
1:30 NOTE_PRESUPPOSED → W
1:30 ASSIGN → W
1:30 RESULT → M
1:31 TEST → W
1:31 WITNESS_STATE → O
1:31 COMMIT → W
2:1 EVENT → M
2:1 NOTE_PRESUPPOSED → W
2:2 EVENT → M
2:2 WITNESS_STATE → O
2:2 EVENT → M
2:3 BLESS → W
2:3 ASSIGN → W


---

## THE VOWEL MEASUREMENT — could the front end stand on the scroll
## plus Onkelos, without the Masoretic vowels?
## (2026-09-03, owner: "yes run that measurement" — following the
## finding that our morphology tags carry the Masoretes' vowels)

### The question

The narrative measurement above left one witness untested: 38 of the
creation week's 131 facts are decided by MORPHOLOGY, and our
morphology tags (OSHB on the Westminster Leningrad Codex) bake in
the Masoretic vowels — the same hands that wrote the accents. So:
of those 38 facts, how many could be recovered from **bare
consonants + context + Onkelos alone** — the scroll's ink plus the
oldest witness, no Masoretic vowels?

### The method

Each of the 38 morphology-decided operators was re-examined at the
consonantal (written-letter) level — every claimed letter-visibility
verified against the words table (pointing stripped), every Onkelos
citation pulled and read. Classes:

- **C** — the distinction is LETTER-VISIBLE in the bare consonants.
- **X** — consonants + CONTEXT decide (syntax, speech frames, the
  named subjects); no external witness required.
- **K** — ONKELOS is the deciding witness.
- **V** — only the Masoretic vowels decide.

### THE NUMBERS

| class | count | share |
|---|---|---|
| C — consonants alone | 25 | 66% |
| X — consonants + context | 12 | 32% |
| K — Onkelos decides | 1 | 3% |
| **V — Masoretic vowels as sole decider** | **0** | **0%** |

**Zero of 38.** The Masoretes' vowels never stand as the sole
deciding witness anywhere in the creation week. And in every X case
where Onkelos was pulled, his rendering CONFIRMS the contextual
reading (verified this sitting at 1:3, 1:6, 1:9, 1:26, 2:1, 2:2).

### The star exhibits

**The plene vav that carries a delegation (C at its best).** Genesis
1:12, וַתּוֹצֵא הָאָרֶץ — "and the earth BROUGHT FORTH": the
causative stem is visible in the bare letters — ותוצא with the vav
(the plain 'and she went out' would be ותצא) — and the feminine tav
prefix hands the verb to the earth. The week's only non-divine build
event rides on TWO CONSONANTS. Contrast 1:11's תדשא ('let it
sprout'), written defective — there the stem is NOT letter-visible
and context must decide (class X).

**The one K.** Genesis 2:1, וַיְכֻלּוּ הַשָּׁמַיִם וְהָאָרֶץ וְכָל
צְבָאָם — "and the heavens and the earth were finished, and all
their host." The bare ויכלו allows 'and they ENDED' (active) or
'and they WERE COMPLETED' (passive) — the world state is the same
either way (agentless completion), but the VOICE is settled only by
a witness: Onkelos writes וְאִשְׁתַּכְלָלוּ ('and they were
completed'), unambiguously passive. The single fact in 38 where an
external witness is the clean decider — and the witness is the
translation, not the vowels.

**The vav ambiguity, handled by position (X).** יְהִי אוֹר וַיְהִי
אוֹר — "let there be light, and there was light" (1:3). In bare
consonants the two forms are יהי and ויהי — and ויהי could equally
be 'and let it be' (as it in fact IS at 1:6, וִיהִי מַבְדִּיל 'and
let it divide'). What decides? POSITION: inside the quoted speech,
continuation of command (1:6); after the quote closes, narrative
report (1:3). Onkelos confirms both readings exactly — וַהֲוָה
('and there WAS') at 1:3, וִיהִי מַפְרִישׁ ('and let it be
dividing') at 1:6. The reading tradition's vowels (va- vs vi-)
encode precisely this judgment — which is to say: the vowels are
the teacher's parse WRITTEN DOWN, recoverable from context by the
same reasoning the teacher used.

### VERDICT — the witness stack, now fully measured

Combining both measurements over the creation week's 131 facts:

- **94 facts (72%)** stand on the SCROLL'S BARE INK alone — 69 by
  words/roots/order + 25 letter-visible morphology.
- **12 more (81% cumulative)** add only CONTEXT — syntax and speech
  frames, no witness needed.
- **1 fact** needs ONKELOS as the deciding witness (2:1's voice).
- **24 facts (18%)** are the teacher's own testimony (witness
  states, censuses) — oral by construction, exactly as declared.
- **The Masoretic vowels decide NOTHING alone; the Masoretic
  accents decide NOTHING alone.** The entire Masoretic layer —
  vowels AND accents — is a CONFIRMING witness across the whole
  week: the teacher's pronunciation and parse written down,
  agreeing everywhere with what ink + context + Onkelos already
  give, and disagreeing nowhere.

The front end can, in principle, stand on the scroll plus the
oldest witness. In PRACTICE we keep consuming the tagged morphology
— it is correct everywhere it was tested, and rebuilding it from
raw consonants would re-derive the same answers — but its STANDING
is now measured: confirmation, not foundation. The hypothesis
strengthens again: the program is in the ink; every layer above the
ink is the teacher, and every piece of the teacher's testimony
checked so far agrees with the ink it teaches.

### Appendix — the 38 morphology facts re-classified (audit trail)

| verse | the fact's morphological hinge | class — decider |
|---|---|---|
| 1:1 | perfect ברא (bara, 'created') = completed event | **C** — suffix conjugation, no vav prefix — letter-visible |
| 1:2 | perfect הָיְתָה ('was') + verbless clauses = states | **C** — suffix form היתה; verbless = absence of verb |
| 1:2 | participle מְרַחֶפֶת ('hovering') = ongoing | **C** — the participle's mem prefix is a consonant |
| 1:2 | no narrative-past verb in the verse | **C** — the ו+prefix event pattern is consonant-detectable; 1:2 has noun-first + perfect |
| 1:3 | jussive יְהִי ('let there be') = LET | **C** — short form יהי vs imperfect יהיה — the final heh is a letter |
| 1:3 | mood alone splits demanded-Q from holds-Q | **C** — יהי אור vs ויהי אור — the vav is a letter |
| 1:3 | וַיְהִי = narrative past ('and there WAS light') | **X** — consonants ויהי could also read 'and let it be'; position outside the quote decides; Onkelos: וַהֲוָה ('and there WAS') — perfect, confirms |
| 1:4 | כִּי ('that') = complementizer, not casuistic 'if' | **X** — syntax: כי directly after a verb of seeing; no vowel involved |
| 1:6 | jussive יְהִי = clean LET | **C** — short form, letter-visible |
| 1:6 | וִיהִי ('and let it be') = second directive, imperfect-coded LET? | **X** — consonants ויהי identical to narrative past; INSIDE the quoted speech = continuation of command; Onkelos: וִיהִי מַפְרִישׁ ('and let it be dividing') confirms |
| 1:6 | participle מַבְדִּיל ('dividing') = standing job | **C** — mem prefix |
| 1:7 | narrative-past וַיַּעַשׂ ('and He made') | **C** — ו+prefix short form, letter-visible |
| 1:7 | the job demand's mood stays LET? on the log | **X** — derivative of the 1:6 וִיהִי ruling — same decider |
| 1:9 | 'let the waters BE GATHERED' (passive) | **X** — consonants יקוו could also be qal 'let them hope'; context (אל מקום אחד 'to one place') decides; Onkelos: יִתְכַּנְשׁוּן ('let them be gathered') — passive, confirms |
| 1:9 | 'and let the dry land BE SEEN' (passive) | **X** — consonants ותראה could be active 'and she will see'; context decides; Onkelos: וְתִתְחֲזֵי ('and let be seen') — passive, confirms |
| 1:11 | causative תַּדְשֵׁא ('let sprout') — the first delegation | **X** — no plene vav — the causative stem is NOT letter-visible here; context (earth + cognate object דשא 'grass') decides |
| 1:11 | participles מַזְרִיעַ / עֹשֶׂה = reproduction duties | **C** — mem prefix / participle pattern |
| 1:12 | וַתּוֹצֵא ('and she BROUGHT FORTH') — earth as build agent, causative + feminine | **C** — BOTH letters: the plene vav ותוצא (qal 'went out' would be ותצא) AND the feminine tav prefix |
| 1:14 | singular fiat יְהִי over plural subject — number mismatch | **C** — יהי vs יהיו — letter-visible |
| 1:14 | purpose clauses = ל + infinitive construct | **C** — the lamed prefix is a letter |
| 1:16 | וַיַּעַשׂ — manufacture verb, narrative past | **C** — letter-visible |
| 1:17 | וַיִּתֵּן ('and He set') + אֹתָם suffix — two-step build | **C** — letter-visible |
| 1:20 | יִשְׁרְצוּ imperfect NOT jussive-coded → mandatory LET? | **C** — the ambiguity IS the fact, and it exists already at consonant level (plural forms show no distinct jussive) |
| 1:20 | יְעוֹפֵף ('let the flier fly') — doubled-stem imperfect | **C** — the doubled פ is a consonant |
| 1:21 | וַיִּבְרָא — creation's verb returns, narrative past | **C** — letter-visible |
| 1:21 | perfect שָׁרְצוּ ('which the waters SWARMED') credits the delegate | **C** — suffix form inside the אשר-clause, letter-visible |
| 1:22 | וַיְבָרֶךְ + three imperatives (פְּרוּ וּרְבוּ וּמִלְאוּ 'be fruitful, multiply, fill') | **X** — consonants פרו ורבו could be perfects ('they were fruitful'); the blessing frame + לאמר ('saying') decides imperative |
| 1:24 | causative תּוֹצֵא ('let the earth bring forth') = clean LET | **C** — plene vav letter-visible (contrast 1:11's defective תדשא) |
| 1:25 | וַיַּעַשׂ — made, not created | **C** — letter-visible |
| 1:26 | נַעֲשֶׂה ('let US make') — first-person volitive CMD-US? | **X** — consonants נעשה could be 'it was made' (passive perfect); the speech frame ויאמר decides; Onkelos: נַעֲבִיד ('let us make') — first person, confirms |
| 1:26 | וְיִרְדּוּ ('and let them rule') — jussive design clause | **X** — plural jussive = imperfect in form; continuation of the volitive decides |
| 1:27 | בָּרָא tripled: one narrative past + two perfects | **C** — ויברא vs ברא — letter-visible |
| 1:29 | נָתַתִּי ('I HAVE GIVEN') — performative first-person perfect | **C** — suffix form, letter-visible |
| 1:29 | יִהְיֶה imperfect ('it SHALL BE for food') = LET? | **C** — the final heh — letter-visible vs jussive יהי |
| 1:30 | the last וַיְהִי כֵן answers a same-root demand in narrative past | **X** — the ויהי vav-ambiguity again; formula position decides; (Onkelos: וַהֲוָה כֵן) |
| 2:1 | וַיְכֻלּוּ ('and they WERE FINISHED') — passive, the week's first agentless main-line event | **K** — consonants ויכלו allow active-intransitive 'and they ended' vs passive 'were completed' — same world state either way, but the VOICE is settled only by a witness: Onkelos וְאִשְׁתַּכְלָלוּ ('and they were completed'), passive. The one fact in 38 where the deciding witness is external |
| 2:2 | וַיְכַל ('and God FINISHED') — active, dated inside day seven | **X** — subject אלהים + object מלאכתו decide active; Onkelos: וְשֵׁיצֵי ('and He finished'), active, confirms |
| 2:2 | וַיִּשְׁבֹּת ('and He CEASED') — narrative past | **C** — letter-visible |

## THE SCROLL BREAKS AS FUNCTION BOUNDARIES — the measured coincidence
## (2026-09-04, owner: "I like this description. Lets record it...
## for epub tutorial purposes" — written as tutorial-ready prose)

WHAT THE BREAKS ARE. Every Torah scroll carries two kinds of
paragraph mark, written as blank space and copied scribe to scribe
as part of the received text: פ (petuchah, an "open" break — the
rest of the line left empty) and ס (setumah, a "closed" break — a
gap inside the line). They are far older than chapter numbers
(those are medieval additions); a scroll written with the wrong
breaks is unfit. The tradition treats the spacing as ink.

THE MEASURED COINCIDENCE (verified live 2026-09-04 from the marks
table of elijah_docket/tanakh.sqlite — kinds x-samekh / x-pe, mark
recorded after its verse). The breaks around the keeper laws fall
after Exod 22:5, after 22:8 (both ס), and after 22:12 (a פ). So
the scroll's own segmentation of Exodus 22:6-14 is:

  22:6-8    money/vessels deposited; theft; double payment; the
            oath                    = the UNPAID CUSTODIAN
  22:9-12   an animal deposited — death, injury, capture; the
            oath; restitution if stolen = the PAID CUSTODIAN
  22:13-14  the borrowed animal — full liability; the hire clause
            riding 22:14b           = the BORROWER

Babylonian Talmud Bava Metzia 94b divides the span into exactly
these three sections — "the first section... the second... the
third" — and Mishnah Shevuot 8:1's four-guardian grid runs on that
division, the renter routed from the hire clause the third section
ends with. THREE INDEPENDENT WITNESSES agree on the same cuts:

  1. the scroll's SPACING (the פ/ס marks, verified above);
  2. the grammar's verse-initial כִּי ("when") at 22:6, 22:9,
     22:13 — which the cold-compiled guardians function found with
     NO tradition loaded (cold_run_guardians.py);
  3. the Talmud's NAMED sections at Bava Metzia 94b.

AND IT GOES FINER. Immediately before this span the marks table
shows breaks after 21:32, 21:34, 21:36, 22:3, 22:4, 22:5 — the
goring ox, the pit, the grazing beast, the fire are each their own
tiny paragraph. The scroll does not just separate the keepers from
the damages; it gives EACH damage law its own function body.

THE TRADITION'S OWN THEORY OF THE BREAKS is on the corpus record:
the Sifra's charter (witnessed in the Vayikra round, the
reflection-pauses rows) says the breaks exist "to give pause to
reflect between passage and passage" — the text declaring its own
segmentation intentional. The corpus has even witnessed a law
CARRIED BY a break: the goat paragraph's hiatus holding the
no-fat-tail exemption (the Tzav-era reading).

CLASSIFICATION FOR THIS LOG: CODE-IN-INK — the program's block
structure (its function boundaries) is written in the scroll's own
layout, detectable by machine, confirmed by the Talmud's usage.

HONESTY LINE: this is "where measured," not a proven universal.
The verified case is the keeper span plus the fine-grained damages
run before it. The OPEN RESEARCH BLOCK this entry proposes: a
systematic sweep — every sugya's span boundaries against every
פ/ס break in the law chapters — the marks table makes it cheap.

THE OWNER'S ANALOGY FOR THIS ENTRY (2026-09-04): black fire on
white fire — אֵשׁ שְׁחוֹרָה עַל גַּבֵּי אֵשׁ לְבָנָה ("black fire
upon white fire," Jerusalem Talmud Shekalim 6:1; Midrash Tanchuma;
Nachmanides' introduction). The tradition's own image of the
pre-Sinai Torah: letters of black fire on a ground of white fire.
This entry is that image measured: the white space IS text — the
breaks copied as ink, a wrong-spaced scroll unfit, the blank after
22:12 carrying the information "the borrower's function begins
here." BLACK FIRE = the program's content; WHITE FIRE = its
structure. Nachmanides' rider deepens it: written unbroken the
Torah reads as divine names — the division into words and
paragraphs is itself an act of reading. The white fire is where
the parsing lives.

THE SYSTEM-WIDE SWEEP (2026-09-04, owner: "can you do that now") —
the proposed measurement RUN, whole Torah, both directions. Zero-
report law honored: the keeper-case probes (breaks after Exod
22:5/8/12; paragraph starts at 22:6/9/13; the ki-openers there)
all fired before any counting. One instrument bug caught by the
probe itself: the words table writes prefixes with a slash
(ו/כי for וְכִי "and when") — the opener test missed conjunction-
prefixed forms until normalized. The probe caught it; the false
zero never reached the report.

TEST A — THE INK-ONLY SKELETON TEST. All 5,853 Torah verses; 686
verses carry a פ/ס break after them (11.7%); 691 verses begin a
paragraph (11.8% — the 686 plus the five book openings, the
arithmetic's own check). Of the 231 verses opening with כי/וכי
("when"), 76 begin a paragraph — 32.9% against the 11.8% base:
LIFT x2.8. Of the 157 opening with אם/ואם ("if"), only 25 do —
15.9%, lift x1.3, barely above chance. THE WEAK IM RESULT IS
ITSELF A CONFIRMATION: the compiler law says ki OPENS a case and
im branches INSIDE it — and the scroll's own layout agrees,
putting breaks before the ki-verses and not before the im-verses.
The two markers behave differently against the white fire, exactly
as the two-level grammar predicts.

PER BOOK, the lift lives where the law lives: Genesis 0/30 (its
ki-verses are narrative "when," never paragraph heads), Numbers
x0.3 (same), but Exodus x2.2, Leviticus x2.0, Deuteronomy x2.4 —
the three law-dense books. The signal is a LAW-genre phenomenon:
in narrative, ki is a conjunction; in law, it is a function
header, and the scroll spaces accordingly.

TEST B — THE TALMUD WORKING-SPAN TEST. From the citation-links
shelf, Babylonian Talmud tractates only (16,290 links used; 37,101
dropped openly — commentaries, non-Torah anchors, unparsed refs);
3,456 dafs grouped; 594 contiguous cited runs of three-plus verses
(gap tolerance one verse) — the tradition's working spans. Run
STARTS land on paragraph starts 135/594 (22.7%, lift x1.93); run
ENDS land on break-carrying verses 131/594 (22.1%, lift x1.88).
Roughly double chance, both edges, across the whole shelf. Probe:
Bava Metzia 94b's detected run is Exod 22:9-13, starting on the
paragraph start at 22:9 — the run misses 22:6-8 because the daf's
citations there sit sparse in the links shelf: the instrument is
crude (daf-grain, citation-density-dependent), and the x1.9 is
therefore a FLOOR, not a ceiling.

VERDICT FOR THE LOG: the deterministic claim ("every sugya
boundary is a break") is NOT what the Torah-wide data shows — the
relationship is statistical: x2.8 for the ink's own function
headers in the law books, x1.9 for the Talmud's working spans at
a crude grain, both far beyond chance (Test A: 76 hits where
chance expects 27; Test B: 135 where chance expects 70).
CLASSIFICATION: CODE-IN-INK, measured — the scroll's white fire
carries real block structure, strongest exactly where the text is
law; the perfect coincidences (the keeper span) are the clean
cases of a genuinely statistical signal. NEXT INSTRUMENT if
wanted: sugya-grain spans (segment ranges, not daf-grain) from
the triage ledgers' own dockets — the campaign is building that
list block by block.

THE DETERMINISTIC DIRECTION RUN (2026-09-04, owner's challenge:
"it should be 100 percent when the mishnah function needs it...
Am I misunderstanding?"). The owner was right and the earlier
statistics were measuring the WRONG DIRECTION through a blurry
instrument. The refined test: enumerate EVERY break in the
ordinances code (Exod 21:1-23:19) and ask of each — does a
distinct legal unit begin here? RESULT: 31 breaks, 31 distinct
unit openings, ZERO breaks falling mid-law. 100%. The full table
(break → the law it opens): slave-daughter 21:7; the capital
striker 21:12; the presumptuous murderer 21:14; parent-striker
21:15; parent-curser 21:17; the quarrel injury 21:18; the
slave-striking 21:20; the striving men 21:22; the slave's eye
21:26; the slave's tooth 21:27; THE GORING OX 21:28 (a פ — the
open grade at the major module seam); the pit 21:33; ox-vs-ox
21:35; livestock theft 21:37; grazing 22:4; fire 22:5; the unpaid
keeper 22:6; the paid keeper 22:9; the borrower 22:13 (פ); the
seducer 22:15; the witch 22:17; bestiality 22:18; idol-sacrifice
22:19; the lender 22:24 (פ); the curse clauses 22:27; the false
report 23:1; the majority 23:2; the straying ox 23:4; the laden
donkey 23:5; justice-to-the-poor 23:6; and the code's closing
seam at 23:20 (the angel — law hands off to narrative).

WHAT THE EARLIER STATISTICS ACTUALLY MEASURED: the CONVERSE
direction — does every function get its OWN block? No, and that
is code-like too: units GROUP into blocks the way small functions
share a file. The scroll's groupings carry information the
tradition reads: 21:15-16 puts the parent-striker and the
ABDUCTOR in one block before the parent-curser — and the
juxtaposition arguments of Sanhedrin 85b-86a (the round-14
abduction grid, EX21-26) run on exactly that adjacency. The
manslayer's refuge (21:13) sits INSIDE the striker's block — an
inner branch, not a unit, and the scroll spaces it so.

THE MANDATORY-IM CONVERGENCE. Two breaks open אם ("if") verses:
the slave's tooth (21:27, a genuine parallel sub-ruling) and אם
כסף תלוה ("if you lend money," 22:24) — and the Mekhilta itself
rules that this 22:24 im is one of the THREE non-optional ims of
the Torah (obligations phrased as if). The scroll grants that
"if" a block of its own with the open-grade פ; the tradition
says that "if" is not conditional. The white fire and the
Mekhilta agree against the surface grammar — independently.

REVISED VERDICT: in the direction the hypothesis needs — every
break in law material opens a legal unit — the measured rate is
31/31, 100%, on the densest code span we have. The statistical
lifts of the Torah-wide sweep are the converse direction (unit →
own block: a grouping choice, itself meaningful) plus instrument
blur (daf-grain citations). CODE-IN-INK, deterministic where the
claim is stated correctly. NEXT: the same 100%-test on Lev 1-8
(the offering code's breaks — the reflection-pauses charter's own
home) and Deut's law core, on the owner's word.

SOURCING RULED SUFFICIENT (owner, 2026-09-04: "do we need to
research this? do we already have a reliable source"). No
standing diff-project opened. The Westminster Leningrad Codex
marks are the working white-fire witness — sufficient for all
statistical and structural claims made above; and for the
load-bearing keeper cuts the Talmud's own section-reading at Bava
Metzia 94b is the independent second witness. Standing discipline
instead of research: any individual break made load-bearing in a
publication gets a per-item check (the Talmud's usage; Maimonides'
published break table in the Mishneh Torah, Laws of the Torah
Scroll ch. 8, if ever contested). Spot-verification on demand.

---

## 2026-09-05 — THE FIRST CALL EXECUTES (Lev 24:10-23 compiled;
## the Exodus tariff cell resolves through a live import)

The compile-dependency edge recorded at EX21-18 (move M-07
exemplar c) is now a RUNNING call: cold_run_lev24.py compiles
Leviticus 24:10-23 at 23/23 with 70% pure ink and EXPORTS
talion(); cold_run_mishpatim.py's damage cell imports it and
resolves through the call — the first inter-span function call of
the compiled Bible. What the callee showed under compile:

1. THE SPAN IS A RUNTIME CODE REQUEST. The scroll's own paragraph
   marks cut 10-12 | 13-23: a case no issued code covers, custody
   "until it be declared by the mouth of the LORD" (Onkelos: the
   DECREE awaited), then the answer as NEW PROGRAM — with the
   called talion block inside it. The fourth custody-pending case
   is the one whose answer another span calls. And 24:23 is a run
   log that grades itself: "they did as the LORD commanded."
2. THE CENSUSES SHARPEN THE EDGE. Eye/tooth-under: exactly the
   two recorded seats. Life-under: exactly two, and the Leviticus
   seat is the PAY clause. New: fracture-under-fracture is UNIQUE
   to Lev 24:20 — the callee extends the caller's tariff.
3. THE TRANSLATION IS LOAD-BEARING AT THE GATE. Mishnah Sanhedrin
   7:5's liability verb ("until he SPECIFIES the Name") is
   Onkelos' own rendering of 24:11; and Onkelos renders every
   under-particle of the span as "in EXCHANGE for" — pay clause
   and tariff alike.
4. THE MONEY VERDICT RUNS ON THE SPAN'S OWN RIDERS. The pay verb
   on the exchange formula (24:18); pays-beside-dies in one verse
   (24:21, Bava Kamma 83b:10); one-law-EQUAL-for-all (24:22, Bava
   Kamma 84a:1) — literal talion fails the equality rider.
5. 50th effect registered: bears_sin (the divine-ledger debt, no
   earthly executor named; the ink pair scanned by machine —
   Lev 24:15 + Num 18:22).

Records: World/step9/REPORT_LEV24.md; ledger with full cite index
logic/oral_triage/lev_24_first_call_2026-09-05.md. Regression:
43/43 runners + all cold runners green after the wire; no unit
touched (the two Lev 24 drafts stay drafts until Emor's walk).

## 2026-09-09 — THE STORE DROPS THE LARGE LETTERS (a defect report on the
## evidence layer, found by a claim's own machine check at THE TENT sitting 4)

The snapshot store torah_grok.SNAPSHOT-main-51801ca.sqlite drops every
large-letter segment of the Torah XML (the Masorah's majuscules, carried
in Data/*.xml as <seg type="x-large"> with the note "Large letter(s)").
Measured: FOUR such segments in the five books, THREE words broken in
the store — Lev 11:42 the vav (and its nun) of "belly" (the Torah's
middle letter: the store reads two consonants of four), Num 27:5 the
final nun of "their judgment" (the store's ONLY token ending in a bare
slash, 1 of 80,052), Deut 6:4 the ayin of "hear" and the dalet of "one"
(the Shema's two large letters: the store reads them absent). The
Tanakh DB at elijah_docket/tanakh.sqlite and the XML carry all four
whole. Found because claim NM27-04's token count of "their judgment"
returned zero on the store and the ledger script's count on the Tanakh
DB returned one; the ink itself explained the delta. Consequences:
the text gate's contract is the store, so a unit's step at those verses
mirrors the truncated token with the finding on the step (num_27's
step 5); the manifest checks run on the stem; the counts are computed
on the Tanakh DB. The snapshot is immutable evidence — its rebuild
(the builder taught the large-letter segment) is the owner's word, and
every frozen hash would move with it. The daughters' halt verse is the
one case verse of the four that carries a majuscule in the ink.

## 2026-09-09 — THE SHELF'S EXPORT MISLABELS A PISKA'S HEAD (a defect report
## on the reading shelf, found by the ledger script at THE NUMBERS WALK sitting 1)

The Sefaria export of the Sifrei on Numbers (Data/sefaria_export/
Sifrei_Bamidbar/en.json) heads its piska 62 "(Bamidbar 3:24)". By
POSITION the piska sits between piska 61, headed 8:4 (the menorah's
making), and piska 63, headed 8:25 (the Levite's retirement at fifty);
by its own quotations it opens on 8:24 ("this is what applies to the
Levites: from the age of twenty-five") and cites 4:23 ("from thirty
years and up") to reconcile the two ages. It is the Sifrei's row on
Numbers 8:24 with a mistyped chapter digit (8 → 3). Measured at the
sitting: piska 1 opens on 5:1 and NO other head in the export lies
inside chapters 1-4 — the Sifrei on Numbers has no piska on Bamidbar
1:1-4:20 by position. Consequences: the ledger script's assert on the
heads catches the stray head (write_bamidbar_ledgers.py, sitting 1);
the row is READ FRESH at num_04_kehat's ledger where 4:3's thirty is
its subject and will be CREDITED when the walk reaches 8:24; the
export is evidence and is not edited — the heads are found by position
(THE TENT sitting 4's lesson), never trusted from their labels. Two
other heads in the export carry no parsable verse at all (piska 59
opens without a citation; piska 102 cites "Ibid. 4" — measured), and
the same rule covers them: their place is their address.
