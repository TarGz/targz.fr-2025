# Rewrite preview: Chromatic Interplay series (7 pieces)

N°3 is already shipped (calibration piece). This doc previews the other 7: **N°1, N°2, N°4, N°5, N°6, N°7, and Unfinished N°6.**

Nothing pushed. Review, then say go or fix.

---

## How to read this doc

For each piece you'll see:
- **Where it lives** (Shopify product ID and/or portfolio file path)
- **Before** (current state, abbreviated)
- **After** (proposed new copy)
- **Flags** if I had to leave something as TODO or noticed a discrepancy in the source

Common pattern across all 7: the hook follows the same structure as N°3 (Number of passes → series position + specific colors → "Home made generative truchet tilling algorythm").

---

## Cross-series flags (decide once, applies to all)

These 4 things show up across multiple pieces. Decide once and I'll apply consistently:

1. **Paper discrepancy.** Portfolio SEO descriptions for N°1, N°6, N°7, Unfinished N°6 all say "Bristol paper". Shop descriptions for the same pieces all say "cartridge Studio Gerstaecker by Clairefontaine". Which is correct? **My default: trust the shop.**

2. **N°7 has a YouTube iframe** embedded in the current shop description (plotter video). Keep it, drop it, or move to a "Process" section? **My default: keep as a "Watch the plot" link below the spec block.**

3. **N°7 has shipping notes** ("shipped rolled in cardboard tube, color may vary, shipped unframed"). These are operational, not voice. Drop from individual descriptions and centralize in shop policy page? **My default: drop them here, you add to shop policy separately.**

4. **N°6 ink-stain disclosure.** Current description has a note about a small ink stain on the lower part. This is a condition issue buyers must see. **My default: preserve in the new description as its own paragraph.**

---

## Piece 1 — Chromatic Interplay N°1

**Status:** Portfolio only (not on shop, per your earlier call).

**Surfaces touched:**
- Portfolio: `/Users/targz/Documents/GIT/targz.fr-2025/_posts/portfolio/2023-03-04-chromatic-interplay-n-1.md`

### Before (portfolio body)
Empty. Post has no body text, just an image.

### After (portfolio body)

```markdown
First in the Chromatic Interplay series. A1 paper. Non-archival ink.

Home made generative truchet tilling algorythm.

---

**Type**: <!-- TODO: confirm edition -->
**Medium**: Non-archival ink on Bristol paper
**Size**: 59 × 84 cm (A1)
**Frame**: <!-- TODO -->
**Plotter**: Custom-made pen plotter
**Year**: 2023

*Process details*
**Pen**: <!-- TODO -->
**Inks**: <!-- TODO: which specific Ecoline colors? -->
**Paper**: Bristol
```

### Frontmatter changes
None. Existing `ink: "Non Archival Ink"` stays; `pen` and `frame` stay empty (no source data).

### Flags
- N°1 is the only piece where I have no detailed ink/pen info (your shop never carried it). I marked them TODO instead of guessing. If you have a record of which inks you used, I'll fill them in.
- The hook is minimal because the source has zero existing copy. Per the never-invent rule, I won't write a story from nothing.

---

## Piece 2 — Chromatic Interplay N°2

**Surfaces touched:**
- Shopify: `gid://shopify/Product/8717344178515`
- Portfolio: `2024-02-02-chromatic-interplay-n2.md`

### Before (shop description, abbreviated)

```
An Exploration of Color Moiré. This piece is a generative art piece created
using my own P5.js code, this artwork is part of a series of patterns called
Chromatic Interplay. Each iteration of Chromatic Interplay is plotted multiple
times, employing different colors and pen angles.

Type: One of 4 Unique Originals (signed a numbered 1-4)
Size: A3 (297x420mm / 11.7 x 16.5 in)
Reference: 2023-06-17_BS-LJ03VEX6
... [old spec block continues]
```

### After (both shop and portfolio)

```
Three pen passes, three ink colors. The parallel pen turned to a different
angle each pass. The overlap makes a moiré.

Number 2 in the Chromatic Interplay series. Ultramarine Deep at 135°,
Magenta at 45°, Light Orange at 90°. One of 4 hand-signed prints from the
same plot.

Home made generative truchet tilling algorythm.

Type: One of 4 hand-signed and numbered prints
Medium: Ecoline watercolor on paper
Size: A3 (297 × 420 mm / 11.7 × 16.5 in)
Frame: Unframed
Plotter: Custom-made pen plotter
Year: 2023
Reference: TGZ-CHROMATIC-INTERPLAY-2-2023

Process details
Pen: Parallel pen 2.4mm
Inks (3 passes):
  1. Ecoline Ultramarine Deep 506 (135°)
  2. Ecoline Magenta 337 (45°)
  3. Ecoline Light Orange 236 (90°)
Paper: Studio Gerstaecker by Clairefontaine, 250g/m² (90lbs)
```

### Frontmatter changes
- `ink: ""` → `ink: "Ecoline watercolor"`

### Flags
- This piece is **edition of 4**, not unique. Unusual for the series. I called it out in the hook ("one of 4 hand-signed prints").

---

## Piece 3 — Chromatic Interplay N°4

**Surfaces touched:**
- Shopify: `gid://shopify/Product/8717292110163`
- Portfolio: `2024-02-02-chromatic-interplay-n4.md`

### After (both shop and portfolio)

```
Three pen passes, three ink colors. The parallel pen turned to a different
angle each pass. The overlap makes a moiré.

Number 4 in the Chromatic Interplay series. Pastel Green at 135°,
Pastel Roser at 90°, Magenta at 45°.

Home made generative truchet tilling algorythm.

Type: Hand-signed, unique original (1 of 1)
Medium: Ecoline watercolor on paper
Size: A2 (420 × 594 mm / 16.5 × 23.4 in)
Frame: Unframed
Plotter: Custom-made pen plotter
Year: 2023
Reference: TGZ-CHROMATIC-INTERPLAY-4-2023

Process details
Pen: Parallel pen 2.4mm
Inks (3 passes):
  1. Ecoline Pastel Green 666 (135°)
  2. Ecoline Pastel Roser 390 (90°)
  3. Ecoline Magenta 337 (45°)
Paper: Studio Gerstaecker by Clairefontaine, 250g/m² (90lbs)
```

### Frontmatter changes
- `pen: "Parallel pen 2,4mm"` → `pen: "Parallel pen 2.4mm"` (fix decimal)
- `ink: ""` → `ink: "Ecoline watercolor"`

---

## Piece 4 — Chromatic Interplay N°5

**Surfaces touched:**
- Shopify: `gid://shopify/Product/8717213172051`
- Portfolio: `2024-02-02-chromatic-interplay-n5.md`

### After (both shop and portfolio)

```
Three pen passes, three ink colors. The parallel pen turned to a different
angle each pass. The overlap makes a moiré.

Number 5 in the Chromatic Interplay series. Light Orange at 90°,
Pastel Roser at 135°, Magenta at 45°.

Home made generative truchet tilling algorythm.

Type: Hand-signed, unique original (1 of 1)
Medium: Ecoline watercolor on paper
Size: <!-- TODO: confirm size (not in source) -->
Frame: Unframed
Plotter: Custom-made pen plotter
Year: 2023
Reference: TGZ-CHROMATIC-INTERPLAY-5-2023

Process details
Pen: Parallel pen 2.4mm
Inks (3 passes):
  1. Ecoline Light Orange 236 (90°)
  2. Ecoline Pastel Roser 390 (135°)
  3. Ecoline Magenta 337 (45°)
Paper: Studio Gerstaecker by Clairefontaine, 250g/m² (90lbs)
```

### Frontmatter changes
- `pen: "Parallel pen 2,4mm"` → `pen: "Parallel pen 2.4mm"`
- `ink: ""` → `ink: "Ecoline watercolor"`

### Flags
- **Size missing from source.** Current shop description has no Size line. I marked TODO. Guess based on series: probably A2 like N°3/N°4 or A3 like N°2 — but I won't pick one. Tell me which.

---

## Piece 5 — Chromatic Interplay N°6

**Surfaces touched:**
- Shopify: `gid://shopify/Product/8717319012691`
- Portfolio: `2023-04-29-chromatic-interplay-n-6.md`

### After (both shop and portfolio)

```
Two pen passes, two ink colors. The parallel pen turned to different angles
between passes. The overlap makes a moiré.

Number 6 in the Chromatic Interplay series. Chartreuse at 45°, Magenta at 90°.
A1 paper, larger than N°2 through N°5.

A small ink droplet stained the lower part during printing, near the artwork's
number. It does not affect the image. I can cover it with white on request.

Home made generative truchet tilling algorythm.

Type: Hand-signed, unique original (1 of 1)
Medium: Ecoline watercolor on paper
Size: A1 (594 × 841 mm / 23 × 33 in)
Frame: Unframed
Plotter: Custom-made pen plotter
Year: 2023
Reference: TGZ-CHROMATIC-INTERPLAY-6-2023

Process details
Pen: Parallel pen 2.4mm
Inks (2 passes):
  1. Ecoline Chartreuse 233 (45°)
  2. Ecoline Magenta 337 (90°)
Paper: Studio Gerstaecker by Clairefontaine, 250g/m² (90lbs)
```

### Frontmatter changes
- `frame: ""` → `frame: "Unframed"`
- `ink: "Non Archival Ink"` → `ink: "Ecoline watercolor"` (more specific; matches shop spec block)

### Flags
- Portfolio body currently says "Tears of Contrast." Cute, but no longer fits the new structure. Drop or keep as alt title?
- The portfolio frontmatter says `ink: "Non Archival Ink"`. The shop says Ecoline watercolor. They're not contradictory (Ecoline is non-archival ink), but the shop version is more specific. Going with the more specific.

---

## Piece 6 — Chromatic Interplay N°7

**Surfaces touched:**
- Shopify: `gid://shopify/Product/8714574463315`
- Portfolio: `2023-10-15-chromatic-nbsp-interplay-n-7.md`

### After (both shop and portfolio)

```
Four pen passes, four ink colors. The parallel pen turned to different angles
between passes. The overlap makes a moiré.

Number 7 in the Chromatic Interplay series. Cyan, Magenta, Magenta 3345,
and Light Orange. A1 paper, largest in the series.

Home made generative truchet tilling algorythm.

Type: Hand-signed, unique original (1 of 1)
Medium: Ecoline watercolor on paper
Size: A1 (594 × 841 mm / 23 × 33 in)
Frame: Unframed
Plotter: Custom-made pen plotter
Year: 2023
Reference: TGZ-CHROMATIC-INTERPLAY-7-2023

Process details
Pen: Parallel pen 2.4mm
Inks (4 passes):
  1. Ecoline Cyan 578 (0°)
  2. Ecoline Magenta 337 (0°)
  3. Ecoline Magenta 3345 (0°)
  4. Ecoline Light Orange 236 (90°)
Paper: Studio Gerstaecker by Clairefontaine, 250g/m² (90lbs)

Watch the plot: https://www.youtube.com/watch?v=ST9J0CgTWas
```

### Frontmatter changes
- Portfolio body is currently empty. Will be filled with the new text above.

### Flags
- **YouTube iframe → plain link.** Current shop has an embedded iframe. New version uses a plain link to keep the description clean. If you want the iframe back, say so.
- **Shipping notes dropped.** Current shop has "shipped rolled in cardboard tube, color may vary, shipped unframed". These are policy info, not voice. Recommend you add a single "Shipping & condition" section to shop policy and link to it from every product.
- Three inks have angle 0° (Cyan, Magenta, Magenta 3345). That's unusual — all three plot at the same angle. Confirms?

---

## Piece 7 — Unfinished Chromatic Interplay N°6

**Surfaces touched:**
- Shopify: `gid://shopify/Product/8717312590163`
- Portfolio: `2023-05-01-chromatic-interplay-n-6-half.md`

### After (both shop and portfolio)

```
Two pen passes, two ink colors. I stopped the plot before it finished.
The result was already what I wanted.

A variation on N°6 in the Chromatic Interplay series. Chartreuse at 45°,
Magenta at 90°. Same plot file as N°6, but stopped halfway through.

Home made generative truchet tilling algorythm.

Type: Hand-signed, unique original (1 of 1)
Medium: Ecoline watercolor on paper
Size: A1 (594 × 841 mm / 23 × 33 in)
Frame: Unframed
Plotter: Custom-made pen plotter
Year: 2023
Reference: TGZ-UNFINISHED-CHROMATIC-INTERPLAY-6-2023

Process details
Pen: Parallel pen 2.4mm
Inks (2 passes):
  1. Ecoline Chartreuse 233 (45°)
  2. Ecoline Magenta 337 (90°)
Paper: Studio Gerstaecker by Clairefontaine, 250g/m² (90lbs)
```

### Frontmatter changes
- None (frontmatter already has `pen`, `frame`, `ink`. Just `ink` value updates from generic to Ecoline watercolor).

### Flags
- Portfolio currently has "The blur of certainty" as a closer. Drop or keep?

---

## Summary of changes

| Piece | Shop description | Portfolio body | Frontmatter |
|---|---|---|---|
| N°1 | n/a (portfolio only) | Add minimal hook + spec block (mostly TODO) | No change |
| N°2 | Full rewrite | Full rewrite | `ink` filled |
| N°4 | Full rewrite | Full rewrite | `pen` decimal fix + `ink` filled |
| N°5 | Full rewrite (Size = TODO) | Full rewrite | `pen` decimal fix + `ink` filled |
| N°6 | Full rewrite + preserve stain note | Full rewrite | `frame` + `ink` updated |
| N°7 | Full rewrite + YouTube as link + drop shipping notes | Full rewrite (was empty) | No change |
| Unfinished N°6 | Full rewrite | Full rewrite | `ink` updated |

## What "go" will execute

- **6 Shopify `update-product` calls** (all 7 except N°1, which has no shop product)
- **7 portfolio file edits** (one per piece, hitting body + frontmatter as needed)

Total: 13 actions across 6 Shopify products and 7 markdown files.

---

## Outstanding decisions before push

Quick answers and I push. Defaults in parens.

1. **Paper: Bristol or Studio Gerstaecker?** (default: Studio Gerstaecker)
2. **N°7 YouTube: link or iframe?** (default: link)
3. **N°7 shipping notes: drop or keep?** (default: drop)
4. **N°5 size: A2, A3, or other?** (default: leave as TODO and skip pushing N°5 until you say)
5. **N°6 "Tears of Contrast" closer: keep, drop, or move?** (default: drop)
6. **Unfinished N°6 "The blur of certainty" closer: keep, drop, or move?** (default: drop)
7. **N°1 minimal hook OK as-is, or do you have ink/pen specifics to fill in?** (default: ship as-is with TODOs)
