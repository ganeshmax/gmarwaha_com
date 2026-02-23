#!/usr/bin/env python3
"""
Fix the "Mobile Payments Blog Series" wrapped sections that contain a prose paragraph
with inline markdown links (not a bullet list).

These look like:
<div class="related-reading">
<p class="related-reading-title">Mobile Payments Blog Series</p>
Welcome to the [Mobile payments FAQ...](/url) series and you are on FAQ #N. ...
</div>

We convert the inline markdown links to HTML <a> tags in the prose text.
"""

import os
import re

POSTS_DIR = os.path.join(os.path.dirname(__file__), '..', '_posts')

# Match the wrapped prose paragraph
WRAPPED_PROSE_RE = re.compile(
    r'(<div class="related-reading">\s*\n<p class="related-reading-title">[^<]+</p>\s*\n)(.*?)(</div>)',
    re.DOTALL
)

# Inline markdown link: [text](url)
MD_INLINE_LINK_RE = re.compile(r'\[([^\]]+)\]\(([^\)]+)\)')


def convert_inline_links(text):
    """Convert [text](url) to <a href="url">text</a> in prose text."""
    return MD_INLINE_LINK_RE.sub(r'<a href="\2">\1</a>', text)


total = 0

for fname in sorted(os.listdir(POSTS_DIR)):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(POSTS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    def fix_div(m):
        header = m.group(1)
        body = m.group(2)
        closing = m.group(3)
        # Check if it still has un-converted markdown links
        if '[' in body and '](' in body:
            converted = convert_inline_links(body)
            return header + converted + closing
        return m.group(0)

    new_content = WRAPPED_PROSE_RE.sub(fix_div, content)

    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Fixed prose links: {fname}")
        total += 1

print(f"\nDone. Fixed {total} files.")
