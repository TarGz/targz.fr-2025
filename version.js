const VERSION = "1.10.0";

const CHANGELOG = [
  {
    version: "1.10.0",
    date: "2026-07-05",
    changes: [
      "Add The Last Brain Cell portfolio post with responsive images",
      "Add Pillow fallback to new_artwork.py when cwebp is not installed",
      "Document the artwork contribution workflow in README and CLAUDE.md",
      "Remove invalid-dated draft duplicate (2026-06-31-the-last-brain-cells)"
    ]
  },
  {
    version: "1.9.1",
    date: "2026-06-18",
    changes: [
      "Fix spelling and grammar in about.md"
    ]
  },
  {
    version: "1.9.0",
    date: "2026-05-25",
    changes: [
      "Add install.sh bootstrap script (Homebrew Ruby + bundler + vendored gems)",
      "Document local install/run flow in README"
    ]
  },
  {
    version: "1.8.1",
    date: "2026-05-24",
    changes: [
      "Rename Grand Palais 2025 post title to Comparaison 2025, update preview image",
      "Rename Art Capital 2026 post title to Comparaison 2026, update preview image",
      "Add Lines By Lines CAYO exhibition photos (IMG_8280-8514)",
      "Add preview images for Comparaison 2025, Comparaison 2026, Lines By Lines CAYO"
    ]
  },
  {
    version: "1.8.0",
    date: "2026-05-24",
    changes: [
      "Add Rouen National Arts 2026 exhibition post (Biennale RNA, Halle aux Toiles)",
      "Add Matilda's series: Y¹ Nettie Stevens, Y² Lise Meitner",
      "Add post-columns-2 and col-text CSS classes for image+text two-column layout",
      "Add image-columns-2 square variant for 1:1 aspect ratio",
      "Add Y1 and Y2 artwork images and preview for RNA 2026 post"
    ]
  },
  {
    version: "1.7.2",
    date: "2026-05-24",
    changes: [
      "Add Lines By Lines exhibition post (CAYO Paris Treize, October 2025)",
      "Add CAYO Coffee Pack commission post",
      "Add exhibition and commission images with responsive webp conversion"
    ]
  },
  {
    version: "1.7.1",
    date: "2026-05-23",
    changes: [
      "Auto-generate llms.txt from Jekyll posts on every build via _plugins/generate_llms.rb",
      "Remove static llms.txt (now managed by generator)"
    ]
  },
  {
    version: "1.7.0",
    date: "2026-05-20",
    changes: [
      "Rewrite artist statement on about page",
      "Add community shoutout and resource links (Drawingbots, vpype, grbl, Bantam Tools)",
      "Add link to bits exploration page"
    ]
  },
  {
    version: "1.6.0",
    date: "2026-04-16",
    changes: [
      "Add Art Capital 2026 exhibition post (Comparaison, Grand Palais)",
      "Add responsive images for Art Capital 2026 (preview, dome, setup)"
    ]
  },
  {
    version: "1.5.1",
    date: "2026-04-07",
    changes: [
      "Add llms.txt for LLM discoverability (artist bio, series, exhibitions, techniques)",
      "Remove noai robots directive — welcome LLM indexing",
      "Link llms.txt from HTML head for crawler discovery"
    ]
  },
  {
    version: "1.5.0",
    date: "2026-04-07",
    changes: [
      "Rewrite README as artist portfolio with copyright and SEO keywords",
      "Move dev documentation to CONTRIBUTING.md",
      "Add copyright, author, and keyword meta tags to head",
      "Strengthen footer copyright to explicitly cover artworks and images"
    ]
  },
  {
    version: "1.4.0",
    date: "2026-04-07",
    changes: [
      "Add new portfolio artworks: Plasama Churn, Y1, Y2",
      "Replace Synapses Canvas, Crops, Fragmentation preview images with correct framed versions"
    ]
  },
  {
    version: "1.3.1",
    date: "2026-04-07",
    changes: [
      "Auto-clean portfolio_drop/ folders after processing in new_artwork.py",
      "Update CLAUDE.md workflow docs to reflect cleanup step"
    ]
  },
  {
    version: "1.3.0",
    date: "2026-04-07",
    changes: [
      "Add new portfolio artwork: Crops (2025-10-20)",
      "Add new portfolio artwork: Fragmentation (2025-10-21)",
      "Remove shop fields from new_artwork.py post template (shopify_id, stripe_url, price, stock)"
    ]
  },
  {
    version: "1.2.1",
    date: "2026-04-07",
    changes: [
      "Add utility scripts: new_artwork.py, check_404_urls.py, organize_images.py, restructure_images.py",
      "Gitignore temporary report files (*.csv, *_report.txt)"
    ]
  },
  {
    version: "1.2.0",
    date: "2026-04-07",
    changes: [
      "Add all portfolio images in dated subfolder structure (42 artwork folders)",
      "Add tablet responsive variants for bits, commissions, exhibitions, portfolio"
    ]
  },
  {
    version: "1.1.3",
    date: "2026-04-07",
    changes: [
      "Simplify dev server flags (remove --incremental --verbose)",
      "Remove orphaned synapses_canvas video file"
    ]
  },
  {
    version: "1.1.2",
    date: "2026-04-07",
    changes: [
      "Update README with new image directory convention and project structure",
      "Add portfolio_drop/ to .gitignore",
      "Remove .jekyll-metadata from tracking"
    ]
  },
  {
    version: "1.1.1",
    date: "2026-04-07",
    changes: [
      "Fix responsive image path generation in home layout for new subfolder structure"
    ]
  },
  {
    version: "1.1.0",
    date: "2026-04-07",
    changes: [
      "Restructure all images into dated category subfolders (bits, commissions, exhibitions, portfolio)",
      "Update image paths in all bits, commissions, and exhibitions posts",
      "Move mobile/tablet responsive variants into matching subfolder structure"
    ]
  },
  {
    version: "1.0.0",
    date: "2026-04-07",
    changes: [
      "Remove shop/product features from theme (specs, pricing, buy links)",
      "Redesign navigation: logo left, shop button + burger right",
      "Add fullscreen menu overlay with generative art background",
      "Strip price/stock/stripe_url from all portfolio front matter",
      "Delete Shopify/Stripe migration scripts and data files",
      "Restore shop link in navbar and footer"
    ]
  }
];

module.exports = { VERSION, CHANGELOG };
