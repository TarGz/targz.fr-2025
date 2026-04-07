const VERSION = "1.4.0";

const CHANGELOG = [
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
