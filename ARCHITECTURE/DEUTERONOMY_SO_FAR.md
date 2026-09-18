# Deuteronomy so far — the five books as a program

*A tutorial for a reader with no background, rewritten from scratch on 2026-09-18 on the owner's word ("a tutorial for the public with no knowledge"). It says what Deuteronomy is, then takes the five books of Moses one at a time, with the Joseph story as its own section, and answers two questions for each: what does the book do, and where does it sit in the machine. Everything here is what the project has built as of chapter 7 of Deuteronomy. The records behind every sentence are in the repository: the maps `World/step9/NUMBERS_WALK.md` and `World/step9/DEUTERONOMY_WALK.md`, the runners `World/step9/cold_run_<span>.py`, the ledgers in `logic/oral_triage/`. Chapter numbers are used throughout. Book names are given in full.*

---

## 1. What this project is, in plain words

The Hebrew Bible opens with five books, traditionally called the five books of Moses, or the Torah (a Hebrew word meaning "instruction"). Genesis, Exodus, Leviticus, Numbers, Deuteronomy. This project reads those five books as if they were a computer program, and builds the computer that runs them.

That sounds like a metaphor. Here it is not. The project's rule, stated by its owner and followed in every line of code, is this:

**The twenty-four books of the Hebrew Bible are the program. The Talmud holds the compile rules. The Mishnah is the answer sheet.**

Three names need saying once.

- **The Mishnah** is a law code written down about the year 200. It states results: in this case, this is the ruling. It rarely says why. For the machine it is the answer sheet, the set of expected outputs a correct program must reproduce.
- **The Talmud** (the Babylonian Talmud, finished about the year 500) is the long commentary on the Mishnah. It argues, cites verses, and shows how a ruling follows from the text. For the machine it is the set of compile rules: how a verse becomes a procedure.
- **The written text** itself, the five books and the nineteen after them, is the program. Every verse either records something that happened, or states a rule.

The machine therefore has two halves, and the owner's frame for them, ruled on 2026-09-16, is the shortest way to say it:

**Law is code. Narrative is everything else in a computer program.**

A law in the text is compiled into a small function. A story in the text is data: an event on a timeline, with a date, that the functions can react to. The numbers in the stories (a census count, an age, the size of a spoil) are the variables the functions read. The date stamps are the clock.

Nothing religious is claimed by any of this. The project is a way of reading closely with a machine that will not let a verse be skipped, a number be rounded, or a rule be paraphrased. When the machine's output disagrees with the Mishnah, the machine is wrong, and the disagreement is written down.

---

## 2. What Deuteronomy is

Deuteronomy is the fifth and last of the five books. Its name is Greek and means "second law." Its traditional Hebrew name, Mishneh Torah, means "the repetition of the instruction." Both names say the same thing: this book says again what the earlier books said.

The setting is one place and almost one day. Israel is camped on the plains of Moab, east of the river Jordan, in the fortieth year after leaving Egypt, in the eleventh month, on the first day (1:3). Moses is about to die and will not cross the river. Almost the whole book is speeches he gives before he dies.

In order, the book does five things.

1. **Chapters 1 to 3.** Moses retells the journey: the departure from Horeb (the mountain also called Sinai), the spies and the forty years, the kings Sihon and Og defeated east of the river, and Joshua named to lead the crossing.
2. **Chapters 4 to 11.** Moses retells the giving of the law at Horeb, says the Ten Commandments a second time (chapter 5, with small differences from Exodus 20), gives the creed "Hear, O Israel" (chapter 6), and gives the law of the seven nations of Canaan (chapter 7). Chapters 8 to 11 exhort.
3. **Chapters 12 to 26.** A long law code, much of it new: where to worship, what to eat, the courts, the king, the prophet, war, marriage, and many more.
4. **Chapters 27 to 30.** The covenant renewed: blessings for keeping it, curses for breaking it.
5. **Chapters 31 to 34.** Moses writes the book down, deposits it beside the ark, sings a song, blesses the tribes, and dies on Mount Nebo.

The project's walk through Deuteronomy started on 2026-09-15 and has reached the end of chapter 7. Every chapter so far has been read whole with two ancient companions (Onkelos, the ancient Aramaic translation, and the Sifrei on Deuteronomy, an early commentary that reads the book line by line), and then compiled. What the machine learned from those seven chapters is in section 9. But the reason Deuteronomy matters to the architecture can be said now.

### Why the fifth book is different for the machine

The first four books put events and laws on the timeline in the order the text gives them. Deuteronomy **says things again.** A machine that keeps one event per thing that happened must decide what to do when the text tells it a second time. The answer, built in the first sittings of the walk and now a standing rule, is called **the readback**:

**A retelling is a reference row, graded against the timeline. It is never a second act.**

When Moses retells the exodus, the machine does not add a second exodus. It finds the line the exodus already made, sets the retelling beside it, and records a grade: VERBATIM if the words repeat, VARIANT if a word moved and the sense did not, EXPANDED if a clause was added, SHORTENED if the line was compressed, TURNED if a ground or an object was replaced, SUPPLIED if the retelling tells something no earlier book recorded, DISAGREES if it contradicts the line.

The SUPPLIED grade is where Deuteronomy changed the timeline. When Moses tells an act that no earlier book wrote down, the act is real and belongs on the timeline, but at the day it happened, not the day Moses speaks. The machine steps its clock back to that day, writes the line once, and steps forward again. The device that does this is called a **retrograde marker**.

The readback has taken four forms so far, one per kind of thing the text retells. Section 9 shows them. The short version: Deuteronomy is the book where the program reads itself back, and the machine grades the reading.

---

## 3. The machine in one picture

Before the books, the parts. There are seven, and the rest of this tutorial uses their names.

**The tape.** One timeline of events, in the order of the verses, with a clock. Every event is a line: a kind (what happened), a subject (who it happened to), the verse it comes from, and a date on the clock. The clock stands today at year 40, month 11, day 1, which is the date Deuteronomy 1:3 gives. The tape holds 1,307 lines after chapter 7.

**The runners.** One program file per stretch of text. A runner holds the stretch's laws as functions ("cells"), the stretch's events, and the tests the stretch must pass. There are 62 runners. Section 10 counts them by book.

**The daemons.** A law, once given in the text, becomes a small program that watches the tape for the kinds of event it governs, and writes its verdicts when they arrive. There are 67. Each has a verse where it was given and an act that switched it on: 26 were on from the start, 14 were switched on by the blood thrown at the covenant of Exodus 24, 3 by the erection of the sanctuary, 17 by the call from the tent that opens Leviticus (1:1), 4 by the sentence or the statute declared at a case that had no rule yet, and one waits for the entry into the land, which is Joshua's book, not yet run.

**The ledgers.** A daemon's verdict is never a new event. It is an entry on a ledger: a debit (something owed, open until closed), a block (something barred), a status, an entry in heaven's ledger (a promise or a blessing, often with a condition), or a close (a debit paid). The vocabulary of ledger entries is fixed and registered: 1,029 names. There are 127 closes on the tape today, and 319 entities (people, peoples, places, things) that ledger entries can be written on.

**The checkpoints.** Assertions about the world at a named point on the tape: after this verse, this debit is open, that count is 19, the clock reads this. There are 244 of them, and every run of the tape must satisfy all of them.

**The answer sheet.** The Mishnah's rulings on a stretch are read whole from the shelf, typed as test rows, and run against the cells. The count of graded cells across all runners is 6,669 after chapter 7. When a Talmud page discusses the stretch, its rows are read whole too, and sorted: a law, a derivation, a dispute, context, or outside the stretch. Chapter 7's docket alone is 520 rows.

**The readings.** Before anything is compiled, the stretch is read: the text, its ancient translation, its early commentary, verse by verse, and the reading is frozen as a unit that never changes afterward. There are 221 frozen units. The reading comes first, the code second, and the code may never run ahead of the reading.

One more thing sits under all seven: **the one database.** Every line of the tape, every ledger write, every reading is in a single file, and a gate replays the tape from the start and refuses the run if the replay does not match what was written the first time. The replay is the audit.

Now the books.

---

## 4. Genesis: the world is opened, and the promises are made

Genesis runs from the creation to Joseph's coffin in Egypt. Fifty chapters, almost all story. For the machine it does three things.

**It makes the entities.** Adam, Noah, Abraham, Sarah, Isaac, Rebekah, Jacob, Leah, Rachel, the twelve sons, Esau, Ishmael, the nations, the cities, the land itself. A ledger entry has to be written on someone. Genesis is where most of the someones are born, and the population table the later books read (148 rows today) begins here.

**It writes the promises, with their conditions and their dates.** The covenant with Noah (chapter 9). The promise to Abram at 12:2-3, "I will bless you," which the machine records as an entry in heaven's ledger named for Abram, and which is still there when Deuteronomy 7 reads it back. The oath sworn to Abraham at 22:16, "by Myself I have sworn," a line the machine names `sworn_by_himself` and which later books cite. The oath upheld to Isaac at 26:3. Joseph's promise at 50:24, "God will surely visit you," which opens a debit that the exodus closes. These are the debits and heaven entries that the rest of the program pays or keeps.

**It gives the first laws.** Few, but real, and they are given before Sinai: the day boundary and the sabbath (chapter 1 and 2:1-3), the one command in the garden (2:16-17), the one flesh (2:24), the laws given to Noah about blood and life (9:1-17), and circumcision (chapter 17). The machine calls these the pre-Sinai code, and five daemons are given in Genesis.

**Where it sits.** Genesis is the initialization. Its narrative sets the variables the code later reads: the seventy who went down to Egypt (46:27), the names of the twelve sons which become the keys of every census roll in Numbers, the four hundred years foretold at 15:13 and counted out at Exodus 12:40. Its laws are the first daemons on the tape.

The book runs in five runners: the pre-Sinai code; the story from Eden to Hagar (chapters 2 to 16); the story from Mamre to the heap of stones at Gilead (chapters 18 to 31, Abraham and Sarah to Jacob and Laban); and the family code, which holds the purchase of the cave (chapter 23), the commission of the servant (chapter 24), the sinew at the ford (32:25-33), Judah and Tamar (chapter 38), and the two blessings at Jacob's deathbed (chapters 48 and 49). The fifth Genesis runner is the Joseph story, which gets the next section.

---

## 5. Joseph: the bridge from a family to a people

The Joseph story is Genesis 37 to 50 with the stretch that leads into it, and the machine gives it a runner of its own, named "from the ford to the coffin": Jacob's night at the ford of the Jabbok and the meeting with Esau (chapters 32 and 33), Dinah at Shechem (34), Bethel again and three deaths (35), Esau's roster (36), the dreamer sold by his brothers (37), Potiphar's house and the prison (39 and 40), Pharaoh's two dreams and the rise (41), the brothers' two descents into Egypt (42 to 44), "I am Joseph" (45), the seventy who come down and settle in Goshen (46 and 47), and the oath, the mourning and the coffin (50). Chapters 38, 48 and 49 belong to the family code, and the story's runner calls them when it needs their law.

**What it does.** Three things, and each is why the story deserves its own section.

First, **it moves the family into Egypt.** Exodus opens with "these are the names of the sons of Israel who came into Egypt" (Exodus 1:1). The seventy, Goshen, the years of famine, Joseph's fifth (47:24) are the initial state of the second book. Without this runner, Exodus has no starting values.

Second, **it opens the debit the next book closes.** At 50:24 Joseph makes his brothers swear: God will visit you, and you will carry my bones out of here. The machine writes this as a promise line, `visitation_promised`, and Exodus answers it: Moses takes the bones at 13:19, a line of its own on the tape, and the going out at 12:51 is the visit. In Deuteronomy 7:8, "the LORD brought you out with a mighty hand," the retelling is graded against this very line, among others.

Third, **it carries an answer sheet of its own.** The story reads like story, but the Mishnah rules on it in ten places: Reuben's act is read in public but not translated (Megillah 4:10); Joseph's burying of his father sets the rule for who buries whom (Sotah 1:9); Judah's surety for Benjamin is the model case of the guarantor (Bava Batra 10:8, Bava Metzia 5:11); the men of Shechem's pain on the third day (34:25) fixes the third day after circumcision in the law of the sabbath (Shabbat 19:3); the search of the sacks (44:12) is set beside the search for leaven (Pesachim 1:1); Joseph's forgiveness of his brothers is the model of forgiveness (Bava Kamma 8:7); Shechem's act is the model of the seducer (Ketubot 3:4); "be fruitful" the duty to have children (Yevamot 6:6); and the order of inheritance (Bava Batra 8:2). Every one of those rows is typed as a test, and the runner's twenty-three cells must reproduce them.

**Where it sits.** The Joseph runner is the model of how the machine handles a long narrative. Each act and each speech is typed as an event with a witness cut from the verse's own consonants, so that the event cannot be claimed where the verse does not say it. The scene the events produce on a bare world (which ledgers, how many entries, what the clock reads at the end) was predicted by hand before the file was typed, and the run had to match the prediction. The same discipline governs every runner after it.

---

## 6. Exodus: a family becomes a people with a law and a clock

Exodus has forty chapters. The first nineteen are story; the twenty-first to the twenty-third are law; the rest is the sanctuary, its plans and its building, with the golden calf in the middle.

**What it does.**

**The story (chapters 1 to 19)** puts the exodus on the tape as lines the whole rest of the Bible will cite. The ten plagues are ten lines, each with its close (the plague struck, the plague removed). The going out at 12:51. The sea split and the people saved at the sea (chapter 14). The healer promised at Marah (15:26). The manna. Amalek's blotting sworn (17:14). And at 19:5-6 the offer at Sinai: "if you will hear My voice and keep My covenant, you shall be My treasure among all peoples." The machine writes that as an entry in heaven's ledger, `treasured_people`, with the condition attached; Deuteronomy 7:6 reads it back word for word.

**The Passover (chapters 12 and 13)** is the first law given inside the story, at its own day, and its daemon is the first that a story switches on. It also gives the machine its calendar: "this month shall be for you the beginning of months" (12:2).

**The ten words (20:1-17)** are the Ten Commandments. The machine compiles them as cells, and a question is on the table, not yet ruled, whether they are also the program's table of contents, each word a heading under which the later laws file. The tutorial on that question is `THE_TEN_AS_A_SCHEMA.md` in this folder.

**The ordinances (chapters 21 to 23)** are the first block of case law: the slave, the injuries, the ox that gores, the four kinds of guardian (22:6-14), the seducer, the judges, the festival calendar (23:10-19). And at 23:20-33, the clauses about the angel who goes before the people and the land they will enter: no covenant with the inhabitants, the hornet, "little by little," the snare of their gods. Those clauses are the code that Deuteronomy 7 says again for the land, and the machine grades chapter 7 against them by calling them.

**The covenant and the calf (chapters 24, 32 to 34).** At 24:8 Moses throws the blood of the covenant on the people, and the machine switches on fourteen daemons at that act. Then the calf, the tablets broken, and the covenant written a second time (chapter 34), whose clauses on the seven nations and their daughters are also code that Deuteronomy 7 reads back.

**The sanctuary (chapters 25 to 31 and 35 to 40)** is the first place the machine grades a specification against its own run. The plans in 25 to 31 are a spec. The building in 35 to 40 is the spec executed. The runners for the sanctuary, the vestments and the incense altar read the plan, read the construction, and assert that the second matches the first, piece by piece.

**Where it sits.** Exodus is where the machine gets its clock (the first month), its first switched-on laws (the Passover at its day, fourteen daemons at the blood of the covenant, three at the erection of the sanctuary in chapter 40), its first spec-versus-run grading, and the lines the rest of the Bible cites most. Eighteen daemons are given in Exodus. Thirteen runners cover the book.

---

## 7. Leviticus: the law book, almost entirely code

Leviticus has twenty-seven chapters, and nearly every verse is a rule. There is story only at chapters 8 to 10 (the ordination of the priests, the eighth day, the death of Nadab and Abihu) and 24:10-23 (the blasphemer). Twenty-two daemons are given here, the most of any book, and twenty runners cover it.

**What it does.** It installs the functions that the cases of the whole Bible will later hit.

- **The offerings (chapters 1 to 7)** are an engine: the burnt offering, the meal offering, the peace offering, the sin offering with its rank tree (a different animal for a priest, a ruler, a common person), the guilt offering, and the priests' portions. Chapter 9 is that engine's first run, the eighth day, and the machine grades the run against the spec of chapters 1 to 4.
- **The species classifier (chapter 11)** takes an animal's signs and returns clean or unclean. Deuteronomy 7:26 borrows its verb ("you shall utterly detest it," 11:43) and the runner for chapter 7 calls the classifier to say so.
- **The impurity clocks (chapters 12 and 15)** are timers: a birth or a discharge starts a count of days, and the count fires on the tape's clock.
- **The leper (chapters 13 and 14)** is a diagnosis table and a cleansing procedure.
- **The day of atonement (chapter 16)** is a procedure with an annual timer.
- **Blood, unions and sanctions (chapters 17, 18, 20)** hold the forbidden unions and the penalties, including the giving of seed to Molech at 20:2-5. That one verse matters to chapter 7 of Deuteronomy for a comic reason: the Hebrew consonants of "Molech" and "king" are the same, and when the machine's token census scanned Deuteronomy 7:8, "Pharaoh king of Egypt," it demanded to know why chapter 7 was citing the sanctions of Leviticus 20. The answer, a homograph, is filed as a false edge with its reason.
- **The holiness code (chapter 19)** is the densest law chapter in the Torah: love your neighbor, the gleanings, the false weights, the mixed kinds, the elder's honor.
- **The priesthood and its dues (21 and 22), the appointed times (23), the jubilee (25), the covenant's cascade of blessing and curse (26), consecration and substitution (27).** The appointed times are the machine's period timers: they fire every year of the tape's clock, and the count of fires is one of the numbers every run must reproduce.

**Where it sits.** Leviticus is the layer of installed functions. When Numbers brings a case (a man gathers wood on the sabbath; a man blasphemes), it is a Leviticus daemon, or one born at that case, that answers. When the Prophets and the Writings bring their cases (Jephthah's vow, Ruth's redemption, Naboth's vineyard), it is these functions, waiting on the tape, that they reach. The Mishnah's shelf is richest on this book, and the answer sheet is longest here.

---

## 8. Numbers: the laws are asked to act

Numbers has thirty-six chapters, and it is the first book where the installed laws fire on cases in the story. The walk through it, chapter by chapter from 1:1, closed on 2026-09-13 in fifteen sittings. Eighteen daemons are given here, and eighteen runners cover it.

**What it does.**

- **The census and the camp (chapters 1 to 4)** count the people by tribe and lay out the camp. The counts are variables: the machine reads the twelve tribes' numbers, sums them, and checks the sum the text gives.
- **The tent's four cases.** Four times in the Torah the people bring a case to Moses, he has no rule, and the rule comes from the tent: the blasphemer (Leviticus 24:10-23), the men unclean at Passover (Numbers 9), the wood-gatherer (15:32-36), and the daughters of Zelophehad who ask to inherit their father's land (27:1-11, with the amendment at chapter 36). The machine calls these laws born from cases; their daemons are switched on by the sentence or the statute declared at the case itself. The daughters' case is also the first input the machine's port accepts: a case that arrives from outside the text and asks the running world what it rules.
- **The march and the spies (chapters 10 to 14).** The decree of forty years is the biggest single walk of the clock: the tape steps through the years, and every timer that fires in them (the appointed times, the impurity counts) fires on the way.
- **Korah (16 to 18), the red heifer and the waters of Meribah (19 to 21), Sihon and Og (21).** That the two kings' cities were devoted, that is, put under the ban, is told only in Deuteronomy 2:34 and 3:6; the machine wrote those lines at their own day from the retelling, and notes that this is the ban run before its rule is stated: the rule comes at Deuteronomy 7:2 and 20:16-18.
- **Balak and Balaam (22 to 24) and the whoring at Peor (25).** Peor is the exhibit the marriage law of Deuteronomy 7:3-4 points to.
- **The second census (26), the offerings calendar (28 and 29, eight period timers on the altar), vows (30), the war of Midian (31), Gad and Reuben (32), the journeys (33), the borders (34), the cities of refuge (35).** The journeys chapter ends with the command to dispossess the inhabitants and destroy their images (33:50-56). The machine writes that as two debits on Israel, open, and they are still open at the end of Deuteronomy 7, because the act that closes them is Joshua's.

**Where it sits.** Numbers is the first book that runs the program instead of only writing it. Its cases reach the Leviticus functions; its counts are read and summed; its timers fire across the forty years; its debits stay open into the next books. The population table, the timer table and the checkpoint table all grew most in this book.

---

## 9. Deuteronomy so far: the program read back, chapter by chapter

The walk began on 2026-09-15 and each chapter is done in two sittings: the reading (the text with Onkelos and the Sifrei, whole; a frozen unit; the ledger of what the commentary says on each verse) and the compile (the docket of everything the Mishnah and the Talmud say on the chapter, every row read whole; the runner; the tape; the gates). Four daemons are given in the seven chapters, and five runners cover them.

**Chapters 1 to 3: the retelling of acts.** The readback's first form. Moses' retelling of the journey is 42 reference rows graded against the tape: EXPANDED 12, SUPPLIED 11, TURNED 10, SHORTENED 6, DISAGREES 2, VERBATIM 1. The eleven supplied acts, things the earlier books never recorded (the appointment of the judges as Moses tells it, the request to send the spies coming from the people, and others), were written once at their own day by three retrograde markers. The two disagreements (1:37, where Moses blames the people for his exclusion, and 2:29, on what Edom gave) are left open, not resolved. Joshua's commission (Numbers 27:12-23) is the runner's callee: the retelling of it at 3:28 is graded against the line it made. The chapter's one forward marker, 1:1, walks the clock 177 days to the date at 1:3, and 36 timers fire on the way.

**Chapter 4: the tape had a hole.** Moses retells the day at Horeb when the people stood before the mountain and heard the ten words, and the giving of the first tablets. The tape had no line for either: Exodus 20:1 and 31:18 had never been written as events. Chapter 4 put both lines there, at their own days, by a retrograde marker. The chapter also holds one law, "you shall not add to the word" (4:2), one case (the three cities of refuge east of the river, 4:41-43), and the exhortation.

**Chapter 5: the code said again.** The readback's second form, the laws' form. The ten words are given a second time, with differences (the sabbath's "keep" for "remember," and its reason changed from creation to Egypt). Each word of the second copy is graded against the cell that compiles the first copy: sixteen rows on the code, VERBATIM 5, VARIANT 5, EXPANDED 3, TURNED 3. Two words had no cell anywhere in the machine, the second (no other gods, no image) and the tenth (do not covet), and were compiled here from both copies. And the people's request for a mediator (Exodus 20:18-21, told fully only here at 5:23-31) had no line; it was written at its day.

**Chapter 6: "Hear, O Israel."** The creed at 6:4 and its four duties (recite these words, teach them to your children, bind them on the hand and between the eyes, write them on the doorposts) had no cell anywhere in the machine, and were compiled here at the chapter's own day. The readback's third form appeared: "when your son asks you" (6:20) is a law's clause, and the answer the father must give (6:21-25) is a retelling of the exodus inside a law, graded against the tape and against the cell that compiles the duty to answer. The commentary read 6:11's spoil of the seven nations as permitted, which the next chapter's ban must be squared with. Also in this sitting, the owner ruled the whole-row rule: no row of the Mishnah or the Talmud is ever read cut; the rows already read short were reread whole and the grades corrected.

**Chapter 7: the seven nations.** The readback's fourth form: the chapter re-says the code of another chapter for a new place. "Make no covenant with them" is Exodus 23:32; "little by little" is Exodus 23:30; the hornet is 23:28; the daughters are Exodus 34:16; the images and pillars are Numbers 33:52; "to a thousand generations" is the second word's clause. So the row's first telling is a cell in another runner, and chapter 7's runner grades the row by calling that cell: twenty-one rows, VERBATIM 4, VARIANT 5, EXPANDED 8, TURNED 3, SHORTENED 1, every cell found. Four things in the chapter had no first telling anywhere: the ban itself (7:2, "you shall utterly destroy them"), "show them no favor" (7:2), "your eye shall not pity" (7:16), and the abomination brought into the house (7:25-26). These are the code's four holes, and they were compiled here, their writes at the chapter's own day. Two ledger names from Exodus, the covenant barred and intermarriage barred, were written on the tape for the first time: in Exodus they were written only on cases (the entry into the land, a daughter taken) that never arose on the tape. The chapter's docket was 520 rows, mostly from the tractate Avodah Zarah (on idolatry) of the Babylonian Talmud, every row read whole.

**Two questions on the table, not ruled.** One is the schema question of section 6. The other came from the owner's remark on 2026-09-18: Deuteronomy alters old code and creates new code; is it the program's install? The walk's own record says the fifth book reads the program back, finalizes it, writes it down and names the installer, which a companion document in this folder, `THE_BOOKS_AS_A_PROGRAM.md`, calls the release, with Joshua the install. Both are recorded as questions. Nothing of the engine was changed for either.

**What is ahead.** Chapters 8 to 11, then the law code of 12 to 26 (where the war chapter, 20, will give the cells the ban's rule owes forward), then the covenant, the song, the blessing and the death. After Deuteronomy, the second pass: every earlier book run again with the readback's rules in force.

---

## 10. How the five books fit together

Read the five books as five layers of one program, laid down in order.

| Book | What it does | Laws given | Runners |
|---|---|---|---|
| Genesis | Makes the entities, writes the promises with their dates and conditions, gives the first laws | 5 | 5 (the Joseph story one of them) |
| Exodus | Turns a family into a people with a calendar, a covenant and a sanctuary; the first laws switched on by acts; the first spec graded against its run | 18 | 13 |
| Leviticus | Installs the functions: offerings, purity, the forbidden unions, holiness, the priesthood, the timers, the jubilee | 22 | 20 |
| Numbers | Runs the program: cases reach the functions, counts are summed, timers fire across forty years, debits open toward the land | 18 | 18 |
| Deuteronomy (to chapter 7) | Reads the program back and grades the reading; fills the holes the reading found; re-declares old code for the land | 4 | 5 |

The tape runs through all five without a break. A promise made in Genesis 50 is closed in Exodus 13. A law switched on in Exodus 24 answers a case in Numbers 15. A clause in Exodus 23 is called by Deuteronomy 7. The clock that starts at the first month in Exodus 12 reads year 40, month 11, day 1 at Deuteronomy 1:3, and every timer between them has fired the number of times it should. That continuity is what the gates check, in one chain, at the end of every sitting: the tape replayed, the checkpoints, the daemons, the dependencies, the one database, the journal, the register of receipts, the positions of the checkpoints, the sweep of every runner. All green, or the sitting is not closed.

---

## 11. Where to look next

Everything in this tutorial has a longer form.

- `THE_TOUR.md` in this folder: the seven parts, how they are wired, and one event followed from birth to rest.
- `THE_EFFECTS.md`: the ledgers and the vocabulary of effects, with stories.
- `THE_CLOCK.md` and `TIME.md`: the calendar, the counter, the timers, the markers.
- `THE_LINKS.md`: how a link between two verses is admitted (only when a teacher taught it; otherwise a labeled hypothesis).
- `THE_TEN_AS_A_SCHEMA.md`: the ten words as the program's table of contents (on the table).
- `THE_BOOKS_AS_A_PROGRAM.md`: the six books after the Torah measured by function (a discussion document, nothing ruled).
- `World/step9/DEUTERONOMY_WALK.md`: the walk's map, one section per sitting, with the design before the code and the "as built" after it.
- `World/step9/NUMBERS_WALK.md` and `World/step9/THE_TENT.md`: the fourth book's walk and its four case-born laws.
- `THE_STEPS.md` at the repository root: the six steps a span of text goes through, in the owner's plain language.

---

## 12. A short glossary

- **The tape.** The one timeline of events, in verse order, with a clock.
- **A line.** One event on the tape: a kind, a subject, a verse, a date.
- **A marker.** A line that moves the clock: forward to a stated date, or backward (a retrograde marker) to write an act at its own day.
- **A runner.** One program file for one stretch of text, holding its cells, its events and its tests.
- **A cell.** One compiled law, a function that takes a case and returns a verdict with its effects.
- **A daemon.** A law installed on the tape, watching for the kinds of event it governs.
- **An effect.** What a verdict writes on a ledger: a debit, a block, a status, a heaven entry, a close.
- **A debit.** Something owed and open, until an act closes it.
- **A close.** The line that pays a debit.
- **A checkpoint.** An assertion about the world at a point on the tape, checked on every run.
- **The answer sheet.** The Mishnah's rulings on a stretch, typed as tests.
- **The docket.** Everything the Mishnah and the Talmud say on a chapter, every row read whole and sorted.
- **A unit.** A frozen reading of a stretch, never changed after it is frozen.
- **The readback.** A retelling graded against the tape, never a second act.
- **The shelf.** The local copies of the Mishnah, the Talmud, the ancient translation and the early commentaries, from which every row is read.
- **A gate.** A check that must pass before a sitting closes; the gates run as one chain.
