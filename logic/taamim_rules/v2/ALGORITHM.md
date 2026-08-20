# Ta'amim parse algorithm — v2 (prose + mandatory glue bricks)

**Version:** `v2`  
**System:** prose (Torah + Prophets + most Writings; not Psalms/Proverbs/Job poetry system)  
**Parent:** v1 continuous dichotomy  
**Change:** **Glue is mandatory.** Terminal units are multi-word bricks, not flat n-ary lists of single words.

---

## Two layers (required)

### Layer A — Glue → terminal bricks

Walk words left → right:

1. Start an empty brick.  
2. Append each word to the current brick.  
3. When the word’s structural mark is **disjunctive**, **close** the brick (this word is the brick’s head / end mark) and start a new brick.  
4. Conjunctive / zero_conjunctive words **never** close a brick; they only glue into the next disjunctive.  
5. After the last word: if a brick is still open, close it (should normally end with silluq / disjunctive).

Each brick is a **terminal unit** for the dichotomy:

- 1 word ending in a disjunctive, **or**  
- several glued words ending in a disjunctive  

**The dichotomy must not flatten glued words as sibling leaves under an n-ary phrase.**

### Layer B — Nest → binary tree of bricks

Same continuous binary dichotomy as v1, but the sequence is **bricks**, not raw words:

1. If 1 brick → return a **leaf** whose `words` = all word indices in that brick.  
2. Interior candidates = brick indices `i` in `0 .. m-2` (every brick ends with a disjunctive under normal prose).  
3. Brick rank = rank of the **last word** of the brick (the disjunctive head).  
4. Strongest rank = minimum rank among interior bricks; **leftmost** brick with that rank.  
5. Split **after** that brick: left = bricks `0..k`, right = bricks `k+1..m-1`.  
6. Recurse. Every internal node is **binary** (exactly 2 children).

---

## Rank scale

Unchanged from v1 — see `ranks_prose.yaml`.

---

## Poetry

Same as v1: refuse poetry books unless `--force-prose` (debug only).  
True poetry ranks → later version.

---

## Failures

- Empty verse  
- Unknown mark  
- Poetry without force  
- **Invariant fail:** any phrase node with arity ≠ 2 (v2 must be pure binary after glue)

---

## Display contract

- Leaves may show **multiple** Hebrew words (the brick).  
- `--tree` must show nested binary structure of bricks.  
- **Never** emit a flat n-ary phrase of single-word leaves for a conjunctive chain (that was v1 “flattening”).

---

## Changelog

| Ver | Note |
|-----|------|
| v1 | Word-level dichotomy; conj chains as n-ary phrases of leaves |
| **v2** | **Glue bricks first, then binary dichotomy on bricks (mandatory)** |
