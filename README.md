# Targz — Algorithmic Pen Plotter Art

**Original pen plotted artworks by Targz** — generative art drawn by machine, inspired by Op Art, geometric abstraction, and mathematical patterns.

Each piece is a unique, one-of-a-kind artwork created using custom algorithms and precision pen plotters. The result is a fusion of computational design and physical craftsmanship — where code meets ink on paper.

## The Work

- **Pen plotting** — Algorithmic drawings executed by precision plotters with archival ink
- **Op Art & geometry** — Optical illusions, moiré patterns, blended gradients, and chromatic interplay
- **Canvas & paper** — Works on fine art paper and stretched canvas, often framed
- **Editions & originals** — Each plot is unique due to the generative nature of the algorithms

## Links

- **Portfolio**: [targz.fr](https://targz.fr)
- **Shop**: [shop.targz.fr](https://shop.targz.fr)
- **Instagram**: [@targz](https://instagram.com/targz)
- **TikTok**: [@targz](https://tiktok.com/@targz)
- **Reddit**: [u/_targz_](https://www.reddit.com/user/_targz_/submitted/)

## Exhibitions

Targz's work has been exhibited internationally, including at the **Grand Palais** (Paris), and featured in group and solo shows focused on generative and plotter art.

## Copyright & Usage

**All artworks, images, and content in this repository are copyrighted.**

© Targz. All rights reserved.

No artwork, image, photograph, or text from this repository may be reproduced, distributed, displayed, or used in any form — including AI/ML training datasets — without explicit written permission from the artist.

For licensing, commissions, or purchase inquiries: visit [targz.fr](https://targz.fr) or contact via Instagram [@targz](https://instagram.com/targz).

## Technical

This site is built with Jekyll and deployed on GitHub Pages.

## Run locally

**First time on a new Mac:**

```bash
./install.sh
```

Installs Homebrew Ruby, bundler, and all gems into `vendor/bundle/`. Takes 1–2 minutes. Requires [Homebrew](https://brew.sh).

**Then start the site** — open a **new** terminal (so the new PATH is picked up), then:

```bash
bundle exec jekyll serve --port 4001 --livereload
```

Visit [http://localhost:4001](http://localhost:4001).

**Stuck on the same terminal where you ran `install.sh`?** Either open a new one, or run:

```bash
source ~/.zshrc
```

## Contributing: adding a new artwork

The whole pipeline (webp conversion, responsive variants, post creation) is automated by `new_artwork.py`.

**Dependencies:** `cwebp` (install with `brew install webp`) and `sips` (built into macOS).

1. **Drop the images.** Create a folder named `YYYY-MM-DD-slug/` inside `portfolio_drop/` and put the source images in it (png, jpg, tiff, heic, bmp, webp all work). Images are sorted by filename and the first one becomes the preview/thumbnail, so prefix them `1-`, `2-`, `3-` to control the order. The slug becomes the post title ("2026-07-05-The-Last-Brain-Cell" gives "The Last Brain Cell").

2. **Run the script.**

   ```bash
   python3 new_artwork.py --dry-run   # preview what will happen
   python3 new_artwork.py             # do it
   ```

   The script:
   - converts each image to webp at 1200px max width into `assets/images/portfolio/{date}-{slug}/`
   - names them `{slug}-preview.webp`, `{slug}-02.webp`, `{slug}-03.webp`, ...
   - generates responsive previews in `assets/images/mobile/portfolio/` (576px) and `assets/images/tablet/portfolio/` (992px)
   - creates the post at `_posts/portfolio/{date}-{slug}.md` with frontmatter and image references
   - deletes the processed folder from `portfolio_drop/`

3. **Write the article.** Open the generated `.md` and fill in the frontmatter (`description`, `ink`, `pen`, `frame`, and `shopify_id` if the piece is in the shop), then add the body text above the image lines.

4. **Check it locally** with `bundle exec jekyll serve --port 4001 --livereload` before committing.

