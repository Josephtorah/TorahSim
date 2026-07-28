# Pass 02 — Top root families that glue BR pairs

**Date:** 2026-07-26 · **Status:** hub roots identified

## Search
Count how often each content root appears as shared glue on a BR co-cite edge.

## Top 20 roots by # of BR edges they glue

| Root | BR edges | Corpus verses w/ root | Of which petihah edges | Top BR chapters |
|------|--------:|----------------------:|-----------------------:|-----------------|
| יספ | 149 | 400 | 0 | [[91, 31], [86, 22], [84, 15], [92, 15]] |
| עקב | 111 | 363 | 2 | [[73, 12], [74, 12], [75, 11], [80, 8]] |
| שמימ | 77 | 395 | 11 | [[1, 14], [17, 13], [12, 7], [6, 6]] |
| רעב | 58 | 123 | 0 | [[64, 22], [25, 21], [40, 7], [90, 6]] |
| אור | 54 | 237 | 9 | [[12, 21], [1, 6], [11, 6], [42, 6]] |
| ליל | 33 | 229 | 0 | [[52, 10], [74, 10], [6, 3], [43, 3]] |
| רחל | 33 | 48 | 0 | [[74, 16], [70, 6], [71, 3], [73, 3]] |
| פרעה | 30 | 230 | 0 | [[90, 7], [40, 6], [88, 6], [89, 4]] |
| שחה | 28 | 172 | 0 | [[56, 21], [50, 1], [66, 1], [75, 1]] |
| צחק | 28 | 113 | 0 | [[53, 12], [64, 4], [65, 3], [56, 2]] |
| כוס | 28 | 34 | 0 | [[88, 28]] |
| אהל | 24 | 341 | 6 | [[35, 10], [48, 9], [41, 1], [45, 1]] |
| עצה | 23 | 299 | 0 | [[12, 10], [19, 7], [15, 1], [21, 1]] |
| מואב | 23 | 172 | 0 | [[41, 21], [51, 1], [74, 1]] |
| צאנ | 22 | 249 | 0 | [[70, 6], [75, 4], [74, 2], [22, 1]] |
| שמש | 21 | 171 | 1 | [[68, 11], [98, 6], [6, 1], [48, 1]] |
| חכמ | 21 | 290 | 0 | [[89, 15], [12, 1], [27, 1], [44, 1]] |
| פרה | 21 | 309 | 0 | [[97, 10], [82, 3], [53, 2], [12, 1]] |
| באר | 21 | 96 | 0 | [[64, 16], [62, 3], [54, 1], [94, 1]] |
| זרע | 19 | 380 | 0 | [[12, 3], [53, 3], [41, 2], [11, 1]] |

## Summary
Hub roots are a mix of:
1. **Semantic packages** we care about: **אור** (light, 54 edges), **אמנ** (18), **חכמ** (21), **שמש** (21)
2. **Narrative name/place hubs**: פרעה, מואב, רחל, עקב — high because BR retells stories with repeated names (still “root/name identity,” different from polyroot *sense* packages)
3. Possible **extraction noise**: e.g. **שמימ**, **יספ** may be over-long lemma keys — treat semantic hubs as primary

## Finding
The link graph has **clear hubs**. Not one amon-only story — light, wisdom, covenant names, famine (**רעב** 58), bow/worship (**שחה** 28) all reappear.

## Next search
Deep-dive **אור** (light) — Theory 6 + T9 together.
