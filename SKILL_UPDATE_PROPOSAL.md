# Proposed update to `~/.claude/skills/the-humanizer-targz/SKILL.md`

Status: **drafted**, awaiting Edit-tool recovery. The auto-mode safety classifier was intermittently unavailable for `~/.claude/skills/` and `Bash` at 2026-05-25 ~14:50. This file is the exact text to insert, ready to apply.

Skill currently at **v1.1** (2026-05-25). Target: **v1.2**.

## Why this update exists

Two failure modes surfaced in Batch A of the targz.fr-2025 exhibition rewrite:

1. **Inventing facts** — I claimed "posters and plotted originals shown side by side" for Blended Squares 2021. You said it was false.
2. **Stripping substance** — I rewrote a 3-sentence Blended Squares paragraph down to "Blended Squares series." Deleted: overlapping squares, color blending, pen-plotted, simple-rules-complex-output, ongoing series — all of which were stated in the original.

The skill's current Step 6 rule 1 ("Never add ideas not in the original. Never remove substance.") was insufficient because it didn't tell me HOW to tell substance from filler. The fix is mechanical: AI texture lives in **verbs**. Facts live in **nouns**. Cut the verbs, keep the nouns.

## Change 1 — Changelog row (insert at top of changelog table)

```markdown
| **v1.2** | **2026-05-25** | Hardened the substance-preservation logic after a Batch A failure on `targz.fr-2025`. Two failure modes captured: stripping load-bearing nouns alongside filler verbs (Fill The Blank lost "visitors complete letterforms", "compose text", "work grows over the run"); inventing facts when the original was vague (Blended Squares got "posters and plotted originals shown side by side" which was false). Two new sections: **Step 5.5 (Substance Decomposition)** — build a fact list before any rewrite; **Step 6.5 (Length sanity check)** — rewrites should be 40–70% of original length unless the original was truly empty. Step 6 rule 0 added: **"Cut the verb, keep the noun"** with explicit transformation table for `explores / creates / transforms / showcases / highlights / demonstrates / represents` and abstract-noun wrappers (`interplay between / nature of / intersection of`). |
```

## Change 2 — New Step 5.5 (insert between current Step 5 and Step 6)

```markdown
---

## Step 5.5: Substance Decomposition (run BEFORE writing the rewrite)

AI-textured prose hides real nouns behind filler verbs. Before stripping anything, build this table from the original paragraph:

| Claim from original | Source / status |
|---|---|
| (one fact per row) | one of: verified from frontmatter / verified from filename / verified from another Julien post / stated in original (unverified) / inferred from context (flag with [VERIFY]) / clearly invented (drop) |

Decomposition rules:

1. **Find every noun** in the AI-textured paragraph. Most are facts.
2. **Find every verb.** Most are filler.
3. Distinguish three categories per phrase:
   - Concrete noun (a thing, a process, a measurement) → keep.
   - Abstract noun that restates a concrete one ("creative process", "participatory experience", "complex system", "foundational moment") → drop.
   - Filler verb ("explores", "creates", "transforms", "showcases", "highlights", "demonstrates", "represents-as-meaning") → drop the verb, but **keep its direct object**.

Worked example — Fill The Blank original:

> "Interactive installation using Billund Mono Sans font, engaging viewers in the creative process. This exhibition transforms typography into a participatory experience, where visitors contribute to the completion of letterforms and textual compositions. The project explores the boundaries between predetermined structure and user input, creating a collaborative artwork that evolves throughout the exhibition period."

Decomposition table:

| Claim | Source |
|---|---|
| Interactive installation | stated in original |
| Uses Billund Mono Sans font | stated; verified from `_posts/bits/2018-01-01-billund-mono-sans.md` |
| Billund Mono Sans is Lego-derived | verified from another Julien post |
| Visitors complete letterforms | stated ("contribute to the completion of letterforms") |
| Visitors compose text | stated ("textual compositions") |
| The piece grows over the exhibition run | stated ("evolves throughout the exhibition period") |

AI filler to cut (no concrete claim): "engaging viewers in the creative process", "transforms ... into a participatory experience", "explores the boundaries between predetermined structure and user input", "creating a collaborative artwork".

Output the decomposition table in your review so Julien can correct it before the rewrite happens. If the table is empty (no concrete claims), flag the original as truly factually empty before deciding to strip the paragraph.
```

## Change 3 — New rule 0 inside Step 6 (prepend to existing rules)

In the current Step 6:

```markdown
## Step 6: Rewrite

Universal rules:
1. **Never add ideas not in the original.** Never remove substance. Preserve every argument.
2. Fix all flagged typos.
[...]
```

Insert as new rule 0, BEFORE current rule 1:

```markdown
0. **Cut the verb, keep the noun.** AI texture lives in verbs. Facts live in nouns. After the Step 5.5 decomposition table, apply this transformation pattern:

| AI verb structure | Cut | Keep |
|---|---|---|
| "explores [X]" | "explores" | X |
| "creates [X]" | "creates" | X |
| "transforms [Y] into [X]" | "transforms ... into" | Y and X |
| "showcases [X]" | "showcases" | X |
| "presents [X]" | "presents" | X |
| "features [X]" | "features" | X |
| "highlights [X]" | "highlights" | X |
| "demonstrates how [X]" | "demonstrates how" | X |
| "invites viewers to [X]" | "invites viewers to" | X (if X is concrete) |
| "represents [X]" (meaning-verb) | the whole structure | X (if X is concrete) |
| "exploring the intersection of [X] and [Y]" | wrapper | X, Y |
| "the interplay between [X] and [Y]" | wrapper | X, Y |
| "the relationship between [X] and [Y]" | wrapper | X, Y |
| "the boundaries between [X] and [Y]" | wrapper | X, Y |
| "the nature of [X]" | wrapper | X |
| "engaging viewers in [X]" | wrapper | X (if X is concrete) |
| "offering [Y] a unique perspective on [X]" | the whole structure | usually cut entirely |

After cutting verbs, the remaining nouns form the rewrite. Add Julien's punctuation (period-led short sentences) and voice (terse, dry, factual).

Worked example — Blended Squares:

Original (3 sentences): "Exhibition featuring the Blended Squares series, showcasing poster and pen plotter art. This collection explores the interplay between overlapping geometric forms, creating visual rhythms through systematic color blending and precise mechanical drawing. The exhibition highlights the evolution of the Blended Squares series, demonstrating how simple rules can generate complex visual harmonies when executed with mechanical precision."

Verb-cut, noun-keep:
- "featuring the Blended Squares series" → keep "Blended Squares series"
- "showcasing poster and pen plotter art" → keep "posters and pen-plotted prints" (flag [VERIFY])
- "explores the interplay between overlapping geometric forms" → keep "overlapping squares"
- "creating visual rhythms through systematic color blending and precise mechanical drawing" → keep "color blending, pen-plotted"
- "highlights the evolution of the Blended Squares series" → keep "ongoing series"
- "demonstrating how simple rules can generate complex visual harmonies" → keep "simple rules, complex output"

Plain rewrite: "Blended Squares series. Posters and pen-plotted prints. Overlapping squares, color blending. Simple rules, layered output. Ongoing series."

(Original: ~70 words. Rewrite: ~20 words. ~28% of original. Length check below will flag this as borderline-too-short, so check the table: is every noun preserved? Yes. So 28% is fine here because the original had repetition.)
```

Then renumber existing rules: 1 → 1, 2 → 2, etc. (No conflict; rule 0 is prepended.)

## Change 4 — New Step 6.5 (insert after Step 6)

```markdown
---

## Step 6.5: Length sanity check

After writing the rewrite, compare its length to the original:

- **40–70% of original length** → correct range for AI-texture stripping.
- **<40% of original length** → you probably deleted nouns. Re-open the Step 5.5 decomposition table. Every "verified" and "stated in original" claim should appear in the rewrite. Stripping is fine; deleting facts is not.
- **>70% of original length** → you probably kept filler verbs. Re-scan with the Step 6 rule 0 table.

Edge case: the original was truly empty of facts (rare for Julien's content but it happens with AI-stub `description:` frontmatter fields like "Created: November 13, 2022 2:03 PM"). In that case, the rewrite can be shorter. Flag explicitly: "Original contained no concrete facts; rewrite cannot exceed the title."
```

## Change 5 — Update Step 6 worked example reference

The "Artwork Description rewrite rules" subsection of current Step 6 already has good Julien-specific guidance. No change needed there.

## Summary of net additions

- 1 changelog row.
- 1 new section: Step 5.5 (Substance Decomposition) — ~40 lines.
- 1 new rule: Step 6 rule 0 (Cut verb, keep noun) — ~30 lines with table.
- 1 new section: Step 6.5 (Length sanity check) — ~10 lines.

Total: roughly +80 lines to the skill. The skill stays under 400 lines.

## Application

When the classifier is back up, I'll apply this via Edit. If you want to apply manually now, paste each Change above into the appropriate location in `~/.claude/skills/the-humanizer-targz/SKILL.md`.

## What changes downstream

After this skill update, future runs of `/the-humanizer-targz` will:
1. Always produce a decomposition table BEFORE rewriting.
2. Cut filler verbs but preserve their direct objects (the actual facts).
3. Sanity-check rewrite length and flag suspicious over-stripping.
4. Match Julien's voice (period-led short sentences from preserved nouns) — which is what the skill targets anyway.

The Batch A rewrites in `batch-a-exhibitions-review.md` were drafted under the OLD skill. After the skill update, I'll redo all 11 with the new method.
