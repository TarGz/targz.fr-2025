const VERSION = "1.1.2";

const CHANGELOG = [
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
