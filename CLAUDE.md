## Development Guidelines

- Only commit when I ask
- Never mention Claude Code in commits
- Never add Co-Authored-By lines to commits

## Versioning

- Every commit must include a version bump in `version.js`
- Follow semver: Major (breaking changes), Minor (new features), Fix/Patch (bug fixes)
- Always update the CHANGELOG array in `version.js` with the current date and list of changes

## Project Rules

- Never change top: -100px; to top: -250px; for slide-nav-overlay.active

## Image Structure

All images use dated folder names matching the post filename:

```
assets/images/{category}/{YYYY-MM-DD}-{slug}/
assets/images/mobile/{category}/{YYYY-MM-DD}-{slug}/
assets/images/tablet/{category}/{YYYY-MM-DD}-{slug}/
```

Categories: portfolio, exhibitions, commissions, bits.

## Preview Image Geometry

Every `*-preview.webp` is the artwork floating on a white canvas. The home grid
gives each card the full column width, so the artwork must occupy the same slice
of the canvas on every piece or it reads as bigger or smaller than its
neighbours. **Every number below is mandatory, including the margins** — the
caption is positioned off the bottom margin, so getting it wrong pushes the title
onto the artwork.

| | value |
|---|---|
| canvas width | **1200 px**, always |
| canvas height | **323 + artwork height + 270** |
| background | pure `#fff` at the edges (it is composited onto white) |
| artwork width | **743 px**, centred on x = 600 |
| top margin | **323 px** above the artwork |
| bottom margin | **270 px** below the artwork |

A portrait mockup (artwork 743 × 1094) therefore lands on 1200 × 1687, and a
square piece on 1200 × 1326 — same width, shorter canvas. Never scale a square up
to fill a portrait canvas: `Y1`/`Y2` originally shipped 1062 px wide and read 40%
larger than everything else, and padding them out to portrait height instead left
a hole in the grid.

Any canvas that is **not** 1200 × 1687 needs `preview_height: <H>` in the post's
front matter — `_layouts/home.html` uses it for the card's `aspect-ratio`, and
without it the image gets cropped to portrait by `object-fit: cover`.

To re-fit an off-scale preview: measure the artwork's ink extent, scale by
`743 / current_artwork_width`, composite onto white so the artwork lands at
x = 228…971, then crop so exactly 323 px of white sits above it and 270 below.

```bash
magick -size 1200x<tall> xc:white \( SRC.webp -filter Lanczos -resize <pct>% \) -geometry +<dx>+<dy> -composite -quality 90 OUT.webp
magick OUT.webp -crop 1200x<323+h+270>+0+<dy> +repage OUT.webp
```

Then re-run `generate_responsive_images.py` and set `preview_height` if the
height changed.

## Adding New Portfolio Artworks

Requires `cwebp` (from the `webp` package) and macOS `sips` on the PATH.

Use `portfolio_drop/` workflow:

1. Drop a folder named `YYYY-MM-DD-slug/` into `portfolio_drop/` with images inside (png, jpg, tiff, heic, bmp, webp). The slug becomes the post title, title-cased ("The-Last-Brain-Cell" becomes "The Last Brain Cell").
2. Images are sorted by filename and the first one becomes the preview/thumbnail. Prefix them `1-`, `2-`, `3-` to control the order.
3. Run `python3 new_artwork.py` (or `--dry-run` to preview)
4. The script converts images to webp (1200px), generates mobile (576px) and tablet (992px) responsive variants, creates the markdown post in `_posts/portfolio/`, and removes the processed folder from portfolio_drop/
5. Fill in the generated post by hand: `description`, `ink`, `pen`, `frame`, body text above the image lines, and `shopify_id` if the piece goes to the shop. Never invent technique or material details; leave them empty for the artist to fill.

## Scripts

- `new_artwork.py` — Scan `portfolio_drop/` and create portfolio posts with responsive images
- `generate_responsive_images.py` — Rebuild mobile (576px) / tablet (992px) variants from every
  `portfolio/<slug>/<slug>-preview.webp`. Writes to `mobile|tablet/portfolio/<slug>/<name>.webp`,
  which is the nested path `_layouts/home.html` builds its `<source srcset>` from. Only touches
  outputs older than their source unless `--force`.
- `restructure_images.py` — One-time migration script (already run) to add dates to image folders
