#!/usr/bin/env python3
"""
Rewrite all absolute gmarwaha.com/blog URLs in _posts markdown files
to Jekyll-compatible relative paths.

e.g. https://www.gmarwaha.com/blog/2014/10/20/mobile-payments-what-is-apple-pay/
  -> /2014/10/20/mobile-payments-what-is-apple-pay.html
"""

import os
import re

POSTS_DIR = os.path.join(os.path.dirname(__file__), '..', '_posts')

# Matches absolute gmarwaha blog URLs in markdown link syntax and raw text
# Groups: (1) year, (2) month, (3) day, (4) slug
BLOG_URL_RE = re.compile(
    r'https?://(?:www\.)?gmarwaha\.com/blog/(\d{4})/(\d{2})/(\d{2})/([^/\s"\')\]]+)/?'
)

def replace_url(match):
    year, month, day, slug = match.groups()
    # Strip any trailing punctuation from slug that may have been captured
    slug = slug.rstrip('.,;:')
    return f'/{year}/{month}/{day}/{slug}.html'

total_replacements = 0
total_files = 0

for fname in sorted(os.listdir(POSTS_DIR)):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(POSTS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, count = BLOG_URL_RE.subn(replace_url, content)
    if count > 0:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  {fname}: {count} URL(s) replaced")
        total_replacements += count
        total_files += 1

print(f"\nDone. Replaced {total_replacements} URLs across {total_files} files.")
