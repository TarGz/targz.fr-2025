#!/usr/bin/env bash
#
# install.sh — One-shot Jekyll setup for targz.fr on a fresh Mac.
#
# Installs Homebrew Ruby (system Ruby 2.6 is too old for Jekyll 4.3),
# wires it into your shell PATH, then runs `bundle install` so the site
# is ready to serve. Does NOT start the server — run `bundle exec jekyll
# serve` yourself afterwards.
#
# Idempotent — safe to re-run.
#
# Usage:
#   ./install.sh

set -euo pipefail

PORT=4001
RUBY_PREFIX="/opt/homebrew/opt/ruby"   # Apple Silicon. Intel: /usr/local/opt/ruby
SHELL_RC="$HOME/.zshrc"                # adjust if you use bash

say()  { printf "\033[1;34m==>\033[0m %s\n" "$*"; }
warn() { printf "\033[1;33m!!\033[0m %s\n" "$*"; }
die()  { printf "\033[1;31mxx\033[0m %s\n" "$*" >&2; exit 1; }

# 1. Homebrew --------------------------------------------------------------
if ! command -v brew >/dev/null 2>&1; then
  die "Homebrew not found. Install it first: https://brew.sh"
fi
say "Homebrew: $(brew --version | head -1)"

# 2. Ruby (via brew) -------------------------------------------------------
if [ ! -x "$RUBY_PREFIX/bin/ruby" ]; then
  say "Installing Ruby via Homebrew…"
  brew install ruby
else
  say "Ruby already installed: $("$RUBY_PREFIX/bin/ruby" -v)"
fi

# Pin this script to the brew Ruby toolchain regardless of caller PATH.
RUBY_VERSION_SHORT=$("$RUBY_PREFIX/bin/ruby" -e 'puts RUBY_VERSION.split(".")[0,2].join(".")+".0"')
GEM_BIN="$RUBY_PREFIX/lib/ruby/gems/$RUBY_VERSION_SHORT/bin"
export PATH="$RUBY_PREFIX/bin:$GEM_BIN:$PATH"
hash -r 2>/dev/null || true

say "Using ruby:   $(command -v ruby)  ($(ruby -v))"

# 3. Persist PATH in shell rc ---------------------------------------------
PATH_LINE='export PATH="/opt/homebrew/opt/ruby/bin:$PATH"'
if [ -f "$SHELL_RC" ] && ! grep -qF "$PATH_LINE" "$SHELL_RC"; then
  say "Adding Ruby to PATH in $SHELL_RC"
  printf '\n# Homebrew Ruby for Jekyll (targz.fr)\n%s\n' "$PATH_LINE" >> "$SHELL_RC"
else
  say "Shell PATH already configured."
fi

# 4. Bundler + gems --------------------------------------------------------
BUNDLE="$RUBY_PREFIX/bin/bundle"
if [ ! -x "$BUNDLE" ]; then
  say "Installing bundler into Homebrew Ruby…"
  "$RUBY_PREFIX/bin/gem" install bundler --no-document
fi
say "Using bundler: $BUNDLE  ($("$BUNDLE" -v))"

# If a Gemfile.lock pins a specific bundler that's not installed, grab it.
if [ -f Gemfile.lock ]; then
  PINNED=$(awk '/^BUNDLED WITH/{getline; gsub(/^ +| +$/,""); print; exit}' Gemfile.lock || true)
  if [ -n "${PINNED:-}" ] && ! "$RUBY_PREFIX/bin/gem" list -i bundler -v "$PINNED" >/dev/null 2>&1; then
    say "Installing pinned bundler $PINNED from Gemfile.lock…"
    "$RUBY_PREFIX/bin/gem" install bundler -v "$PINNED" --no-document
  fi
fi

# Vendor gems inside the project so we never touch system Ruby.
say "Installing project gems (bundle install)…"
"$BUNDLE" config set --local path 'vendor/bundle'
"$BUNDLE" install

# 5. Done ------------------------------------------------------------------
say "Install complete."
echo
echo "  To start the site, open a NEW terminal (so PATH picks up) and run:"
echo "    bundle exec jekyll serve --port $PORT --livereload"
echo "  Then visit: http://localhost:$PORT"
echo
echo "  If \`which bundle\` still points to /usr/bin/bundle in an existing"
echo "  terminal, run:  source $SHELL_RC"
echo
