# THE COST AUDIT — 2026-09-20 (on the owner's "Do a complete audit of our process … I can't pay $1000 a chapter")

A DISCUSSION RECORD, NOT A RULING. Every number below was COMPUTED from the session transcripts (the harness's own usage fields on every API
call, one usage per message id — the transcript writes one entry per content block, so a naive sum over-counts by 2.7x; the scripts and their prints
are in forms_deuteronomy_walk/cost_audit_2026-09-20_*.py / .out). The dollar figures use a YARDSTICK — the Opus-class list prices ($15 per M new
input, $18.75 per M cache write, $1.50 per M cache read, $75 per M output). The model's own prices may be higher; the SPLIT and the LEVERS hold at
any price, because every lever is a token count.

## 1. THE BILL AS MEASURED (2026-09-12 to 2026-09-20, one session, 3,435 API calls)

| day | calls | $ (yardstick) | cache WRITES | cache READS | OUTPUT | avg context per call |
|---|---|---|---|---|---|---|
| 09-12 | 327 | 654 | 49% | 30% | 20% | 456k |
| 09-13 | 475 | 832 | 41% | 40% | 18% | 510k |
| 09-14 | 322 | 313 | 10% | 72% | 17% | 474k |
| 09-15 | 513 | 623 | 27% | 58% | 13% | 489k |
| 09-16 | 503 | 987 | 50% | 32% | 16% | 482k |
| 09-17 | 226 | 355 | 50% | 29% | 20% | 354k |
| 09-18 | 266 | 509 | 56% | 26% | 16% | 396k |
| 09-19 | 393 | 779 | 49% | 34% | 15% | 512k |
| 09-20 | 410 | 887 | 50% | 27% | 21% | 462k |
| TOTAL | 3,435 | 5,940 | 45% | 37% | 17% | — |

THE DEUTERONOMY WALK's five days (09-16 to 09-20) cost $3,517 at the yardstick for eleven chapters read and compiled — $320 a chapter at the
yardstick; the owner's $1,000 figure says the model's real prices run about three times the yardstick. The split is what matters:

- **CACHE WRITES 45%.** 169 calls each re-wrote the WHOLE context (their reads were 20k — the system prompt alone): 102M of the 143M tokens
  written (71% of the writes, about a THIRD of the whole bill). Their cause, by the gap since the call before: 126 of 169 came after a gap of
  5 to 60 minutes, 16 after more than an hour, 27 under 5 minutes. TODAY: 24 after gaps of 5-60 minutes, 1 over an hour. THE CACHE IS
  EXPIRING AT FIVE MINUTES, NOT THE HOUR the harness names (its own note: in usage overage the TTL drops to five minutes). Every wait past
  five minutes on a 500k context — the chain, the tape, the recorder, the positions table, the sweep, the owner's pauses — costs a full
  re-write: about $9 at the yardstick each, some 25 times a day.
- **CACHE READS 37%.** Every call re-reads the whole context. A third of all calls ran at 600k-1.1M of context and carried 57% of the reads
  and 55% of the writes; another third at 300k-600k. THE TWO-RUN RULE SAYS 300k; the practice averaged 460-510k with a third of the calls
  past 600k (the docket's run went to 610k, RUN A to 724k on 09-19 before "Get ready to compact"). At 460k a call costs $0.69 in reads alone;
  410 calls a day is $283 in reads before anything is typed.
- **OUTPUT 17%.** 14.0M tokens over nine days; 613 calls over 5k output carry 73% of it (the typed runner parts, the dockets' verdict rows,
  the records). The largest single output 64k — the output limit was hit three times (a typed runner part), each continuation a full re-write.

## 2. WHAT THIS SAYS ABOUT THE GROWTH

The program's size does not raise the price of a call — the CONTEXT does, and the WAITS do. As the tape and the chain grew (the tape 28 s → 235 s
with the cache off; the chain 18-45 min; the positions table 7 min; the sweep 6 min), every wait crossed the five-minute line and the whole
context was re-written on the other side. The reading itself is cheap: the 1,048-row docket entered the context once (~90k tokens, $1.35 at the
yardstick as new input); what cost was carrying it in a 500k context for the next 300 calls. The typed prose — the design (~25 KB), the AS BUILT
(~10 KB), the records in fourteen files (~30 KB), the commit message (10 KB) — is output at 17% of the bill; its fixed part per sitting is under
5% of the bill. "One book at a time and then integrate" would trim that fixed part and would not touch the two levers that carry 80%.

## 3. THE OPTIONS (each a token count; the savings are projections from the measured split)

- **A. THE CACHE LAW — no big context waits past five minutes.** (1) Every long job (the chain, the tape, the recorder, the positions
  table, the sweep) runs in the background at the END of a run, and the run ENDS at its clean point before the wait; the next run starts at
  ~30k after the reread and reads the summary. (2) Before any pause by the owner: the clean point and the compaction first, the break after.
  (3) The owner checks the plan's overage state — in overage the TTL is five minutes; out of it, an hour. Projected saving: most of the 169
  re-writes — about 30% of the bill.
- **B. THE 300k CAP KEPT — compact at every clean point, never past 400k.** The rule exists (the two-run rule); the practice broke it. A
  compaction costs one summary (~15k output, ~$1) and one re-write of the new context (~150k, ~$3) — against 100 calls at 700k ($105 in reads
  alone, $30 per re-write). Projected: reads and writes roughly halved — another 25-30% of the bill.
- **C. FEWER CALLS — one call per pipeline step, none to verify what the chain verifies.** 410 calls a day at $0.69 in reads each. The sheet's
  records in one call is already the form; the same for the probes, the types, the parts (one assemble-and-run), the docket's chunks (larger
  chunks, fewer calls). Projected: a quarter to a third fewer calls — 10-15%.
- **D. THE RECORDS AS A CARD — one YAML of the sitting's facts, fourteen files rendered by fixed templates.** The prose of the same sitting is
  typed fourteen times today; the commit messages run 10 KB. Projected: ~5% of the bill, and no more output-limit continuations.
- **E. BOOK-AT-A-TIME (or PORTION-AT-A-TIME) INTEGRATION.** Read and compile the chapters, integrate (the tape's literals, the checkpoints,
  the dispositions, the chain, the records) once per portion or per book. It cuts the fixed overhead per chapter by the batch size and the
  chain's waits with it; it does not cut the context per call or the reads. The risk: a slip found at integration after ten chapters is
  ten chapters wide (the tape 10/10 on the first run comes from integrating each chapter at once). A middle form: integrate per PORTION (two
  to four chapters). Projected: 5-10% at book grain, less at portion grain — a process choice more than a cost lever.
- **F. A CHEAPER MODEL FOR THE MECHANICAL TAIL.** The docket's verdicts, the design and the cells need the strongest model; the recorder, the
  stitcher, the copier, the records writer's run and the commit message do not. The harness allows a model switch mid-session; a cheaper
  model's cache reads cost a fifth. The risk: the mechanical tail has needed judgment when a print diverged (the retypes). The owner's call.
- **G. WHAT WOULD NOT HELP.** Fewer shelf rows (the whole-row rule stands and the rows are cheap to read once); shorter runners (output is
  17%); a shorter chain (its minutes cost nothing — only the wait across them does, which A removes).

## 4. THE PROJECTION

A + B + C together: the same work at roughly a THIRD of today's price per chapter — from ~$1,000 to ~$300-400 at the owner's rate. A alone is
the largest single lever and needs no new instrument: it is the order of the steps and where the clean point falls. B is a discipline the rule
already names. C is a habit. D and E are process choices with small savings; F is the owner's.

## 5. THE FIRST DECISION ASKED (one at a time)

Whether to adopt A — THE CACHE LAW — as a standing rule: every long job at the end of its run, the clean point before the wait, the compaction
before a break; and the owner to check the plan's overage state. Nothing changes until his word.

## 6. THE RULING (2026-09-20)
"Yes I like a b and c. Do you agree? Will that save money not lose quality" — agreed: the three change WHEN things happen and HOW MANY calls, not what is read, typed or gated. "What if we remove the cap for B" — the pile keeps its rent (reads 37%); the cap at 400k recommended as one compaction per sitting. **"Let's go to 400 a b and c" — RULED: A THE CACHE LAW, B THE 400k CAP, C FEWER CALLS.** Written into the recovery page, RECORD_FORMS, THE_STEPS, GATES_CHAIN.md, the map, THE_BRIEFING, the state doc (#199 addendum 4), the addenda §53, the memory.

## 7. THE AMENDMENT (2026-09-20, the evening — after sitting 10's tail)
The owner: "Let's set the cutoff at 600". RULE B AMENDED: a run ends at the clean point nearest 600k, never past 650k (400k / 450k until then). The occasion: chapter 12's tail left the context at 350k with the compile's RUN A ahead; under 400k the run would have waited for a compaction. A and C unchanged. Written into the recovery page, RECORD_FORMS, THE_STEPS, the map's rules section, THE_BRIEFING, the state doc (#200 addendum 3), the addenda §55, the memory.
