#!/bin/bash

# Navigate to the script's directory (in case it is run from elsewhere)
cd "$(dirname "$0")"

echo "Starting Jekyll server with LiveReload on port 4001..."
bundle exec jekyll serve --livereload --port 4001
