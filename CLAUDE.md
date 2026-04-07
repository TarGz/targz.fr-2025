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

Use `portfolio_drop/` workflow:

1. Drop a folder named `YYYY-MM-DD-slug/` into `portfolio_drop/` with images inside
2. Run `python3 new_artwork.py` (or `--dry-run` to preview)
3. The script converts images to webp (1200px), generates mobile (576px) and tablet (992px) responsive variants, and creates the markdown post

## Scripts

- `new_artwork.py` — Scan `portfolio_drop/` and create portfolio posts with responsive images
- `restructure_images.py` — One-time migration script (already run) to add dates to image folders
