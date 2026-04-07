# Targz - Pen Plotting Art Portfolio

A minimalist portfolio website showcasing pen plotting art inspired by Op Art, built with Jekyll and Pico CSS.

## About

This is the source code for Targz's artistic portfolio website, featuring:
- **Pen plotting artwork** - Generative art created with pen plotters
- **Op Art inspiration** - Geometric patterns and optical illusions
- **Minimalist design** - Clean, distraction-free presentation
- **Responsive layout** - Works beautifully on all devices

## Technical Stack

- **Jekyll** - Static site generator
- **Pico CSS** - Minimal CSS framework for semantic HTML
- **GitHub Pages** - Hosting and deployment
- **Custom CSS** - Additional styling for portfolio presentation

## Local Development

### Prerequisites

- Ruby 3.2.2 or higher
- Bundler gem

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/targz/targz.fr-2025.git
   cd targz.fr-2025
   ```

2. Install Ruby (if needed):
   ```bash
   # Install Homebrew if you don't have it
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

   # Install rbenv and ruby-build
   brew install rbenv ruby-build

   # Install Ruby 3.2.2
   rbenv install 3.2.2
   rbenv global 3.2.2

   # Add rbenv to your shell
   echo 'eval "$(rbenv init -)"' >> ~/.zshrc
   source ~/.zshrc
   ```

3. Install dependencies:
   ```bash
   gem install bundler
   bundle install
   ```

4. Run the development server:
   ```bash
   # Use the provided script:
   ./startlocaldev.sh
   
   # Or manually:
   bundle exec jekyll serve --port 4001 --livereload
   
   # Clean cache if needed:
   bundle exec jekyll clean
   ```

5. Open your browser to `http://localhost:4001`

## Project Structure

```
├── _posts/                # Published blog posts
│   ├── portfolio/         # Artwork posts
│   ├── bits/              # Experiments
│   ├── exhibitions/       # Show documentation
│   └── commissions/       # Custom projects
├── _drafts/               # Unpublished draft posts & templates
├── _layouts/              # Jekyll layout templates
├── _includes/             # Reusable HTML components
├── _plugins/              # Jekyll plugins (responsive images)
├── assets/
│   ├── images/
│   │   ├── portfolio/     # Portfolio images (dated subfolders)
│   │   ├── exhibitions/   # Exhibition images (dated subfolders)
│   │   ├── commissions/   # Commission images (dated subfolders)
│   │   ├── bits/          # Bits images (dated subfolders)
│   │   ├── mobile/        # Mobile responsive variants (mirrors above structure)
│   │   └── tablet/        # Tablet responsive variants (mirrors above structure)
│   └── css/               # Custom stylesheets
├── portfolio_drop/        # Drop folder for new portfolio artworks (gitignored)
├── new_artwork.py         # Script to process portfolio_drop/ images
├── _config.yml            # Jekyll configuration
├── startlocaldev.sh       # Local development script
└── startlocaldev-draft.sh # Local development with drafts
```

### Image Directory Convention

All images live in dated subfolders matching the post filename:

```
assets/images/portfolio/2025-02-08-dye-with-me/
    dye-with-me-preview.webp    # Preview (homepage grid)
    dye-with-me-02.webp         # Additional images
    dye-with-me-03.webp
assets/images/mobile/portfolio/2025-02-08-dye-with-me/
    dye-with-me.webp            # 576px mobile variant
assets/images/tablet/portfolio/2025-02-08-dye-with-me/
    dye-with-me.webp            # 992px tablet variant
```

## Content Categories

- **Portfolio** (`category: portfolio`) - Featured pen plotting artworks
- **Bits** (`category: bits`) - Experiments and works in progress
- **Exhibitions** (`category: exhibitions`) - Show documentation and gallery features
- **Commissions** (`category: commissions`) - Custom projects and collaborations
- **Updates** (`category: updates`) - News and project updates

## Adding New Portfolio Artworks

The fastest way to add new portfolio artworks:

### 1. Drop images into `portfolio_drop/`

Create a folder named `YYYY-MM-DD-slug/` inside `portfolio_drop/` and put your images in it:

```
portfolio_drop/
  2025-03-01-new-piece/
    image1.jpg
    image2.png
    image3.tiff
```

- Images are sorted by filename. The **first one becomes the preview** (homepage grid).
- Supported formats: jpg, jpeg, png, tiff, tif, webp, heic, bmp.
- The slug becomes the title (e.g., `new-piece` → "New Piece").

### 2. Run the script

```bash
# Preview what will happen (no files written)
python3 new_artwork.py --dry-run

# Process all folders
python3 new_artwork.py
```

The script will:
- Convert all images to **1200px-wide webp** (quality 82)
- Name them `{slug}-preview.webp`, `{slug}-02.webp`, `{slug}-03.webp`, ...
- Generate **mobile** (576px) and **tablet** (992px) responsive variants of the preview
- Create the markdown post in `_posts/portfolio/` with frontmatter and image references

### 3. Fill in the post details

Open the generated `_posts/portfolio/YYYY-MM-DD-slug.md` and fill in the optional fields (description, ink, pen, price, etc.).

### Requirements

- macOS `sips` (built-in) for image resizing
- `cwebp` for webp conversion: `brew install webp`

---

## Creating Other Posts

For exhibitions, commissions, and bits, create posts manually.

### Post Templates

#### Portfolio Post (auto-generated by `new_artwork.py`)
```markdown
---
layout: post
title: "Your Artwork Title"
seo-title: "Your Artwork Title - Algorithmic Pen Plotted Art | Targz"
description: ""
date: YYYY-MM-DD
category: portfolio
image: /assets/images/portfolio/YYYY-MM-DD-slug/slug-preview.webp
ink: ""
pen: ""
frame: ""
stripe_url: ""
price: ""
stock: ""
---

![]({{ site.baseurl }}/assets/images/portfolio/YYYY-MM-DD-slug/slug-02.webp)
```

#### Exhibition Post
```markdown
---
layout: post
title: "Exhibition Name"
date: YYYY-MM-DD
category: exhibitions
image: /assets/images/exhibitions/YYYY-MM-DD-slug/slug-preview.webp
location: "Gallery Name, City"
---
Your content here...
```

#### Bits Post
```markdown
---
layout: post
title: "Experiment Name"
date: YYYY-MM-DD
category: bits
image: /assets/images/bits/YYYY-MM-DD-slug/slug-preview.webp
---
Your content here...
```

### Front Matter Fields

**Required fields:**
- `layout`: `post` for all categories
- `title`: The title of your piece
- `date`: Publication date in YYYY-MM-DD format
- `category`: One of: portfolio, bits, exhibitions, commissions
- `image`: Path to preview image

**Optional fields (portfolio):**
- `seo-title`: Custom SEO title
- `description`: Post description
- `ink`: Ink type used
- `pen`: Pen type used
- `frame`: Frame details
- `stripe_url`: Stripe payment link
- `price`: Artwork price
- `stock`: Stock status

**Optional fields (exhibitions):**
- `location`: Gallery/venue location

### Publishing

1. Save your post in the appropriate `_posts/[category]/` folder
2. Test locally with `bundle exec jekyll serve`
3. Commit and push to GitHub
4. GitHub Actions will automatically build and deploy

## Deployment

The site is automatically deployed to GitHub Pages on every push to the main branch.

Live site: [https://targz.github.io/targz.fr-2025](https://targz.github.io/targz.fr-2025)

## Features

- **Minimalist Navigation** - Burger menu with clean typography
- **Image Overlays** - Artwork titles positioned on images
- **Responsive Grid** - 2-column desktop, 1-column mobile layout
- **Blog Migration** - Python script for importing from Shopify
- **SEO Optimized** - Meta tags and structured data

## License

**Code & Portfolio Framework**: This project's code and portfolio framework are licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

**Content & Artwork**: All images, texts, and artworks are copyrighted by Targz. All rights reserved. The artwork and content may not be reproduced, distributed, or used without explicit permission.