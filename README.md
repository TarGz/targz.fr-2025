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
├── _posts/           # Published blog posts
│   ├── portfolio/    # Artwork posts
│   ├── bits/         # Experiments
│   ├── exhibitions/  # Show documentation
│   └── commissions/  # Custom projects
├── _drafts/          # Unpublished draft posts & templates
├── _layouts/         # Jekyll layout templates
├── _includes/        # Reusable HTML components
├── _plugins/         # Jekyll plugins (responsive images)
├── assets/
│   ├── images/       # Artwork images and assets
│   │   ├── mobile/   # Auto-generated mobile images
│   │   └── tablet/   # Auto-generated tablet images
│   └── css/          # Custom stylesheets
├── _config.yml       # Jekyll configuration
├── startlocaldev.sh  # Local development script
└── startlocaldev-draft.sh  # Local development with drafts
```

## Content Categories

- **Portfolio** (`category: portfolio`) - Featured pen plotting artworks
- **Bits** (`category: bits`) - Experiments and works in progress
- **Exhibitions** (`category: exhibitions`) - Show documentation and gallery features
- **Commissions** (`category: commissions`) - Custom projects and collaborations
- **Updates** (`category: updates`) - News and project updates

## Creating New Posts

### Working with Drafts

#### Quick Start for Drafts

1. **Copy the appropriate template** from `_drafts/TEMPLATE-[category]-post.md`
2. **Save it in `_drafts/`** with any name: `your-title-here.md` (no date needed for drafts)
3. **Update the front matter** (the content between `---` markers)
4. **Add your images** to `/assets/images/`
5. **Preview locally** using `./startlocaldev-draft.sh` to see drafts
6. **When ready to publish**, move to `_posts/[category]/` with proper date prefix

#### Testing Drafts Locally

```bash
# Start local server WITH draft posts visible
./startlocaldev-draft.sh

# Or manually:
bundle exec jekyll serve --port 4001 --livereload --drafts
```

Drafts will appear with today's date when viewing locally.

#### Publishing a Draft

When your draft is ready:
1. Move it from `_drafts/` to the appropriate `_posts/[category]/` folder
2. Rename it with date prefix: `YYYY-MM-DD-your-title.md`
3. Commit and push to publish

### Image Requirements

#### Main Images
- **Preview image** (for homepage grid): Name it `your-artwork-preview.webp`
  - Recommended size: 704x990px (portrait orientation)
  - This will be automatically resized for mobile/tablet
  
#### Responsive Images (Generated Automatically)
The Jekyll plugin automatically creates responsive versions:
- Mobile: 400px width (saved in `/assets/images/mobile/`)
- Tablet: 600px width (saved in `/assets/images/tablet/`)

#### Image Optimization Tips
- Use `.webp` format for best performance
- Compress images before uploading
- Keep file sizes under 500KB when possible

### Post Templates

#### Portfolio Post
```markdown
---
layout: portfolio
title: "Your Artwork Title"
date: YYYY-MM-DD
category: portfolio
image: /assets/images/your-artwork-preview.webp
detail_image: /assets/images/your-artwork-detail.webp
size: "50 x 70 cm"
support: "Bristol Paper 180g"
ink: "Pigment Liner"
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
image: /assets/images/your-bit-preview.webp
---
Your content here...
```

#### Exhibition Post
```markdown
---
layout: post
title: "Exhibition Name"
date: YYYY-MM-DD
category: exhibitions
image: /assets/images/exhibition-preview.webp
location: "Gallery Name, City"
---
Your content here...
```

#### Commission Post
```markdown
---
layout: post
title: "Project Name"
date: YYYY-MM-DD
category: commissions
image: /assets/images/commission-preview.webp
client: "Client Name"
---
Your content here...
```

### Front Matter Fields

**Required fields:**
- `layout`: Use `portfolio` for portfolio posts, `post` for others
- `title`: The title of your piece
- `date`: Publication date in YYYY-MM-DD format
- `category`: One of: portfolio, bits, exhibitions, commissions
- `image`: Path to preview image

**Optional fields:**
- `detail_image`: Full resolution detail shot (portfolio)
- `size`: Artwork dimensions (portfolio)
- `support`: Paper/material type (portfolio)
- `ink`: Pen/ink type used (portfolio)
- `price`: Artwork price (portfolio)
- `status`: "available" or "sold" (portfolio)
- `location`: Gallery/venue location (exhibitions)
- `client`: Client name (commissions)
- `tags`: Array of tags like ["geometric", "moire", "abstract"]

### Writing Content

Use standard Markdown syntax:
- `## Heading 2` for section headers
- `**bold text**` for emphasis
- `![Image Alt Text](/assets/images/image.webp)` for images
- `` `code` `` for inline code
- ` ```language ... ``` ` for code blocks

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