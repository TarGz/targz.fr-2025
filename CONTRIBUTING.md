# Development Guide

## Technical Stack

- **Jekyll** — Static site generator
- **Pico CSS** — Minimal CSS framework
- **GitHub Pages** — Hosting and deployment

## Local Development

### Prerequisites

- Ruby 3.2.2+, Bundler
- `cwebp` for image conversion: `brew install webp`

### Setup

```bash
git clone https://github.com/targz/targz.fr-2025.git
cd targz.fr-2025
gem install bundler
bundle install
```

### Run

```bash
./startlocaldev.sh
# or: bundle exec jekyll serve --port 4001 --livereload
```

Open `http://localhost:4001`

## Project Structure

```
├── _posts/                # Posts by category
│   ├── portfolio/         # Artwork posts
│   ├── bits/              # Experiments
│   ├── exhibitions/       # Show documentation
│   └── commissions/       # Custom projects
├── _layouts/              # Jekyll layout templates
├── _includes/             # Reusable HTML components
├── assets/
│   ├── images/
│   │   ├── portfolio/     # Portfolio images (dated subfolders)
│   │   ├── exhibitions/   # Exhibition images (dated subfolders)
│   │   ├── commissions/   # Commission images (dated subfolders)
│   │   ├── bits/          # Bits images (dated subfolders)
│   │   ├── mobile/        # Mobile responsive variants (576px)
│   │   └── tablet/        # Tablet responsive variants (992px)
│   └── css/               # Custom stylesheets
├── portfolio_drop/        # Drop folder for new artworks (gitignored)
├── new_artwork.py         # Script to process portfolio_drop/ images
├── version.js             # Version and changelog
└── _config.yml            # Jekyll configuration
```

## Adding New Portfolio Artworks

1. Create a folder `YYYY-MM-DD-slug/` in `portfolio_drop/` with images
2. Run `python3 new_artwork.py` (or `--dry-run` to preview)
3. The script converts to webp, generates responsive variants, creates the post, and cleans up the drop folder

## Post Templates

### Portfolio
```markdown
---
layout: post
title: "Artwork Title"
date: YYYY-MM-DD
category: portfolio
image: /assets/images/portfolio/YYYY-MM-DD-slug/slug-preview.webp
ink: ""
pen: ""
frame: ""
---
```

### Exhibition
```markdown
---
layout: post
title: "Exhibition Name"
date: YYYY-MM-DD
category: exhibitions
image: /assets/images/exhibitions/YYYY-MM-DD-slug/slug-preview.webp
location: "Gallery, City"
---
```

## Deployment

Automatic via GitHub Pages on push to `main`.
