# The Logic Before Computers — an audio lesson

A narrated companion to the beginner tutorial of the same date. Written to be listened to: no tables, no symbols, no diagrams. Hebrew appears only as spoken transliteration with its English meaning alongside. Date: 2026-07-28. This is a teaching narration; every method here is a lens for study, labeled as hypothesis where it touches the text, and none of it is binding religious law.

---

Here is a question worth sitting with. Long before anyone built a computer, people needed ways to write down commands, promises, procedures, and proofs so precisely that nothing was left to guesswork. Lawyers needed it. Mathematicians needed it. Priests needed it. And so, over centuries, people invented little paper machines — systems of writing where every statement has an exact shape and an exact job. We call these formal logics. Every one of them runs on paper, powered by nothing but a careful reader.

This lesson walks through eight of those methods — the ones we are now using to study the Hebrew text of Genesis. By the end, you'll be able to hear a verse and recognize which kind of logical work it is doing. Our touchstone throughout will be one short verse, Genesis one, verse three. In Hebrew it sounds like this: va-yomer Elohim, yehi or, va-yehi or. Word for word: "and God said — let there be light — and there was light." Six Hebrew words. Keep them in your ear; we will return to them again and again.

Part One. The foundation: predicates and their arguments.

Start with the oldest tool in the box. In eighteen seventy-nine, a German logician named Gottlob Frege noticed that most sentences split cleanly into two kinds of pieces: the claim being made, and the things the claim is about. Logicians call the claim a predicate and the things its arguments. "Light exists" — the claim is *existing*, the thing is *light*. "God created the heavens" — the claim is *creating*, and it takes two things: a creator and a thing created.

That sounds almost too simple to matter. But it is the grammar underneath everything else in this lesson. Every other method we'll meet is a way of decorating this basic skeleton — adding time to it, or obligation, or purpose. When our parser breaks a Hebrew verse into its small phrases using the ancient chanting marks, what those phrases hand us, again and again, is exactly this: here is a claim, and here are its things.

One special trick deserves a mention because Hebrew uses it beautifully. The Hebrew word asher means "which" or "that," and it opens a defining clause. When Genesis says "the waters which were under the firmament," that little word asher is quietly building what a logician calls a defined set: gather up everything that is water, and under the firmament, and treat it as one named collection. Genesis chapter one, verse seven does this twice in a row — waters which were under, waters which were above — and in doing so it converts a vague phrase, "waters and waters," into two precisely bounded groups. Ancient text; sharp set theory.

Part Two. Saying as doing: speech acts.

Now listen to the start of our verse again: va-yomer Elohim — "and God said." Here is a puzzle that philosophers only cracked in the nineteen fifties. Most sentences describe the world, and you can ask whether they're true. But some sentences don't describe anything — they *do* something, by being said. When an official says "I now pronounce you married," she isn't reporting a marriage that already happened. The saying *is* the marrying. The Oxford philosopher J. L. Austin called these performatives, and his little book about them is charmingly titled "How to Do Things with Words."

Genesis one is arguably the most famous chain of performatives ever written. "Let there be light" does not describe light. It brings light. So in our logic notes, we wrap these moments in a marker we call DECLARE — a flag that says: what follows is not information; it is an act of speech that changes the world.

And there is a second performative hiding in the chapter, easy to walk past. Five times in the early verses, God *names* things. Va-yiqra — "and he called" — the light, day. Yom, meaning day. The darkness he called laylah, night. Naming is not a truth claim either. You cannot say "false!" when someone names their baby. A naming installs a label. We treat every naming as a write into a registry — a little table of official labels — and we will see later that tracking that registry carefully turns up two genuine surprises.

Part Three. The logic of commands: deontic logic.

Ordinary logic handles sentences like "it is raining." But what about "close the door," or "you must rest on the seventh day"? Commands can't be true or false either — they can only be obeyed or ignored, satisfied or violated. In nineteen fifty-one, a Finnish philosopher named Georg Henrik von Wright worked out a formal logic for exactly this: the logic of obligation, permission, and prohibition. He called it deontic logic, from the Greek word for duty.

Here is where Hebrew turns out to be astonishingly cooperative. English marks commands mostly with word order and tone. Hebrew builds the command *into the shape of the verb itself*. Our example verse says yehi or — "let there be light." That word yehi is in a form grammarians call the jussive — a verb form whose entire job is to say "let it be so." Later in the same verse, the text says va-yehi or — "and there WAS light." Nearly the same word. Same root, same letters at the core. But the form has shifted from jussive to narrative past. In other words: the difference between the command and its fulfillment — between "let there be" and "there was" — is carried by nothing but the grammatical mood of a single verb. The specification and the delivery, distinguished by morphology alone. When we annotate verses, jussives become our LET operator: let it be the case. Imperatives — direct orders like dabber, "speak!" — get a stronger mark. And one form gets a question mark: sometimes the text uses the plain future tense inside command speech, like yishretzu — "let them swarm" — and we honestly cannot tell from the form alone whether it's a command or a prediction. We label those as probable commands, with the question mark kept visible. The uncertainty is part of the data.

One more discovery from this layer, and it's a lovely one. When day three opens, God says yiqqavu ha-mayim — "let the waters BE GATHERED." Notice the passive. Nobody is told to gather them. The command has no worker in it at all. Deontic logicians have a classical distinction for this: the difference between an obligation that someone *do* something, and an obligation that something *come to be the case*, doer unspecified. German philosophers called it the difference between tun-sollen and sein-sollen — ought-to-do versus ought-to-be. Hebrew encodes that exact distinction in its verb stems, and day three uses the ought-to-be form. The waters are not commanded as servants; the end state is simply required.

Part Four. Before and after: the specification pattern.

Now for the method with the most modern name and the most timeless shape. In nineteen sixty-nine, the computer scientist Tony Hoare proposed writing every operation between two conditions: what must be true *before*, and what will be true *after*. Before, operation, after. If the before-condition holds and you perform the operation, the after-condition is guaranteed. He invented it to reason about computer programs — but notice, there's no computer in it. It is a paper discipline, a way of arguing carefully. Three beats: before, do, after.

Listen to how Genesis one falls into that rhythm. Verse two is pure *before*: the earth was formless and empty — tohu va-vohu — darkness on the face of the deep, waters everywhere. And here is the detail I find most striking: in the entire verse, nothing happens. There is not one action verb in narrative form. It is all state description — a snapshot. Grammar alone tells you verse two is the precondition.

Then the operation: God speaks, yehi or, let there be light. Then the after: va-yehi or, and there was light. And then — this is the part that should make any engineer smile — verification. Va-yar Elohim et ha-or ki tov. "God saw the light, that it was good." The result is inspected and passes a test. Then a label and a timestamp: the naming, then "there was evening, there was morning, day one." A complete verified transaction: precondition, specification, delivery, inspection, labeling, commit.

Once you hear that pattern, the exceptions leap out. Day two — the firmament dividing the waters — commits *without the inspection*. There is no "and God saw that it was good" anywhere in day two. The tradition noticed this absence long ago; our logic notation simply makes it impossible to miss, because the checklist has an empty box. And day three runs the test twice. The pattern is the baseline; the deviations are the findings.

One honest caveat. The test itself — tov, "good" — is never defined in the text. Our notation can mark exactly where the test happens. It cannot tell you what goodness is. Logic finds the socket; it does not supply the electricity.

Part Five. Events with role slots.

Next tool. In nineteen sixty-seven the philosopher Donald Davidson suggested that we think of events as things — objects we can describe with labeled slots. Every event has a type: a creating, a dividing, a naming. It may have an Agent: the one who does it. A Theme: the thing it is done to. A Location, a Time. Linguists took this up enthusiastically, and today they call the practical craft semantic role labeling: read a sentence, find the event, fill in the slots.

Here Hebrew hands us a gift that most languages simply do not have. There is a little Hebrew word — et — that has no meaning and no translation. Generations of students have asked their teachers what et means, and the honest answer is: nothing. It means nothing. But it *does* something: it points at the Theme. It stands before the noun that the verb lands on. When Genesis one, verse one says God created ET the heavens VE-ET the earth — et appearing twice — the text is explicitly flagging both direct objects for you. The complete inventory of what was created, marked in the grammar itself. Our project treats et as a first-class logical operator, and when you're listening to Hebrew and you catch an et, you now know what you're hearing: the text is saying, here comes the thing the action lands on.

Part Six. The clock: temporal logic.

In the nineteen fifties, a New Zealand logician named Arthur Prior — who began his career in theology, fittingly enough — built time itself into logic. In temporal logic, statements are true *at* times: this holds now; that will hold next; this holds until that. Sequence becomes something you can reason about, not just narrate.

Genesis one wears its clock on the outside. Each unit of work closes with the same chime: va-yehi erev, va-yehi voqer — "there was evening, there was morning" — followed by a day label. We write that closing as a commit: the transaction is sealed and stamped. And the very first stamp holds a small oddity that the temporal lens makes visible: day one is not called "the first day." It is called yom echad — "day ONE," the cardinal number, one — while the later days use ordinals: a second day, a third day. Interpreters have wondered about that difference for two thousand years. The logic layer doesn't settle it; it just refuses to let you overlook it.

Part Seven. Standing jobs: invariants.

Engineers have a word for a condition that must remain true the whole time a system runs: an invariant. The bridge must bear its load — not once, but continuously. Hebrew has a grammatical form that says almost exactly this: the participle. It describes ongoing action, action as a standing state.

Genesis one, verse two, uses one: the spirit of God merachefet — hovering — over the waters. Not "hovered once"; hovering, continuously, as part of the scene. And verse six uses one inside a command, which is where it gets interesting. God says: let there be a firmament in the midst of the waters, vi-yhi mavdil — "and let it be DIVIDING" — between waters and waters. Mavdil is a participle. Day one's command asked for a thing to exist. Day two's command asks for a thing to exist *and to hold down a job* — keep the upper and lower waters apart, indefinitely. A specification with an ongoing duty attached. The participle alone carries that meaning, and our invariant marker preserves it.

Part Eight. The oldest IF-THEN in the world: casuistic law.

Everything so far came from Genesis. The last method belongs to law, and it will matter most when this project works in Leviticus. Legal scholars of the ancient Near East — and of the Bible in particular — distinguish two shapes of law. One is the absolute command: you shall not murder. No conditions, no cases. Scholars call that apodictic. The other shape is the case: IF a person does such-and-such, THEN here is what follows. That form is called casuistic, and it is the oldest form of written law we possess — the code of Hammurabi is built from thousands of such if-then cases.

The Hebrew trigger word is ki — "when," or "if." Leviticus one, verse two: adam ki yaqriv — "a person, WHEN he brings an offering..." That is a case frame opening. And everything that follows in the chapter fills in the sub-cases: if from the herd, this procedure; if from the flock, that one; if a bird, another. It is a decision tree, spoken aloud, thirty-three centuries before flowcharts. When our project writes Leviticus rules as if-then tables, we are not imposing computer thinking on an ancient text. We are restoring the text's own native form.

Part Nine. Running it all by hand.

So how do these eight tools work together? Here is the practice we call the dry run, and it needs nothing but paper. You keep six little lists as you read. The clock: where are we in time. The world: what exists so far, and what is currently true of it. The registry: what has been officially named. The open specifications: commands issued but not yet fulfilled. The test log: what has been inspected and passed. And the ledger: which day-units have been sealed. Then you walk the verses in order, one at a time, and update the lists.

Do that for the first ten verses of Genesis and three genuine discoveries fall out. First: the world list splits in two. Some things arrive by explicit creation — light, the firmament. But others are simply *used* without ever being introduced: the darkness, the deep, the waters. They appear in the story as if already there. Readers have debated the pre-existing materials for millennia; the bookkeeping surfaces them automatically, because you reach for them on your list and find no entry.

Second: commands are fulfilled at three different speeds. Light is instant — the command and its fulfillment sit in the same breath. The firmament takes a spec in one verse and an explicit build step in the next — God *makes* it, then the checkmark comes. And the gathering of the waters is commanded with no worker and fulfilled in the same verse with no builder named — it simply comes to pass. Same pattern, three tempos.

Third: the registry contains two label collisions. The name shamayim — heavens — is installed in verse one, and then installed *again* in verse eight, onto the firmament. The name eretz — earth — is installed in verse one, and again in verse ten, onto the dry land. Two names, each officially given twice, to arguably different things. Is that aliasing? Refinement? A deliberate echo? The logic cannot say. But it can catch the collision and hold it up to the light — which is exactly the division of labor we want. The paper machine finds the anomalies; the interpretation of anomalies belongs to study, and to the tradition.

Part Ten. What this all is, and what it is not.

Let me close with the honest frame. Nothing in this lesson claims that Genesis *is* a computer program, or that its authors knew formal logic. These methods are lenses. Each one was invented — by Frege, by Austin, by von Wright, by Hoare, by Davidson, by Prior, and by nameless ancient legal drafters — to make one kind of human meaning precise: facts, speech-acts, duties, procedures, events, time, standing conditions, and cases. The Hebrew text visibly traffics in all eight kinds of meaning, and its grammar marks them with a precision that rewards this kind of reading. When the lenses fit, we say so, and label it tested. When a reading goes beyond the form — like hearing every future-tense verb as a command — we keep the question mark, and label it hypothesis. The Hebrew remains the only source. The logic is just a way of taking it seriously, word by word, mark by mark.

That is the toolbox. Before, do, after. Let it be. Here is the thing it lands on. There was evening, there was morning. And a small word that means nothing and points at everything.

End of lesson.
