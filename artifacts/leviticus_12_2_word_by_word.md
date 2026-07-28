# Lev 12:2 Word-by-Word → Logic Mapping

**Provenance:** Web Grok recovery batch (saved into `artifacts/`).

**Hebrew**: דַּבֵּ֨ר אֶל־בְּנֵ֣י יִשְׂרָאֵל֮ לֵאמֹר֒ אִשָּׁה֙ כִּ֣י תַזְרִ֔יעַ וְיָלְדָ֖ה זָכָ֑ר וְטָמְאָ֖ה שִׁבְעַ֣ת יָמִ֑ים כִּימֵ֙י נִדַּ֣ת דְּוֹתָ֔הּ תִּטְמָֽא׃

| Phrase | Role | Logic |
|--------|------|--------|
| דַּבֵּ֨ר אֶל־בְּנֵ֣י יִשְׂרָאֵל֮ לֵאמֹר֒ | Header/setup (major disjunctive) | Context only |
| אִשָּׁה֙ כִּ֣י תַזְרִ֔יעַ וְיָלְדָ֖ה זָכָ֑ר | Condition pivot (strong disjunctive near "zachar") | **IF** `child_gender == "male"` |
| וְטָמְאָ֖ה שִׁבְעַ֣ת יָמִ֑ים | Consequence | `impurity_duration = 7 days` |
| כִּימֵ֙י נִדַּ֣ת דְּוֹתָ֔הּ | Reference | `niddah` rule |
| תִּטְמָֽא׃ | Implication | `status = impure` |

**Derived Logic**: IF male birth THEN 7 days impurity like niddah. All words accounted for in tree grouping (connectors stay structural; content phrases become variables).

**Justification**: Ta'amim hierarchical divisions; variables from delimited phrases only. Representation only — not autonomous law generation.
