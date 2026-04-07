const VERSION = "1.1.0";

const CHANGELOG = [
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
