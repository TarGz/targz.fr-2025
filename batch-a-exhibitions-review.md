# Batch A — Exhibitions Rewrite Review

11 exhibition posts. Original copy + proposed rewrite for each one. Edit the **REWRITE** blocks until they're factually correct, then I can apply the approved versions back into `_posts/exhibitions/*.md`.

## Approach (updated 2026-05-25)

After file 1 failed twice — once by inventing ("posters and plotted originals shown side by side" for Blended Squares) and once by over-stripping (deleted "visitors complete letterforms" because the surrounding prose sounded AI) — the method is now:

1. **Decompose the original.** List every factual claim it makes (separated from the AI filler).
2. **Tag each claim:** verified from frontmatter/filename/other Julien post / stated in original / inferred from context / clearly invented.
3. **Keep every fact**, in plain language. Drop only the filler verbs and abstract noun stacking.
4. **Never add** a claim that wasn't in the original or another Julien source.

Each rewrite below includes a **Substance decomposition** table so you can see what was kept vs. what was filler.

**Markers used in this file:**
- `[VERIFY: ...]` — claim I'm not sure about. Confirm, correct, or delete the sentence.
- `[INVENTED]` — I made this up from nothing. Delete or replace with a real fact.
- `[FACT FROM FRONTMATTER]` — pulled from the post's frontmatter (size, location, date).
- `[FACT FROM FILENAME]` — pulled from an image filename in the post (sizes, years, gallery names).
- `<!-- TODO: ... -->` — gap I think you should fill, doesn't ship publicly.

**Hard rules already applied:**
- No em-dashes (`—`).
- No "represents/embodies/explores/channels" filler.
- No "deserved", "like ghosts", "brutal architectural".
- French slips fixed.
- Singular/plural fixed.

**Files NOT rewritten:**
- `2026-02-11-art-capital.md` (file 10) — reference quality, leave verbatim.

## Status

- **File 1 (Fill The Blank)** is redone below with the new approach (substance preserved).
- **Files 2–9 and 11** still need to be redone with the substance-decomposition method — currently they're shown in the over-stripped form. Once you confirm File 1 reads right, I'll redo the rest.

---

## 1. Fill The Blank (2018-11-01) — REDONE 2026-05-25 with substance preserved

**File:** `_posts/exhibitions/2018-11-01-fill-the-blank.md`
**Detected as:** Exhibition statement.
**Scores:** AI-Likeness 9 / Voice 2 / Subject Specificity 3 / Buy-Readiness 3.
**Flags:** "engaging viewers in the creative process", "transforms typography into a participatory experience", "explores the boundaries between", "evolves throughout the exhibition period". 16 stock image alts.

### Substance decomposition of the original

The AI-textured original makes these factual claims (separated from the filler):

| Claim from original | Source / status |
|---|---|
| Interactive installation | stated in original |
| Uses Billund Mono Sans font | stated in original (and Billund Mono Sans is Julien's own Lego-derived typeface, confirmed in `_posts/bits/2018-01-01-billund-mono-sans.md`) |
| Visitors complete letterforms | stated: "visitors contribute to the completion of letterforms" |
| Visitors compose text | stated: "textual compositions" |
| The piece grows / evolves over the exhibition run | stated: "evolves throughout the exhibition period" |

AI filler in the original (drop, don't rewrite):
- "engaging viewers in the creative process"
- "transforms typography into a participatory experience"
- "explores the boundaries between predetermined structure and user input"
- "creating a collaborative artwork"

### Body — ORIGINAL
> Interactive installation using Billund Mono Sans font, engaging viewers in the creative process. This exhibition transforms typography into a participatory experience, where visitors contribute to the completion of letterforms and textual compositions.
> The project explores the boundaries between predetermined structure and user input, creating a collaborative artwork that evolves throughout the exhibition period.

### Body — REWRITE (substance preserved)
> Interactive installation built on Billund Mono Sans, my own Lego-derived typeface. Visitors complete the letterforms and compose their own text. The piece grows over the run.
>
> <!-- TODO: ADD Paris venue name, dates, anything specific to this show (what visitors actually built/wrote, scale, how the piece looked at the end). -->

**What changed vs my previous (too-stripped) rewrite:**
- Kept: "visitors complete letterforms" (was deleted before — that was the core of the work).
- Kept: "compose their own text" (was deleted before — also core).
- Kept: "the piece grows over the run" (was deleted before — defines why it's an *exhibition* of a *process*).
- Still dropped: every AI filler verb.
- Still didn't invent: nothing about Lego bricks at the install, nothing about what specific words visitors wrote.

### Image alts — ORIGINAL (16x)
"Typography Installation" / "Interactive Element" / "Font Details" / "Visitor Interaction" / "Process View" / "Letter Formation" / "Interactive Setup" / "Typography Process" / "User Engagement" / "Installation Detail" / "Collaborative Element" / "Exhibition Space" / "Interactive Display" / "Typography Evolution" / "Final Installation" / "Complete View"

### Image alts — REWRITE
All 16 → `Fill The Blank` (title only). If you want per-image alts that describe what each photo shows, you'd have to caption them yourself, since I haven't seen the photos.

---

## 2. Blended Squares Exhibition (2021-11-10)

**File:** `_posts/exhibitions/2021-11-10-blended-squares-exhibition.md`
**Detected as:** Exhibition statement.
**Scores:** AI-Likeness 9 / Voice 2 / Subject Specificity 2 / Buy-Readiness 3.
**Flags:** "explores the interplay", "creating visual rhythms", "demonstrating how simple rules can generate complex visual harmonies", "executed with mechanical precision".

### Body — ORIGINAL
> Exhibition featuring the Blended Squares series, showcasing poster and pen plotter art. This collection explores the interplay between overlapping geometric forms, creating visual rhythms through systematic color blending and precise mechanical drawing.
> The exhibition highlights the evolution of the Blended Squares series, demonstrating how simple rules can generate complex visual harmonies when executed with mechanical precision.

### Body — REWRITE
> Blended Squares series.
>
> <!-- TODO: ADD what was actually shown (number of pieces, format, medium, framing), the Paris venue name, dates of the run, what was specific about this exhibition vs. just showing the series elsewhere. Do NOT auto-rewrite this without your input — earlier I invented technique details (translucent layers stacked, overlap = third color) and that was wrong. -->

### Image alts — ORIGINAL (4x)
"Blended Squares Exhibition Overview", "Exhibition Gallery View", "Artwork Detail", "Final Exhibition View"

### Image alts — REWRITE
All 4 → `Blended Squares Exhibition` (just the title). [VERIFY: you can refine per-image once you confirm what's in each photo.]

---

## 3. Chunk of Maze (2022-08-31)

**File:** `_posts/exhibitions/2022-08-31-chunk-of-maze.md`
**Detected as:** Exhibition statement.
**Scores:** AI-Likeness 9 / Voice 1 / Subject Specificity 3 / Buy-Readiness 3.
**Flags:** "exploring maze-like patterns", "represents a possible solution" (represents-as-meaning-verb), "invites viewers to lose themselves", "contemplating the relationship between".
**Frontmatter note:** image folder name has a typo (`chucnkofmaze`). Not fixing here.

### Body — ORIGINAL
> A commissioned work exploring maze-like patterns and algorithmic structures. This exhibition presents intricate labyrinths generated through code, where each path represents a possible solution in a complex system.
> The piece invites viewers to lose themselves in the geometric complexity while contemplating the relationship between human perception and computational logic.

### Body — REWRITE
> Commissioned work. 59 × 84 cm. [FACT FROM FRONTMATTER: size]
>
> <!-- TODO: ADD who commissioned it, what the work actually is (technique, what the maze looks like, what's specific to "Chunk of Maze" vs. a generic maze), the Montana venue name, dates. -->

### Image alts — ORIGINAL (4x)
"Maze Detail 1", "Maze Pattern", "Algorithmic Structure", "Final View"

### Image alts — REWRITE
All 4 → `Chunk of Maze`

---

## 4. The Bitcoin Genesis Exhibition (2022-10-10)

**File:** `_posts/exhibitions/2022-10-10-the-bitcoin-genesis-exhibition.md`
**Detected as:** Exhibition statement.
**Scores:** AI-Likeness 10 / Voice 1 / Subject Specificity 2 / Buy-Readiness 3.
**Flags:** "exploring the intersection of", "creating a physical manifestation of", "bridges the gap between", "intangible nature of blockchain technology", "offering viewers a unique perspective".

### Body — ORIGINAL
> Exhibition featuring the Bitcoin Genesis artwork, exploring the intersection of cryptocurrency and generative art. This piece visualizes the genesis block of Bitcoin through algorithmic patterns, creating a physical manifestation of digital currency's foundational moment.
>
> The work bridges the gap between the intangible nature of blockchain technology and the tactile experience of pen-plotted art, offering viewers a unique perspective on the aesthetics of decentralized systems.

### Body — REWRITE
> Bitcoin Genesis. Shown at the Norman Rea Gallery, University of York. [FACT FROM FILENAME: `2023-01-15-norman-rea3.webp` confirms Norman Rea; Heslington is the University of York campus per frontmatter location.]
>
> <!-- TODO: ADD what the work actually is (medium, dimensions, year, how the genesis block is represented in the drawing), exhibition dates, anything specific to this Norman Rea show. -->

### Image alts — ORIGINAL (3x)
"Bitcoin Genesis Detail", "Exhibition Close-up" (x2)

### Image alts — REWRITE
All 3 → `Bitcoin Genesis at Norman Rea Gallery`

---

## 5. Plotter Fest (2024-08-28)

**File:** `_posts/exhibitions/2024-08-28-plotter-fest.md`
**Detected as:** Exhibition statement / first-person recap.
**Scores:** AI-Likeness 4 / Voice 7 / Subject Specificity 7 / Buy-Readiness 6. **Already mostly in voice.**
**Flags:** "buzzing with energy, ideas, and passionate people", "It wasn't just about X, it was about Y" pattern.

### Body — ORIGINAL
> A meetup organized by Bantam Tools where every pen plotter artist came with a piece turned out to be a great chance to share my work and connect with others. It wasn't just about showing art, it was about the community. The conversations pushed me to try new materials and formats, and thanks to Nima Nabavi's encouragement, I experimented with canvas for the first time. It felt less like a festival and more like a lab, buzzing with energy, ideas, and passionate people.

### Body — REWRITE
> Bantam Tools organized this. Every plotter artist showed up with a piece in hand. Less festival, more lab. Nima Nabavi pushed me to try canvas. I'd never plotted on canvas before.
>
> <!-- TODO (optional): if anything specific happened next (you kept working on canvas, made a piece from it, etc.), add it here. Earlier I wrote "I came home and started" but that was extrapolation. -->

### Image alts — ORIGINAL
(empty / not set)

### Image alts — REWRITE
All → `Plotter Fest, New York 2024` [FACT FROM FRONTMATTER: NY United States + date]

---

## 6. Comparaison 2025 / Grand Palais (2025-03-09)

**File:** `_posts/exhibitions/2025-03-09-grand-palais.md`
**Detected as:** Exhibition recap / blog post.
**Scores:** AI-Likeness 9 / Voice 2 / Subject Specificity 5 / Buy-Readiness 4.
**Flags:** "iconic Parisian venue", "magnificent glass roof", "stunning backdrop", "explores the intersection of", "showcasing how algorithmic processes can create works that resonate with", "couldn't help but feel the weight of its history", "welcomed me with open arms", "ideas flowed freely", "Her keen eye and constructive feedback challenged me", "breathtaking", "added another layer of meaning", "not just with memories, but with a renewed drive". Every section heading is a cliché.
**Structural recommendation:** collapse the 5-section essay into one tight piece in the style of file 10 (`art-capital`).

### Opening paragraph + "A Space Steeped in History" — ORIGINAL
> Bringing generative, pen-plotted art to the Grand Palais felt both surreal and deeply meaningful. This iconic Parisian venue, with its magnificent glass roof and Beaux-Arts architecture, provided a stunning backdrop for contemporary computational art. The exhibition explores the intersection of historical Constructivist principles with modern generative techniques, showcasing how algorithmic processes can create works that resonate with the geometric abstraction and systematic approaches of the early 20th century avant-garde.
>
> ## A Space Steeped in History
>
> Walking through the Grand Palais, I couldn't help but feel the weight of its history. Originally built for the 1900 Universal Exhibition, this architectural masterpiece has been home to a vast array of events from scientific fairs to major cultural exhibitions. Over the decades, it has also welcomed generations of artists, each leaving their mark and pushing the boundaries of what art can be. To be part of this legacy, even in my own small way, was humbling.

### Opening — REWRITE
> Comparaison 2025. Grand Palais. First time showing pen-plotted work under the glass dome. The hall was built for the 1900 Universal Exhibition. [VERIFY: 1900 is in the original, kept verbatim.]
>
> <!-- TODO: name the work(s) you showed in 2025 and add 1-2 specific lines if you want it longer. Pattern: like the 2026 art-capital post. -->

### "Finding My Place Among Masters" — ORIGINAL
> One of the highlights of this experience was the incredible artists I had the chance to meet. JARA, the leader of our Constructivism group, welcomed me with open arms and made me feel like I truly belonged. His generosity and leadership set the tone for a space where ideas flowed freely, and artistic boundaries were stretched.

### "Finding My Place Among Masters" — REWRITE
> Hernan Jara runs the Constructivism group at Comparaison. He brought me in. [VERIFY: original says "JARA" only. The 2026 art-capital post names "Hernan Jara" — I'm assuming same person. Confirm.]
>
> <!-- TODO (optional): one specific thing he did or said that mattered. -->

> ⚠️ **Do NOT auto-borrow the Constructivism group statement quote** ("The expressive force of formal relationships, the purity of rhythms, the balance of proportions") from the 2026 art-capital post into this 2025 post. That statement may belong to the 2026 show specifically, not 2025. [VERIFY: was the same group statement used in 2025? If yes, OK to add. If no, don't.]

### "Conversations That Left a Mark" — ORIGINAL
> Another defining moment came from my discussions with Rebecca Chou. Her keen eye and constructive feedback challenged me to think differently about my work. It's not often you find someone who understands your approach yet pushes you to refine it further. Those conversations, along with exchanges with other artists, were some of the most enriching moments of the entire exhibition.

### "Conversations That Left a Mark" — REWRITE
> Talked at length with Rebecca Chou.
>
> <!-- TODO: ADD 1 specific thing she said or that came out of those conversations that changed how you drew the next piece. Without that, this section is generic. If nothing specific, cut the whole section. -->

### "The Beauty of the Grand Palais" — ORIGINAL
> Beyond the people, the setting itself was breathtaking. Seeing my plotted lines displayed under the massive glass dome, within a space that has hosted some of the greatest exhibitions, added another layer of meaning to my work. It was a reminder that art, no matter how it's created, has a place in history when it challenges perceptions and sparks conversations.

### "The Beauty of the Grand Palais" — REWRITE
> *(Cut entirely. The dome image already does this work.)*

### "Looking Ahead" — ORIGINAL
> This exhibition was more than just a show it was a validation of the medium I've chosen to explore. Generative art, pen plotting, and algorithmic design have a voice in contemporary art, even in the most traditional settings. I left the Grand Palais not just with memories, but with a renewed drive to push my practice even further.

### "Looking Ahead" — REWRITE
> Pen plotting belongs here.
>
> *(Or cut the whole section and let the images close.)*

### Image alts — ORIGINAL
"Gallery View", "the constructivism group", "Rebecca Chou in front of her **peice**" (typo: peice → piece), "Final View"

### Image alts — REWRITE
- "Gallery View" → `Comparaison 2025, Grand Palais`
- "the constructivism group" → keep (factual)
- "Rebecca Chou in front of her peice" → `Rebecca Chou in front of her piece` (typo fix only)
- "Final View" → `Comparaison 2025, Grand Palais`

---

## 7. A Plot in the Wild (2025-05-25)

**File:** `_posts/exhibitions/2025-05-25-a-plot-in-the-wild.md`
**Detected as:** Exhibition statement.
**Scores:** AI-Likeness 8 / Voice 2 / Subject Specificity 5 / Buy-Readiness 4.
**Flags:** "takes art out of galleries and into public spaces" (used twice), "transforms urban landscapes into open-air galleries", "making art accessible to everyone regardless of their proximity to traditional art institutions". The unattributed quote in the middle is awkward.

### Body — ORIGINAL
> Part of Project / Forward: 2049, this global video art exhibition takes art out of galleries and into public spaces. The project features artists from Australia, Indonesia, India, Nigeria, Norway, Spain, and the United States.
> "What I love most about this project is that it takes art out of galleries and brings it directly to people in their everyday environments."
> The exhibition transforms urban landscapes into open-air galleries, making art accessible to everyone regardless of their proximity to traditional art institutions.

### Body — REWRITE
> Part of Project / Forward: 2049. A global video-art program that shows on outdoor screens, not in galleries. Artists from Australia, Indonesia, India, Nigeria, Norway, Spain, the US. And me.
>
> <!-- TODO: ADD which city/screen showed your piece, when, and what the piece was (which work, which medium, how long the video was). The quote in the middle of the original (unattributed) should be cut OR attributed properly if it's a quote from you or from the curators. -->

### Image alts — ORIGINAL (5x)
"A Plot in the Wild" (x2), "Street Display", "Public Space Art", "Night View"

### Image alts — REWRITE
All 5 → `A Plot in the Wild` (consistent, no invented descriptions)

---

## 8. Behind The Lines (2025-05-31)

**File:** `_posts/exhibitions/2025-05-31-behind-the-lines.md`
**Detected as:** Exhibition statement.
**Scores:** AI-Likeness 4 / Voice 6 / Subject Specificity 6 / Buy-Readiness 5. Close to voice already.
**Flags:** mild. "What emerges is both mechanical and deliberate" verges on abstract.

### Body — ORIGINAL
> A transparent glass installation lets visitors watch the pen plotter draw in real time. The process, usually hidden, is fully visible, from the algorithms guiding each move to the choices shaping the final image. What emerges is both mechanical and deliberate, a slow unfolding of lines on glass.

### Body — REWRITE
> Glass installation. The pen plotter runs in real time, behind the work, in full view. The code, the pen, the slow unfolding of lines on glass. The thing usually hidden in the studio.
>
> [VERIFY: I removed "set on a plinth" from an earlier draft — you don't say "plinth" in the original. If the plotter actually sat on a plinth at Lodève, add it back. If on a table or wall mount, say that instead.]

### Image alts — ORIGINAL
"Glass Installation View", "Pen Plotter in Action", "Process Detail", "Final Installation View"

### Image alts — REWRITE
- "Glass Installation View" → `Behind The Lines, Lodève`
- "Pen Plotter in Action" → keep (factual)
- "Process Detail" → keep (factual)
- "Final Installation View" → `Behind The Lines, Lodève`

---

## 9. Lines By Lines (2025-10-24)

**File:** `_posts/exhibitions/2025-10-24-lines-by-lines-cayo.md`
**Detected as:** Exhibition statement.
**Scores:** AI-Likeness 3 / Voice 8 / Subject Specificity 9 / Buy-Readiness 8. **Strong post otherwise.**
**Flags:** typo "accross" → "across"; em-dash in image alt; 12 em-dashes in the works list (skill v1.1 forbids em-dash everywhere).

### Frontmatter `location` — ORIGINAL
> `location: "CAYO Paris Treize,"` (trailing comma)

### Frontmatter `location` — REWRITE
> `location: "CAYO Paris Treize"`

### Body — ORIGINAL
> Opening: October 24, 2025.
>
> An exhibition of 12 pen-plotted works spanning accross all my last series with a focus on "Dye with Me".

### Body — REWRITE
> Opening: October 24, 2025.
>
> Twelve pen-plotted works across every recent series, with a focus on *Dye with Me*.

### Image alt — ORIGINAL
> "Vernissage — people in front of the works"

### Image alt — REWRITE
> "Vernissage. People in front of the works."

### Works list — ORIGINAL
Twelve entries using em-dashes:
- `*Plasma Convection* — 50 × 73 cm, acrylic on canvas`
- `*Synapses Canvas* — 60 × 80 cm, UV-sensitive ink on canvas`
- `*Chromatic Multiplication* — 59 × 84 cm, UV-sensitive ink on Bristol paper`
- `*Bubblesscape* — 59 × 84 cm, UV-sensitive ink on Bristol paper`
- `*First Division* — 59 × 84 cm, UV-sensitive ink on Bristol paper`
- `*Particle Asymmetry* — 59 × 84 cm, UV-sensitive ink on Bristol paper`
- `*Chromatic Moiré* — 59 × 84 cm, UV-sensitive ink on Bristol paper`
- `*Synapses* — 59 × 84 cm, UV-sensitive ink on Bristol paper`
- `*Dye With Me* — 70 × 100 cm, UV-sensitive ink on Bristol paper`
- `*Parcels* — 70 × 100 cm, UV-sensitive ink on Bristol paper`
- `*Fragmentation* — 70 × 100 cm, UV-sensitive ink on Bristol paper`
- `*Blended Squares GOLD* — 59 × 84 cm, acrylic on Bristol paper`

### Works list — REWRITE
Replace every em-dash with a comma:
- `*Plasma Convection*, 50 × 73 cm, acrylic on canvas`
- `*Synapses Canvas*, 60 × 80 cm, UV-sensitive ink on canvas`
- `*Chromatic Multiplication*, 59 × 84 cm, UV-sensitive ink on Bristol paper`
- `*Bubblesscape*, 59 × 84 cm, UV-sensitive ink on Bristol paper`
- `*First Division*, 59 × 84 cm, UV-sensitive ink on Bristol paper`
- `*Particle Asymmetry*, 59 × 84 cm, UV-sensitive ink on Bristol paper`
- `*Chromatic Moiré*, 59 × 84 cm, UV-sensitive ink on Bristol paper`
- `*Synapses*, 59 × 84 cm, UV-sensitive ink on Bristol paper`
- `*Dye With Me*, 70 × 100 cm, UV-sensitive ink on Bristol paper`
- `*Parcels*, 70 × 100 cm, UV-sensitive ink on Bristol paper`
- `*Fragmentation*, 70 × 100 cm, UV-sensitive ink on Bristol paper`
- `*Blended Squares GOLD*, 59 × 84 cm, acrylic on Bristol paper`

[VERIFY: confirm "Bubblesscape" spelling — looks like a typo for "Bubblescape" but it's in the original.]

---

## 10. Comparaison 2026 / Art Capital (2026-02-11)

**File:** `_posts/exhibitions/2026-02-11-art-capital.md`
**Scores:** AI-Likeness 1 / Voice 10 / Subject Specificity 9 / Buy-Readiness 8.

### Verdict
**No changes recommended.** This post is the voice target. Leave verbatim.

---

## 11. Rouen National Arts 2026 (2026-05-20)

**File:** `_posts/exhibitions/2026-05-20-rouen-national-arts.md`
**Detected as:** Exhibition statement + artwork descriptions.
**Scores:** AI-Likeness 7→4 / Voice 7→9 / Subject Specificity 9 / Buy-Readiness 7. **Bios are reference quality. Intro paragraph is the problem.**

**Typos:**
- Line 16: `Y¹ **et** Y²` (French "et") → `Y¹ and Y²` for EN audience.
- Line 16: `my new series called **Matilda's**` → `my new series Matildas` (no apostrophe; the series is plural, named after the Matilda Effect — confirm).

**Intro-paragraph flags (Julien-specific kill-list, all of them at once):**
- `from my new series called X` opener
- `brutal, architectural pattern` (stacked adjectives, skill kill-list)
- `represents society, power networks, paternalism, and the establishment` (represents-as-meaning-verb + abstract noun stacking)
- `women who deserved a Nobel Prize` (deserved editorializes)
- `Barely visible, like ghosts` (ghost metaphor, skill kill-list)
- `they remain a mystery` (abstract summary closer)

**Preserved (must NOT be rewritten):** the Y¹ Stevens and Y² Meitner biography blocks. They're the strongest writing on the site.

### Body line 1 — ORIGINAL (KEEP)
> Rouen National Arts 2026. Halle aux Toiles. May 20 - June 14.

### Body line 1 — REWRITE
**Keep as-is.**

### Intro paragraph — ORIGINAL
> For the first time, I'm presenting two pieces (Y¹ et Y²) from my new series called Matilda's.
> Up close, the brutal, architectural pattern represents society, power networks, paternalism, and the establishment that tried to erase these women. But step back, and variations within the pattern reveal a portrait of invisible women, women who deserved a Nobel Prize for their discoveries. Barely visible, like ghosts, they are there, but nobody knows their name or their detailed face, they remain a mystery.
>
> The visitor will have to make the effort to discover the story behind each of the two women presented.

### Intro paragraph — REWRITE
> Two pieces from the Matildas series. Y¹ and Y². 61 × 61 cm, acrylic and pen on canvas. [FACT FROM FILENAME: `Julien_Targz_Y1_61x61cm_Acrylic_pen_2026_1000EUR.webp` and Y2 equivalent.]
>
> Up close, a dense pattern. Step back, a portrait. Two women whose discoveries were credited to men.
>
> The biographies below tell the rest.

[VERIFY: "dense pattern" replaces "brutal, architectural pattern" — confirm the pattern is what you want to call it. If you want a single adjective, pick one: "architectural", "dense", "ordered", "grid-like" — your call.]

### Biography blocks (Y¹ Stevens, Y² Meitner) — ORIGINAL
*(see lines 25-44 of the source file)*

### Biography blocks — REWRITE
**Keep verbatim. Do not touch.** These are the voice target.

### Image alts — ORIGINAL
"Y¹ - Nettie Stevens", "Y² - Lise Meitner", and the preview hero alt.

### Image alts — REWRITE
Keep "Y¹ - Nettie Stevens" and "Y² - Lise Meitner". Or expand:
- `Y¹, Nettie Stevens, 61 × 61 cm, 2026`
- `Y², Lise Meitner, 61 × 61 cm, 2026`

---

## Summary table

| # | File | What needs your input |
|---|---|---|
| 1 | fill-the-blank | How visitors interacted, Paris venue, dates |
| 2 | blended-squares | Pieces shown, Paris venue, dates |
| 3 | chunk-of-maze | Commissioner, technique specifics, Montana venue |
| 4 | bitcoin-genesis | Medium, dimensions, year, what the drawing represents |
| 5 | plotter-fest | Optional: what happened next with canvas |
| 6 | grand-palais | One specific thing with Rebecca Chou, confirm Jara, confirm Constructivism quote applies to 2025 |
| 7 | a-plot-in-the-wild | Which city/screen showed your piece, the work itself, attribute the floating quote |
| 8 | behind-the-lines | Confirm plotter mounting (plinth/table/wall) |
| 9 | lines-by-lines-cayo | Just typo + em-dash sweep, no creative input needed |
| 10 | art-capital | **Nothing.** |
| 11 | rouen-national-arts | Confirm "Matildas" no apostrophe, confirm "dense" vs "architectural" choice for the pattern |

## Next step

Edit the **REWRITE** blocks in this file until they're factually correct. When a file is ready, tell me which numbers to apply (e.g. "apply 9, 10, 11 now") and I'll do the actual edits in `_posts/exhibitions/*.md`.

Once everything's applied, I'll bump `version.js` and you can commit.
