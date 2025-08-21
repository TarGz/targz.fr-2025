#!/bin/bash

echo "🚀 Starting Jekyll with drafts enabled..."
echo "📝 Drafts from _drafts/ folder will be visible"
echo "🌐 Server will run on http://localhost:4001"
echo ""

# Clean Jekyll cache first
bundle exec jekyll clean

# Start Jekyll with drafts enabled
bundle exec jekyll serve --port 4001 --livereload --drafts

# The --drafts flag will:
# - Show all posts in _drafts/ folder
# - Use current date/time for draft posts
# - Allow you to preview content before publishing