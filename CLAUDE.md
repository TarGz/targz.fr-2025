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
- `restructure_images.py` — One-time migration script (already run) to add dates to image folders
