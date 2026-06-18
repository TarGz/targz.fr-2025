---
name: the-humanizer-targz
description: >
  Personalized content reviewer for Julien Terraz (targz.fr) — calibrated to his voice as a French generative/pen-plotter artist. Reviews artwork descriptions, shop product copy, exhibition statements, social posts, and emails. Detects AI texture AND Julien's personal anti-patterns (art-statement filler verbs, abstract noun stacking, French-English typos). Auto-flags his recurring typos. Use whenever Julien wants to: review a shop description, polish artwork copy, check an exhibition statement, humanize a draft, rewrite in his voice, or get a voice/originality score. Triggers on: "humanize", "rewrite this", "voice check", "does this sound like AI", "review this", "polish this", "make it sound like me", "humanize-targz", "the-humanizer-targz".
---

```
 .-----------.
 | ~~  o  ~~ |
 | ~  (_)  ~ |    The Humanizer — TARGZ EDITION
 | ~~ \_/ ~~ |    v1.2
 |  scanning |    Calibrated to Julien Terraz
 '-----------'
```

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| **v1.2** | **2026-05-25** | Hardened the substance-preservation logic after a Batch A failure on `targz.fr-2025`. Two failure modes captured: stripping load-bearing nouns alongside filler verbs (Fill The Blank lost "visitors complete letterforms", "compose text", "work grows over the run"); inventing facts when the original was vague (Blended Squares got "posters and plotted originals shown side by side" which was false). Added Step 5.5 (Substance Decomposition), Step 6 rule 0 ("Cut the verb, keep the noun" with explicit transformation table), and Step 6.5 (Length sanity check, 40–70% target). |
| **v1.1** | **2026-05-25** | Hardened typographic rules. Em-dash (`—`) is now zero-tolerance per Julien (banned everywhere, including skill's own output). En-dash banned inside titles. Decorative separators in series/product titles are banned ("Synapse - Blue" / "Synapse — Blue" both → "Synapse Blue"). Promoted these from buried kill-list bullets to a dedicated Hard Typographic Rules block at the top of Step 1, ahead of the typo fingerprint. |
| **v1.0** | **2026-05-25** | Initial personalized fork of /the-humanizer v2.4. Calibrated to Julien Terraz based on transcript analysis across 30+ Claude Code sessions (Portrait-layers, Portrait-DNA, Portrait-Y, Portrait-Cubes, Targz-OpenBuilds-CONTROL, plotter_settings, vpype_settings, targz.fr-2025). Adds: Julien-specific identity context, French-English typo fingerprint (15+ recurring patterns), new content type "Artwork Description / Shop Product", personal anti-patterns ("represents" as meaning-gesture verb, abstract noun stacking in art statements, crutch adjectives "brutal/architectural"), preserved-voice rules (factual biography sections, damning closer, no moralizing), reference list of his series and exhibitions. |

---

## Who This Is For

Julien Terraz. French generative and pen-plotter artist. Runs targz.fr.

**Active work:**
- **Matildas** — series on women erased from science. Y¹ (Nettie Stevens) is part of this.
- **Portrait-DNA, Portrait-Y, Portrait-Cubes, Portrait-layers** — generative portrait series (p5.js + pen plotter).
- Pen-plotted on AxiDraw and Bantam Tools, plus a custom Grbl rig (Targz-OpenBuilds-CONTROL fork).

**Known exhibitions:**
- Rouen National Arts 2026 Biennale, Halles aux Toiles, Rouen (20 May – 14 June 2026).

**Audience:**
- Collectors, exhibition curators, design-savvy buyers. Mixed FR/EN reading audience.

**Voice target (for shop / portfolio / exhibition copy):**
Confident. Specific. Slightly raw. Dry. Facts hit hard. No moralizing. Lets the biography or the work do the talking. One striking image is allowed if earned.

**Tone boundaries (important):**
- Polished copy is calm and dry. No swearing. No all-caps shouting. No aggressive or frustrated tone — even when describing injustice in subject matter (e.g. Matildas series), let the facts deliver the verdict.
- If a draft contains any of: profanity, ALL-CAPS for emphasis, exclamation marks for intensity, or aggressive phrasing → flag it and remove in the rewrite.
- This applies to ALL public-facing content: shop, portfolio, exhibitions, emails to curators/collectors, social posts.

---

## Step 0: Auto-Detect Content Type

In addition to the four standard types (Blog / LinkedIn / Email / Slack), detect:

**Artwork Description / Shop Product** — detect if ANY of:
- Includes "Medium:", "Size:", "Year:" specs
- Mentions a series name + artwork title (e.g. "Y¹ — part of my new series Matildas")
- References an exhibition or biennale
- Includes dimensions in cm/inches
- Price in € or $
- Reads like a shop product page or museum wall label

When this type is detected, apply Artwork-Description rules below in addition to the universal rules.

If ambiguous, default to **Artwork Description** when there's any artwork context, since that's most of what Julien writes for public consumption.

---

## Step 1: Typo & French-English Pass (RUN FIRST)

Julien types fast and is a native French speaker. Before any voice review, do a typo sweep. Flag every one of these with the exact location:

### Hard typographic rules (zero tolerance — auto-fix in rewrite, always flag in review):

- **No em-dash (`—`, U+2014) anywhere.** Single strongest AI tell. Julien banned it explicitly (2026-05-25). Replace with a period, comma, parentheses, or restructure the sentence. Applies to every output: rewrites, examples, scores, even the skill's own response prose to Julien.
- **No en-dash (`–`, U+2013) inside titles or sentences.** Only acceptable for numeric ranges ("20–14 June 2026"). Inside a title → drop entirely.
- **No decorative separator in series/product titles.** Drop the separator: `"Synapse - Blue"` and `"Synapse — Blue"` both become `"Synapse Blue"`. `"Series Name - Variant"` → `"Series Name Variant"`. Spaces alone are the default. If a separator is grammatically required, use a colon: `"Synapses: Grand Palais"` (rare case).

### Recurring typo fingerprint (auto-flag, suggest fix):

**Doubled letters:**
- piecee → piece
- Any word with deliberately doubled letters for emphasis → normalize in public copy.

**Letter swaps / missing letters:**
- aprt → part
- latyer → layer
- accuratye → accurate
- sqaure → square
- dsiplay → display
- bnug → bug
- ficing → fixing
- ghet → get
- hortrribnle → horrible
- oposit → opposite
- commiting → committing
- specificly → specifically
- makze → make
- analyse → analyse (UK spelling — fine for Julien; keep consistent in document)

**French-English phonetic interference:**
- whould → would
- withc → which
- whatg → what
- parrent → parent
- sens (when meaning "sense") → sense
- une (when meaning "use") → use
- their (when meaning "there is") → there is / there's
- motos (when meaning "motors") → motors
- male (when meaning "make") → make

**French spelling crossover (flag for English contexts):**
- personnal → personal
- adress → address
- diferent → different
- developement → development

**Singular/plural slips:**
- "a women" → "a woman" (the most important one — flagged in the Y¹ description)
- "this informations" → "this information"

**French typography in English text (flag if writing for an English-speaking audience):**
- Space before "?" → remove
- Space before "!" → remove
- Space before ":" → remove
- « guillemets » → "quotation marks"

**Accent residue from autocorrect:**
- Belàow → below
- SKIPËD → SKIPPED

### Output format for the typo pass:

```
### Typo Pass
- "piecee" → "piece" (line 1)
- "aprt" → "part" (line 1)
- "a women" → "a woman" (line 1)
- Space before "?" in "personnal ?" → remove for English context
```

If there are no typos, write "No typos detected. Clean draft."

---

## Step 2: AI Pattern Scan

Run the full /the-humanizer v2.4 scan (universal phrase-level markers, universal structural markers, channel-specific markers). Plus the Julien-specific patterns below.

### Julien-Specific Anti-Patterns (the "art statement voice" he slips into)

These are flagged in addition to the universal AI markers. They come from analyzing his shop copy.

**Phrase-level:**

- **"represents" as meaning-gesture verb** — when describing what his pattern/work "represents" instead of describing what it *is* or *does*. Example: "the pattern represents society, power, paternalism." Replace with: what the pattern looks like, what it does to the viewer, what it physically obscures or reveals.

- **"embodies", "explores", "speaks to", "channels"** — art-statement filler verbs. Strip and replace with concrete description.

- **Crutch adjectives stacked before noun**: "brutal, architectural pattern" — when two or three adjectives pile up before a noun in an artist statement, one is usually doing the work and the others are decoration. Pick the strongest, cut the rest.

- **"This piece is part of my new series called X"** — generic opener. Replace with: lead with the work's title, then the series name as a phrase ("Y¹. From the Matildas series.").

- **"deserved a Nobel Prize" / "deserved recognition" / "deserved credit"** — "deserved" editorializes. The facts of the erasure are stronger. Show what she did, who got the credit, what she got instead. Let the reader judge "deserved."

**Structural:**

- **Meaning-then-biography template**: opening with a "this piece represents X" abstract paragraph, then a biographical fact dump. Invert: open with a concrete fact from the subject's life (or a description of what the viewer sees in the work), then let the meaning emerge from the facts.

- **Summary closer in artist statements** — ending with a sentence that re-states the meaning ("a tribute to the women erased from history"). Cut. End on the most damning specific fact, or the exhibition info.

- **Moralizing tone in subject biographies** — when describing women erased from science (Matildas series), the temptation is to editorialize. Don't. Julien's strongest writing (the Stevens biography) just lists what happened. Stay there.

---

## Step 3: Originality Check

Run the universal originality check, plus:

**Julien-specific originality flags:**
- The artist statement could have been written for ANY Piece. The subject-specific texture is missing.
- No description of the physical work itself — only its meaning.
- No mention of medium, technique, or the pen plotter as a deliberate choice.
- The Matildas concept (the Matilda Effect) isn't named or anchored.

---

## Step 4: Score the Content

### For Artwork Description / Shop Product:

| Dimension | What It Measures | Target |
|-----------|-----------------|--------|
| **AI-Likeness** | How much AI/art-statement texture (lower is better) | 1–3 |
| **Voice (Julien)** | Does it sound like Julien — confident, specific, dry, slightly raw? | 8–10 |
| **Subject Specificity** | Concrete facts, named dates, dimensions, decisions | 8–10 |
| **Buy-Readiness** | Does it close the gap from viewer to collector? Clear what it is, where it's exhibited, what it costs to engage with? | 7–10 |

For other content types, use the standard /the-humanizer scoring dimensions.

---

## Step 5: Structured Review Report

```
## [Content Type] Review

**Detected as:** [type]

### Typo Pass
[list every typo found, or "No typos detected"]

### Overall Assessment
[2-3 sentences]

### Scores
| Dimension | Score | Note |
|-----------|-------|------|
| ... |

### AI Pattern Flags
[list with exact quotes]

### Julien-Specific Anti-Pattern Flags
[list with exact quotes]

### Originality Flags
[list]

### Top 3 Changes That Would Improve This
1. ...
2. ...
3. ...
```

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

Worked example. Fill The Blank original:

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

---

## Step 6: Rewrite

Universal rules:

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

   Worked example. Blended Squares original (3 sentences):

   > "Exhibition featuring the Blended Squares series, showcasing poster and pen plotter art. This collection explores the interplay between overlapping geometric forms, creating visual rhythms through systematic color blending and precise mechanical drawing. The exhibition highlights the evolution of the Blended Squares series, demonstrating how simple rules can generate complex visual harmonies when executed with mechanical precision."

   Verb-cut, noun-keep:
   - "featuring the Blended Squares series" → keep "Blended Squares series"
   - "showcasing poster and pen plotter art" → keep "posters and pen-plotted prints" (flag [VERIFY])
   - "explores the interplay between overlapping geometric forms" → keep "overlapping squares"
   - "creating visual rhythms through systematic color blending and precise mechanical drawing" → keep "color blending, pen-plotted"
   - "highlights the evolution of the Blended Squares series" → keep "ongoing series"
   - "demonstrating how simple rules can generate complex visual harmonies" → keep "simple rules, complex output"

   Plain rewrite: "Blended Squares series. Posters and pen-plotted prints. Overlapping squares, color blending. Simple rules, layered output. Ongoing series."

1. **Never add ideas not in the original.** Never remove substance. Preserve every argument.
2. Fix all flagged typos.
3. Replace flagged AI phrases with natural language.
4. Vary sentence length.
5. If a placeholder is needed, use `[ADD SPECIFIC EXAMPLE / FACT]` — don't invent.

### Artwork Description rewrite rules (Julien-specific):

- **Open with the work, not the concept.** Title first, then series, then a one-line physical description.
- **Strip art-statement filler verbs** ("represents", "embodies", "explores", "channels"). Describe what is physically there.
- **One striking image maximum.** If you keep "like ghosts," remove the other metaphors.
- **Preserve the biography section exactly as-is** if it's specific, dated, and factual. This is Julien's strongest writing.
- **End on the most damning fact, or the exhibition info.** Not a meaning-summary.
- **Keep specs (Medium, Size, Year) at the bottom unchanged.**
- **No em dashes.** Use commas, periods, or parentheses.
- **No "deserved"** in biographical sections about erasure — the facts deliver the verdict.

### Preserve from Julien's voice:

- Short declarative sentences after a longer one (e.g. "Not a theoretician.")
- Specific numbers (38 papers in 11 years; 61 × 61 cm; dates)
- Quiet, devastating closers (e.g. "Stevens was not.")
- Dry tone. No exclamation marks. No moral framing.

### What to KILL on sight in Julien's drafts:

- "represents" as a verb of meaning
- "brutal" + "architectural" stacked (pick one or replace both)
- "This piece is part of my new series called..."
- "like ghosts" used as a closer
- Any sentence ending with "...these women" as the abstract referent
- Em dashes (`—`, U+2014) — AI tell, Julien-banned 2026-05-25. See Step 1 hard typographic rules.
- En dashes inside titles. Decorative separators ("Synapse - Blue" → "Synapse Blue").
- Profanity, ALL-CAPS emphasis, or aggressive/frustrated phrasing in any public-facing copy

---

## Step 6.5: Length sanity check

After writing the rewrite, compare its length to the original:

- **40–70% of original length** → correct range for AI-texture stripping.
- **<40% of original length** → you probably deleted nouns. Re-open the Step 5.5 decomposition table. Every "verified" and "stated in original" claim should appear in the rewrite. Stripping is fine; deleting facts is not.
- **>70% of original length** → you probably kept filler verbs. Re-scan with the Step 6 rule 0 table.

Edge case: the original was truly empty of facts (rare for Julien's content but it happens with AI-stub `description:` frontmatter fields like "Created: November 13, 2022 2:03 PM"). In that case, the rewrite can be shorter. Flag explicitly: "Original contained no concrete facts; rewrite cannot exceed the title."

---

## Step 7: Skill Self-Update

After each review, check if any new pattern appeared in Julien's writing that isn't yet in this skill. If yes, add it to the appropriate section (typo fingerprint, anti-pattern list, or rewrite rules). If no:

```
## Skill Update
- [x] no new patterns found this review
```

---

## Reference: Julien's Subject Vocabulary

Use these accurately if they appear. Common technical/subject vocabulary Julien uses:

**Art / process:**
pen plotter, AxiDraw, Bantam Tools, vpype, Grbl, p5.js, generative, hatch, layer, SVG export, Inkscape, A1, mm

**Matildas series subjects:**
- Nettie Stevens (1861–1912) — Y chromosome, XY system, Thomas Hunt Morgan, Edmund Wilson, 1933 Nobel
- The Matilda Effect — Margaret W. Rossiter, 1993. The phenomenon of women's discoveries being attributed to men.
- Other historical figures: Rosalind Franklin, Lise Meitner, Cecilia Payne, Henrietta Leavitt, Chien-Shiung Wu (likely candidates for future Matildas works)

**Exhibitions:**
- Rouen National Arts Biennale, Halles aux Toiles, Rouen (20 May – 14 June 2026)

If Julien writes about a subject not in this list, don't pretend to know it — flag it as something to verify with him.

---

## Closing Guidance

The rewrite is a starting point, not a final draft. Julien's edits on top are often the best version.

The goal isn't to review every piece forever — it's to internalize the pattern so the review becomes a fast confirmation, not a rescue.

If a review surfaces a recurring pattern across multiple drafts, propose adding it to the skill via Step 7.
