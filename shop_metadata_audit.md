# Shop metadata audit — Batch 1 of unification

**Source plan:** `~/.claude/plans/so-i-want-to-snoopy-platypus.md`

**Auto-mode decisions baked into this audit** (override any of these and I'll regenerate):
- Canonical SKU format: `TGZ-{SLUG-UPPER}-{YYYY}` — uppercase, hyphens, year = portfolio post year, no embedded plot date
- All emoji prefixes dropped from **titles** and **handles**
- For "Unfinished Chromatic Interplay N°6": keep "Unfinished" (more meaningful than "half")
- Handles: lowercase, hyphenated, no emoji, no "copy-of-" / no "test"
- Variants get a suffix: `TGZ-{SLUG}-{VARIANT}-{YYYY}`

**What this changes in Shopify per product:** title, handle, SKU(s). Descriptions/specs are out of scope for this batch — those come in batch 3 via `/the-humanizer-targz`.

**What you need to do:** scan the table, flag any rows where the proposed title/slug/year is wrong, then I push the batch to Shopify.

---

## Audit table (32 products)

| # | Current title | Current handle | Current SKU | → New title | → New handle | → New SKU | Year src | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | BLENDED SQUARES N°25 | `blended-squares-n-25` | *(empty)* | Blended Squares N°25 | `blended-squares-25` | `TGZ-BLENDED-SQUARES-25-2021` | 2021-08-17 | Fixes empty SKU |
| 2 | Plasma Convection Canvas | `plasma-convection` | `2024-06-15_BS-LXG48GI0` | Plasma Convection Canvas | `plasma-convection-canvas` | `TGZ-PLASMA-CONVECTION-CANVAS-2024` | 2024-11-24 | Handle was too generic |
| 3 | Synapse - Blue | `synapse-blue` | `2024-05-24_BS-LWKW2QWV-BLUE` | Synapse Blue | `synapse-blue` | `TGZ-SYNAPSE-BLUE-2024` | 2024-07-11 | No separator |
| 4 | Synapse - Orange | `synapse-orange` | `2024-05-24_BS-LWKW2QWV-ORANGE` | Synapse Orange | `synapse-orange` | `TGZ-SYNAPSE-ORANGE-2024` | 2024-07-11 | No separator |
| 5 | Synapses - Grand Palais | `synapses-grand-palais` | *(empty)* | Synapses Canvas | `synapses-canvas` | `TGZ-SYNAPSES-CANVAS-2025` | 2025-02-02 | Exhibition context moves to description, not title |
| 6 | Y² | `y` | `TGZ-Y2-2026` | Y² | `y-2` | `TGZ-Y2-2026` | 2026-03-30 | SKU already canonical; handle fix only |
| 7 | Y¹ | `test` | `TGZ-Y1-2026` | Y¹ | `y-1` | `TGZ-Y1-2026` | 2026-03-25 | SKU already canonical; handle was `test` |
| 8 | ♣️ Vinyl Impression N°1 | `vinyl-impression-n-1` | `2023-09-30_BS-LN6FZHBY` | Vinyl Impression N°1 | `vinyl-impression-1` | `TGZ-VINYL-IMPRESSION-1-2023` | 2023-09-30 | Drop ♣️ |
| 9 | ♣️ Vinyl Impression N°2 | `vinyl-impression-n-2` | `2023-11-26_BS-LPFGW51Y` | Vinyl Impression N°2 | `vinyl-impression-2` | `TGZ-VINYL-IMPRESSION-2-2023` | 2023-11-26 | Drop ♣️ |
| 10 | ⚛️ Particle Asymmetry | `⚛️-particle-asymmetry` | *(empty)* | Particle Asymmetry | `particle-asymmetry` | `TGZ-PARTICLE-ASYMMETRY-2024` | 2024-03-13 | Emoji in handle was broken |
| 11 | ✒️ Monochrome Moiré N°1 | `monochrome-moire-n-1` | `2023-05-13_BS-LHLX0FN1` | Monochrome Moiré N°1 | `monochrome-moire-1` | `TGZ-MONOCHROME-MOIRE-1-2023` | 2023-05-13 | |
| 12 | ✒️ Monochrome Moiré N°2 | `monochrome-moire-n-2` | `2023-11-12_BS-LOVJ45WK` | Monochrome Moiré N°2 | `monochrome-moire-2` | `TGZ-MONOCHROME-MOIRE-2-2023` | 2023-11-12 | |
| 13 | ✳️ Green Lagoon | `green-lagoon` | `2024-03-24_BS-LU5KDDJP` | Green Lagoon | `green-lagoon` | `TGZ-GREEN-LAGOON-2024` | 2024-03-24 | |
| 14 | 〽️ Unfinished Chromatic Interplay N°6 | `unfinished-chromatic-interplay-n-6` | `2023-08-29_BS-LLWOSKAG-U` | Unfinished Chromatic Interplay N°6 | `unfinished-chromatic-interplay-6` | `TGZ-UNFINISHED-CHROMATIC-INTERPLAY-6-2023` | 2023-05-01 | Portfolio slug says "half"; shop wins here |
| 15 | 🌕 A Duet of Gold and Red | `a-duet-of-gold-and-red-🌕` | `2023-07-15_BS-LK42GGKW` | A Duet of Gold and Red | `duet-gold-red` | `TGZ-DUET-GOLD-RED-2023` | 2023-07-15 | Emoji was in handle |
| 16 | 🧬 Chromatic Interplay N°2 | `chromatic-interplay-n-2` | `2023-06-17_BS-LJ03VEX6` | Chromatic Interplay N°2 | `chromatic-interplay-2` | `TGZ-CHROMATIC-INTERPLAY-2-2023` | 2023-06-17 (SKU) — portfolio post dated 2024-02-02 | Year drift: SKU plot date is 2023, portfolio post is 2024. Going with 2023 as plot year |
| 17 | 🧬 Chromatic Interplay N°3 | `chromatic-interplay-n-3` | `2023-07-09_BS-LJV6Z6DS` | Chromatic Interplay N°3 | `chromatic-interplay-3` | `TGZ-CHROMATIC-INTERPLAY-3-2023` | 2023-07-09 | |
| 18 | 🧬 Chromatic Interplay N°4 | `chromatic-interplay-n-4` | `2023-06-28_BS-LJG59XM9` | Chromatic Interplay N°4 | `chromatic-interplay-4` | `TGZ-CHROMATIC-INTERPLAY-4-2023` | 2023-06-28 | |
| 19 | 🧬 Chromatic Interplay N°5 | `chromatic-interplay-n-5` | `2023-06-26_BS-LJCZ58F8` | Chromatic Interplay N°5 | `chromatic-interplay-5` | `TGZ-CHROMATIC-INTERPLAY-5-2023` | 2023-06-26 | |
| 20 | 🧬 Chromatic Interplay N°6 | `chromatic-interplay-n-6` | `2023-08-29_BS-LLWOSKAG` | Chromatic Interplay N°6 | `chromatic-interplay-6` | `TGZ-CHROMATIC-INTERPLAY-6-2023` | 2023-04-29 | |
| 21 | 🧬 Chromatic Interplay N°7 | `chromatic-interplay-n-7-large` | `2023-03-04-BS-LEU59HX6` | Chromatic Interplay N°7 | `chromatic-interplay-7` | `TGZ-CHROMATIC-INTERPLAY-7-2023` | 2023-10-15 | **The original bug.** SKU date was N°1's, not N°7's |
| 22 | 🌈 Color Wheel Chaos | `color-wheel-chaos` | `2023-11-27_BS-LPH6MMNT` | Color Wheel Chaos | `color-wheel-chaos` | `TGZ-COLOR-WHEEL-CHAOS-2023` | 2023-11-04 | |
| 23 | 💘 Fused Duality N°1 | `fused-duality-n-1` | `2023-08-25_BS-LLQZ1IY2` | Fused Duality N°1 | `fused-duality-1` | `TGZ-FUSED-DUALITY-1-2023` | 2023-08-21 | |
| 24 | 🌟 Gold Blended Squares N°20 | `gold-blended-squares-n-20` | `021-C_LxL_CxC2xL_CxC-1` | Gold Blended Squares N°20 | `gold-blended-squares-20` | `TGZ-BLENDED-SQUARES-20-GOLD-2022` | 2022-07-03 | **Was duplicate SKU with row 29** |
| 25 | 👾 Left And Right Space Noodle | `left-and-right-space-noodle` | 3 variants (see below) | Left And Right Space Noodle | `left-right-space-noodle` | (per variant) | 2024-02-06 | 3 variants |
| 25a | ↳ variant LEFT | | `2024-01-21_BS-LRNDGAOD-L` | | | `TGZ-SPACE-NOODLE-LEFT-2024` | | |
| 25b | ↳ variant RIGHT | | `2024-01-21_BS-LRNDGAOD-R` | | | `TGZ-SPACE-NOODLE-RIGHT-2024` | | |
| 25c | ↳ variant LEFT & RIGHT | | `2024-01-21_BS-LRNDGAOD-LR` | | | `TGZ-SPACE-NOODLE-PAIR-2024` | | |
| 26 | 🪢 Luminous Gradient N°1 | `luminous-gradient-n-1` | `2023-04-22_BS-LGS4Q045` | Luminous Gradient N°1 | `luminous-gradient-1` | `TGZ-LUMINOUS-GRADIENT-1-2023` | 2023-04-22 | |
| 27 | 🪢 Luminous Gradient N°2 | `luminous-gradient-n-2` | `2023-04-27_BS-LGZH2CRF` | Luminous Gradient N°2 | `luminous-gradient-2` | `TGZ-LUMINOUS-GRADIENT-2-2023` | 2023-04-25 | |
| 28 | 🪢 Luminous Gradient N°3 | `copy-of-luminous-gradient-n-1` | `2023-04-27_BS-LGZH3CLY` | Luminous Gradient N°3 | `luminous-gradient-3` | `TGZ-LUMINOUS-GRADIENT-3-2023` | 2023-04-27 | Was `copy-of-...` handle |
| 29 | 🍥 pink&gold Blended Squares N°20B | `🍥-pink-gold-blended-squares-n-20b` | `021-C_LxL_CxC2xL_CxC-1` | Pink & Gold Blended Squares N°20B | `pink-gold-blended-squares-20b` | `TGZ-BLENDED-SQUARES-20B-PINK-GOLD-2023` | 2023-01-15 | **Was duplicate SKU with row 24**; emoji in handle |
| 30 | 🦓 Unexpected Patterns | `unexpected-patterns` | `2023-09-30_BS-LN6FZHBY-DASHED` | Unexpected Patterns | `unexpected-patterns` | `TGZ-UNEXPECTED-PATTERNS-2023` | 2023-09-30 | |
| 31 | 🪢 Figure-eight Knot | `figure-eight-knot` | `2024-03-09_BS-LTK49D8C` | Figure-eight Knot | `figure-eight-knot` | `TGZ-FIGURE-EIGHT-KNOT-2024` | 2024-04-27 | |
| 32 | 🇫🇷 Vive La France 🇫🇷 | `vive-la-france` | `2023-07-14-LK2KHH2Q` | Vive La France | `vive-la-france` | `TGZ-VIVE-LA-FRANCE-2023` | 2023-07-14 | |

---

## What this fixes

- **0 empty SKUs** (was 3+ confirmed: rows 1, 5, 10)
- **0 duplicate SKUs** (was rows 24 & 29 both `021-C_LxL_CxC2xL_CxC-1`)
- **0 misleading dates in SKU** (was row 21, the N°7/N°1 confusion you flagged)
- **0 emoji in handles** (was rows 10, 15, 29)
- **0 dev-leftover handles** (was rows 6, 7, 28)
- **1 SKU schema** instead of 3
- All 32 products now have a SKU you can trace back to a portfolio post via the slug

## URL redirect risk

Changing handles means Shopify URLs change. Shopify auto-creates 301 redirects when you edit a handle in admin (default behavior), but **double-check Settings → Navigation → URL redirects** after the batch lands. Any link in an old Instagram caption, email blast, or external article to the old URL will follow the redirect — should be fine, but worth verifying for the 5-6 most-trafficked products.

## Next step

If this all looks right, say "go" and I push the 32-product batch through `update-product` mutations. I'll do them serially with output so you see each one land. If you want me to change any title/slug/year before pushing, point at the row number and tell me what to change.

A few I'd flag specifically as worth a second look:
- **Row 5** — should the title really lose "Grand Palais"? It's the exhibition, not the piece name. I argued title=piece, description=context. Pushback welcome
- **Row 14** — "Unfinished" vs "half" — both work, I picked "Unfinished" because the shop already used it
- **Row 21** — the original bug. The fix here actually changes a SKU that may have been referenced in past orders/inventory exports; if you've ever exported sales data with the old SKU, the new one won't match
