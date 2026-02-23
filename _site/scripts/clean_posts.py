#!/usr/bin/env python3
"""
Clean up posts by removing the decorative "series banner" image+link block
that appears at the top of many imported posts. These were visual navigation
elements on the original site and serve no purpose as content.

Pattern to remove (after front matter):
Lines that look like:
  [
      ![...](img-url)
  ](some-url)

Also removes leading whitespace-only lines after front matter.
"""

import os
import re

POSTS_DIR = os.path.join(os.path.dirname(__file__), '..', '_posts')

# Match the decorative banner: an image inside a link, possibly with lots of whitespace
# This looks like: [\n\t\n\t![](...)\n\t](url)\n
BANNER_RE = re.compile(
    r'^\s*\[\s*\n\s*!\[.*?\]\(https?://[^\)]+\)\s*\n\s*\]\(https?://[^\)]+\)\s*\n',
    re.MULTILINE
)

# Also strip any purely-whitespace lines at the very start of content (after front matter)
LEADING_BLANK_RE = re.compile(r'^(\n\s*)+', re.MULTILINE)

total = 0

for fname in sorted(os.listdir(POSTS_DIR)):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(POSTS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split off front matter
    if not content.startswith('---'):
        continue
    parts = content.split('---', 2)
    if len(parts) < 3:
        continue
    front_matter = '---' + parts[1] + '---'
    body = parts[2]

    original_body = body
    # Remove the banner block
    body = BANNER_RE.sub('', body)
    # Remove excessive leading blank lines
    body = body.lstrip('\n')
    body = '\n' + body  # ensure one leading newline after front matter

    if body != '\n' + original_body.lstrip('\n'):
        new_content = front_matter + body
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Cleaned: {fname}")
        total += 1

print(f"\nDone. Cleaned {total} files.")
