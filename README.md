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
   bundle exec jekyll serve
   # Or with live reload:
   bundle exec jekyll serve --livereload
   ```

5. Open your browser to `http://localhost:4000`

## Project Structure

```
├── _posts/           # Portfolio pieces and blog posts
├── _layouts/         # Jekyll layout templates
├── _includes/        # Reusable HTML components
├── assets/
│   ├── images/       # Artwork images and assets
│   └── css/          # Custom stylesheets
├── _config.yml       # Jekyll configuration
└── migrate_blog.py   # Shopify blog migration script
```

## Content Categories

- **Portfolio** (`category: portfolio`) - Featured pen plotting artworks
- **Updates** (`category: updates`) - News and project updates

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