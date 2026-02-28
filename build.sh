#!/bin/bash

# Navigate to the script's directory
cd "$(dirname "$0")"

echo "Building Jekyll site for production..."
JEKYLL_ENV=production bundle exec jekyll build

echo "Build complete! The site is available in the _site directory."
